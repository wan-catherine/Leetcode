import collections

class Solution(object):
    def accountsMerge_before(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        connections = collections.defaultdict(list)
        self.parents = {}
        self.sizes = {}
        for index, li in enumerate(accounts):
            length = len(li)
            for i in range(1,length):
                connections[li[i]].append(f"{index}_{i}")
                self.parents[f"{index}_{i}"] = f"{index}_{1}"
                self.sizes[f"{index}_{i}"] = 1

        for email in connections:
            l = len(connections[email])
            if l < 2:
                continue
            a = connections[email][0]
            for i in range(1, l):
                self.union(a, connections[email][i])

        mapping = collections.defaultdict(set)
        for key in self.parents:
            mapping[self.find(self.parents[key])].add(key)

        res = []
        for key in mapping:
            index = int(key[:key.index('_')])
            temp = set()
            name = accounts[index][0]
            for index_i in mapping[key]:
                pos = index_i.index('_')
                i, j = int(index_i[:pos]), int(index_i[pos+1])
                temp.add(accounts[i][j])
            res.append([name] + sorted(temp))

        return res

    def union(self, a , b):
        a_p, b_p = self.find(a), self.find(b)
        if a_p == b_p:
            return
        if self.sizes[a_p] < self.sizes[b_p]:
            self.parents[a_p] = self.parents[b_p]
            self.sizes[b_p] += self.sizes[a_p]
        else:
            self.parents[b_p] = self.parents[a_p]
            self.sizes[a_p] += self.sizes[b_p]

    def find(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a

    """
    update : 20210117
    use all email to do union-find 
    owner : email -> name
    after union , we get the parents, then we call find(x) to find each email's root email. 
    mapping : rootemail : all other emails in the same group 
    """
    def accountsMerge(self, accounts):
        owner = collections.defaultdict(str)
        parents = collections.defaultdict(str)
        sizes = collections.defaultdict(int)
        noemails = set()

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            if sizes[pp] < sizes[pq]:
                parents[pp] = pq
                sizes[pq] += sizes[pp]
            else:
                parents[pq] = pp
                sizes[pp] += sizes[pq]

        for li in accounts:
            name = li[0]
            if len(li) == 1:
                noemails.add(name)
                continue
            if li[1] not in parents:
                owner[li[1]] = name
                parents[li[1]] = li[1]
                sizes[li[1]] = 1
            for em in li[2:]:
                owner[em] = name
                if em not in parents:
                    parents[em] = em
                    sizes[em] = 1
                union(em, li[1])

        mapping = collections.defaultdict(set)
        for em in parents:
            root = find(em)
            mapping[root].add(em)

        res = []
        for root in mapping:
            ans = [owner[root]]
            ans.extend(sorted(mapping[root]))
            res.append(ans)
        return res



