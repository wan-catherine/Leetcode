"""
the key is : check the current digit, if it less than the previous digit , then delete the previous
and then check the new previous until the current digit is >= previous digit .

if loop out the num and k > 0 , the we know all the left digits are same .
so just remove the last k digits , we will get the result.
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digits = []
        i = 0
        while i < len(num):
            if not digits:
                digits.append(num[i])
                i+=1
            elif num[i] < digits[-1]:
                if k > 0:
                    digits.pop()
                    k -= 1
                else:
                    digits.append(num[i])
                    i += 1
            else:
                digits.append(num[i])
                i += 1
        digits=digits[:-k]  if k  else digits
        res = ''.join(digits).lstrip('0')
        return res if res else "0"
