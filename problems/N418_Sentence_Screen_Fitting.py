from typing import List
"""
Given a rows x cols screen and a sentence represented by a list of non-empty words, 
find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sentence-screen-fitting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        for word in sentence:
            if len(word) > cols:
                return 0
        st = ' '.join(sentence)
        st += ' '
        length = len(st)
        i = 0
        for r in range(rows):
            i += cols
            while st[i % length] != ' ':
                i -= 1
            i += 1
        return i // length
