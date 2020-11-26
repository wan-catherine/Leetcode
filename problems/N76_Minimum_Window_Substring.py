import collections


class Solution:
    def minWindow_before(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or len(s) < len(t):
            return ""

        t_dict = {}
        for i in t:
            t_dict[i] = t_dict.setdefault(i, 0) + 1

        i, j = 0, 0
        window = {}
        valid_count = 0
        s_len = len(s)
        t_len = len(t_dict)
        res = ""
        while j < s_len:
            if s[j] in t_dict:
                window[s[j]] = window.setdefault(s[j],0) + 1
                if window[s[j]] == t_dict[s[j]]:
                    valid_count += 1
            j += 1

            while valid_count == t_len:
                if not res:
                    res = s[i:j]
                else:
                    res = s[i:j] if j-i < len(res) else res

                if s[i] in t_dict:
                    if window[s[i]] == t_dict[s[i]]:
                        valid_count -= 1
                    window[s[i]] -= 1
                i += 1
        return res

    """
    Slide window 
    The key point is how to check the substring already contains t. 
    We use hashmap and correct_num . 
    correct_num shows how many unique character already have no less than t's number. 
    """
    def minWindow(self, s: str, t: str) -> str:
        count = collections.defaultdict(int)
        for c in t:
            count[c] += 1
        sl, tl = len(s), len(count.keys())
        left, right = 0, 0
        valid = collections.defaultdict(int)
        correct_num = 0
        res = ""
        while right < sl:
            if s[right] in count.keys():
                valid[s[right]] += 1
                if valid[s[right]] == count[s[right]]:
                    correct_num += 1

                while correct_num == tl:
                    if not res:
                        res = s[left:right + 1]
                    else:
                        res = s[left:right + 1] if right - left + 1 < len(res) else res

                    if s[left] in count.keys():
                        valid[s[left]] -= 1
                        if valid[s[left]] < count[s[left]]:
                            correct_num -= 1
                    left += 1
            right += 1
        return res



