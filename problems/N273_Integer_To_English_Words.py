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
