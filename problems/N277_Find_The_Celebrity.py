# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


"""
each call of know(a, b), we can make sure one of (a,b) is not celebrity. 
1. know(a,b)==True ==> a is not celebrity, so candidate = b
2. know(a,b)==False ==> b is not celebrity, so candidate = a

Then we need to check for candidate , all other people know he/she, but he/she doesn't know any of them.

So two pass , O(N) can solve this.

"""
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate

