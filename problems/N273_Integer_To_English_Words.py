class Solution:
    def numberToWords(self, num: int) -> str:
        tens = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        twenties = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        hundreds = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        if num == 0:
            return 'Zero'

        def helper(n):
            if n < 10:
                res = tens[n]
            elif n < 20:
                res = twenties[n-10]
            elif n < 100:
                res = hundreds[n//10] + " " + tens[n%10]
            elif n < 1000:
                res = helper(n//100) + " Hundred " + helper(n%100)
            elif n < 10**6:
                res = helper(n//1000) + " Thousand " + helper(n% 1000)
            elif n < 10**9:
                res = helper(n//10**6) + " Million " + helper(n%10**6)
            else:
                res = helper(n//10**9) + " Billion " + helper(n%10**9)
            return res.strip()
        return helper(num)

    def numberToWords(self, num: int) -> str:
        twenties = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        hundreds = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        bigs = ["Billion", "Million", "Thousand", ""]

        def helper(n):
            res = ''
            flag = False
            if n >= 100:
                res += twenties[n // 100] + ' Hundred'
                n = n % 100
                flag = True
            if n == 0:
                return res
            res += ' ' if flag else ''
            flag = False
            if n >= 20:
                res += hundreds[n // 10]
                n = n % 10
                flag = True
            if n == 0:
                return res
            res += ' ' if flag else ''
            if n > 0:
                res += twenties[n]
            return res

        if num == 0:
            return 'Zero'
        i = 10 ** 9
        res = ''
        j = 0
        while i > 0:
            if num >= i:
                res += helper(num // i)
                num = num % i
                res += " " + bigs[j] + " "
            j += 1
            i //= 10 ** 3
            # print(num, i )
        return res.strip()