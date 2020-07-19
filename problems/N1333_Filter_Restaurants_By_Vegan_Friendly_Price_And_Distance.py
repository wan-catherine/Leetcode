class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        res = []
        for id, rating, vegan, price, distance in restaurants:
            if veganFriendly:
                if not vegan:
                    continue
            if price > maxPrice or distance > maxDistance:
                continue
            # res.append([id, rating])
            res.append([rating, id])

        # res.sort(key=lambda r: (r[1],r[0]), reverse=True) #This is the way to sort by multiple attributes
        res.sort(reverse=True)
        return [i[1] for i in res]
