import heapq
from asyncio import PriorityQueue


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        a1,b1,c1 = 0, 0, 0
        res = []
        while a >= 0 or b >= 0 or c >= 0:
            if a >= b and a >= c:
                while a1 < 2 and a > 0:
                    res.append('a')
                    b1,c1 = 0, 0
                    a1+=1
                    a -= 1
                else:
                    if b >= c and b > 0:
                        res.append('b')
                        b1 += 1
                        b -= 1
                        a1,c1 = 0, 0
                    elif c >= b and c > 0:
                        res.append('c')
                        c1+=1
                        c -= 1
                        a1,b1 = 0, 0
                    else:
                        break
            elif b >= a and b >= c:
                while b1 < 2 and b > 0:
                    res.append('b')
                    a1,c1 = 0, 0
                    b1+= 1
                    b -= 1
                else:
                    if a >= c and a > 0:
                        res.append('a')
                        a1+=1
                        a-=1
                        b1,c1 = 0,0
                    elif c >= a and c > 0:
                        res.append('c')
                        c1+=1
                        c -= 1
                        a1, b1 = 0,0
                    else:
                        break
            elif c >= a and c >= b:
                while c1 < 2 and c > 0:
                    res.append('c')
                    c -= 1
                    c1 += 1
                    a1, b1 = 0, 0
                else:
                    if a >= b and a > 0:
                        res.append('a')
                        a -= 1
                        a1 += 1
                        b1,c1 = 0, 0
                    elif b >= a and b > 0:
                        res.append('b')
                        b -= 1
                        b1 += 1
                        a1,c1 = 0, 0
                    else:
                        break
        return ''.join(res)

    def longestDiverseString_20220731(self, a: int, b: int, c: int) -> str:
        fl, sl, tl = sorted([(a, 'a'), (b, "b"), (c, "c")], reverse=True)
        f, s, t = fl[0], sl[0], tl[0]

        if (f + 1) // 2 > s + t + 1:
            f = (s + t + 1) * 2
        rows = f // 2
        res = [[] for _ in range(rows)]
        for i in range(rows):
            res[i].append(fl[1] * 2)
        i = 0
        while s:
            res[i].append(sl[1])
            s -= 1
            i += 1
            i %= rows
        while t:
            res[i].append(tl[1])
            t -= 1
            i += 1
            i %= rows

        ans = ""
        for row in res:
            ans += ''.join(row)
        if f % 2:
            ans += fl[1]
        return ans

    def longestDiverseString_20241016(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        res = []
        while pq:
            if len(pq) == 1:
                res.append(pq[0][1] * min(2, (-pq[0][0])))
                break
            first, second = heapq.heappop(pq), heapq.heappop(pq)
            fv, fc = -first[0], first[1]
            sv, sc = -second[0], second[1]
            k = min(1 + fv - sv, 2)
            res.append(fc * k)
            res.append(sc)

            fv -= k
            sv -= 1

            if fv > 0:
                heapq.heappush(pq, (-fv, fc))
            if sv > 0:
                heapq.heappush(pq, (-sv, sc))
        return ''.join(res)




