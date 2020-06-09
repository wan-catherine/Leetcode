"""
for each number in the array ,
we need to consider his left and right subarray .
for left subarray, find the ll = count(number < value) and lh = count(number > value)
for right subarray, find the rh = count(number > value) and rl = count(number < value)

Then the count = ll*rh + lh*rl
"""
class Solution(object):
    def numTeams_bruteforce(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        count = 0
        rating_len = len(rating)
        if rating_len < 3 :
            return count

        for i in range(rating_len):
            for j in range(i+1, rating_len):
                if rating[i] > rating[j]:
                    for k in range(j+1, rating_len):
                        if rating[j] > rating[k]:
                            count += 1
                elif rating[i] < rating[j]:
                    for k in range(j+1, rating_len):
                        if rating[j] < rating[k]:
                            count += 1
        return count

    def numTeams(self, rating):
        count = 0
        rating_len = len(rating)
        for i in range(rating_len):
            value = rating[i]
            lh,ll,rh,rl = 0,0,0,0
            for num in rating[:i]:
                if num > value:
                    lh += 1
                elif num < value:
                    ll += 1
            for num in rating[i+1:]:
                if num > value:
                    rh += 1
                elif num < value:
                    rl += 1
            count += lh * rl + ll * rh
        return count