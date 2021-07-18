import collections
import heapq
from typing import List


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = collections.defaultdict(list)
        self.rented = []
        self.avail = {}
        self.price = {}
        for s, m, p in entries:
            heapq.heappush(self.movies[m], (p, s))
            self.avail[(s, m)] = True
            self.price[(s, m)] = p

    def search(self, movie: int) -> List[int]:
        res, temp = [], []
        if movie not in self.movies:
            return res
        while len(res) < 5 and self.movies[movie]:
            p, s = heapq.heappop(self.movies[movie])
            temp.append((p, s))
            if s not in res and self.avail[(s, movie)]:
                res.append(s)
        for t in temp:
            heapq.heappush(self.movies[movie], t)
        return res

    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        heapq.heappush(self.rented, (p, shop, movie))
        self.avail[(shop, movie)] = False

    def drop(self, shop: int, movie: int) -> None:
        self.avail[(shop, movie)] = True

    def report(self) -> List[List[int]]:
        res = []
        while len(res) < 5 and self.rented:
            p, s, m = heapq.heappop(self.rented)
            if not self.avail[(s, m)] and (not res or res[-1] != (p, s, m)):
                res.append((p, s, m))
        for t in res:
            heapq.heappush(self.rented, t)
        return [[s, m] for _, s, m in res]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()