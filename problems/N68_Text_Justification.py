from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words.append('#'*maxWidth)
        res = []
        count, current, length = 0, [], 0
        for j in range(len(words)):
            word = words[j]
            if j == len(words) - 1 or count + len(word) >= maxWidth:
                flag = False
                if count + len(word) == maxWidth:
                    current.append(word)
                    length += len(word)
                    flag = True
                lc = len(current)
                if lc == 1:
                    ans = current[0] + ' ' * (maxWidth - len(current[0]))
                elif j== len(words) - 1:
                    ans = ' '.join(current)
                    ans += ' ' * (maxWidth - len(ans))
                else:
                    spaces = maxWidth - length
                    inter = spaces // (lc - 1)
                    left = spaces % (lc - 1)
                    ans = ""
                    for i in range(lc-1):
                        ans += current[i]
                        ans += ' ' * inter
                        if left > 0:
                            ans += ' '
                            left -= 1
                    ans += current[-1]
                res.append(ans)
                if flag:
                    count, current, length = 0, [], 0
                else:
                    count, current, length = len(word) + 1, [word], len(word)
            else:
                count += len(word)
                count += 1
                current.append(word)
                length += len(word)
        if res[-1] == '#' * maxWidth:
            res = res[:-1]
        return res


