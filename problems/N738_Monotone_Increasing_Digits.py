class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = str(N)
        length = len(s)
        res = []
        for i in range(length):
            j = i
            flag = False
            while j + 1 < length:
                if s[j] < s[j+1]:
                    flag = True
                    break
                elif s[j] == s[j+1]:
                    j += 1
                    continue
                else:
                    break

            if flag:
                res.append(s[i])
            else:
                if s[i] == '1':
                    if i == 0:
                        return int('9' * (length - 1))
                else:
                    if i == length - 1:
                        res.append(s[i])
                    else:
                        res.append(str(int(s[i]) - 1))
                    return int(''.join(res) + '9'*(length - i - 1))
        return int(''.join(res))