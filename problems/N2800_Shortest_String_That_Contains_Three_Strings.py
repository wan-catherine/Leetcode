import collections


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def helper(p, q, k):
            lp, lq, lk = len(p), len(q), len(k)

            for i in range(lp):
                j = 0
                c = i
                while j < lq and c < lp:
                    if p[c] == q[j]:
                        j += 1
                        c += 1
                    else:
                        break
                if j == lq:
                    res = p
                    break
                elif c == lp:
                    res = p[:i] + q
                    break
            else:
                res = p + q
            lr = len(res)
            for i in range(lr):
                j, c = 0, i
                while j < lk and c < lr:
                    if k[j] == res[c]:
                        j += 1
                        c += 1
                    else:
                        break
                if j == lk:
                    break
                elif c == lr:
                    res += k[j:]
                    break
            else:
                res += k
            return res

        li = helper(a,b,c), helper(a,c,b), helper(b,a,c), helper(b,c,a),helper(c,a,b), helper(c,b,a)
        mapping = collections.defaultdict(list)
        for s in li:
            mapping[len(s)].append(s)
        keys = sorted(mapping.keys())
        return min(mapping[keys[0]])

