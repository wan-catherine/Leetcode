class Solution:
    def minWindow(self, s, t):
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





