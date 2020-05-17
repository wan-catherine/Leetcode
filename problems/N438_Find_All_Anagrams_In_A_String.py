class Solution:
    def findAnagrams(self, s: str, p: str):
        if not s or len(s) < len(p):
            return []
        l = len(p)
        i, j = 0, l
        s_len = len(s)
        p_dict = {}
        res = []
        for key in p:
            p_dict[key] = p_dict.setdefault(key, 0) + 1
        re_set_temp_dict = True
        while i < s_len and j <= s_len:
            if re_set_temp_dict:
                temp_dict = {}
                for k in s[i:j]:
                    temp_dict[k] = temp_dict.setdefault(k, 0) + 1
            else:
                if temp_dict[s[i-1]] == 1:
                    del temp_dict[s[i-1]]
                else:
                    temp_dict[s[i-1]] -= 1
                temp_dict[s[j-1]] = temp_dict.setdefault(s[j-1], 0) + 1
            if temp_dict == p_dict:
                res.append(i)

            if j == s_len:
                break
            if j < s_len and s[j] not in p_dict:
                i = j + 1
                j = j + l + 1
                re_set_temp_dict = True
            else:
                # at this time, we just move i and j one character , so no need to reset temp_dict
                # just change the s[i-1] to s[j-1]
                i += 1
                j += 1
                re_set_temp_dict = False

        return res

