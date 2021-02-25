import collections
"""
Notice puzzles[i].length == 7, so we can use bit manipulation . 
Loop all subset of puzzles[i], and check the subset . 

1. convert all word into a mask , and count each mask's number : count
2. for each puzzle, create all subsets :
    because it needs to contain the first letter , so mask initialized as mask = 1 << (ord(puzzle[0]) - ord('a'))
    for the left 6 position, create the subset:
        use the subset to get the position of the puzzle's letter and create mask.
        
KEY POINT : 
    puzzle's subset is about it's length (2 ** 6) , we need to translate it to mask format . 
"""

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        count = collections.defaultdict(int)
        for word in words:
            mask = 0
            w = set(word)
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            count[mask] += 1
        length = len(puzzles)
        res = [0] * length
        for index, puzzle in enumerate(puzzles):
            for subset in range(2**6):
                mask = 1 << (ord(puzzle[0]) - ord('a'))
                for i in range(6):
                    if subset & (1 << i):
                        mask |= 1 << (ord(puzzle[i+1]) - ord('a'))
                if mask in count:
                    res[index] += count[mask]

        return res


