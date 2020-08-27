class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S[0].isalpha():
            return self.mask_email(S)
        else:
            return self.mask_phone(S)

    def mask_email(self, s):
        index = s.index('@')
        new_s = s[0].lower() + '*'*5 + s[index-1].lower() + s[index:].lower()
        return new_s

    def mask_phone(self, s):
        nums = []
        for i in s:
            if i.isdigit():
                nums.append(i)
        length = len(nums)
        if length == 10:
            return "***-***-" + ''.join(nums[-4:])
        if length > 10:
            return '+' + '*' * (length-10) + '-***-***-' + ''.join(nums[-4:])