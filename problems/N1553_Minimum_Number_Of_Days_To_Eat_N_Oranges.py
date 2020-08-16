class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {1: 1, 2:2}
        self.check(n)
        # print(self.memo)
        return self.memo[n]

    def check(self,num):
        if num in self.memo:
            return self.memo[num]
        a = num
        if not num % 2:
            a = min(a, self.check(num // 2) + 1)
        else:
            a = min(a, self.check(num - 1) + 1)

        val = num % 3
        if not val:
            a = min(a, self.check(num//3) + 1)
        elif val == 1:
            a = min(a, 1 + self.check(num - 1))
        else:
            a = min(a, 2 + self.check(num - 2))

        self.memo[num] = a
        return a

    def check_timeout(self, num):
        if num in self.memo:
            return self.memo[num]
        left_two = num % 2
        left_three = num % 3
        if not left_two and not left_three:
            self.memo[num] = min(self.check(num - num // 2), self.check(num - 2 * num // 3)) + 1
            self.memo[num] = min(self.memo[num], self.check(num - 1) + 1)
        elif not left_two:
            self.memo[num] = self.check(num - num // 2) + 1
            self.memo[num] = min(self.memo[num], self.check(num - 1) + 1)
        elif not left_three:
            self.memo[num] = self.check(num - 2 * num // 3) + 1
            self.memo[num] = min(self.memo[num], self.check(num - 1) + 1)
        else:
            self.memo[num] = self.check(num - 1) + 1

        return self.memo[num]