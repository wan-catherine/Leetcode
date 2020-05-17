class Solution:
    def checkInclusion_mymethod(self, s1: str, s2: str) -> bool:
        if not s2 or len(s2) < len(s1):
            return False

        base_dict = {}
        for i in s1:
            base_dict[i] = base_dict.setdefault(i,0) + 1
        s2_len = len(s2)
        s1_len = len(s1)
        i,j = 0, s1_len
        reset = True
        while j <= s2_len:
            if reset:
                window = {}
                for k in s2[i:j]:
                    if k in base_dict:
                        window[k] = window.setdefault(k, 0) + 1
            if window == base_dict:
                return True
            if j == s2_len:
                return False
            if s2[j] in base_dict:
                reset = False
                window[s2[j]] = window.setdefault(s2[j], 0) + 1
                if s2[i] in window:
                    window[s2[i]] -= 1
                    if not window[s2[i]]:
                        del window[s2[i]]

                i += 1
                j += 1
            else:
                reset = True
                i = j + 1
                j += s1_len + 1
        return False

    # slide window method
    # it's much clear than the first one, but slower.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2 or len(s2) < len(s1):
            return False

        base_dict = {}
        for i in s1:
            base_dict[i] = base_dict.setdefault(i,0) + 1
        base_dict_count = len(base_dict)
        i,j = 0,0
        window = {}
        s2_len = len(s2)
        s1_len = len(s1)
        valid_count = 0
        while j < s2_len:
            c = s2[j]
            j += 1
            if c in base_dict:
                window[c] = window.setdefault(c,0) + 1
                if window[c] == base_dict[c]:
                    valid_count += 1
            if j-i== s1_len:
                if valid_count == base_dict_count:
                    return True
                c = s2[i]
                i += 1
                if c in base_dict:
                    if window[c] == base_dict[c]:
                        valid_count -= 1
                    window[c] -= 1
        return False




