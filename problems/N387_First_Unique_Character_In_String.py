class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        index_mapping = {}

        for i in range(len(s)):
            if s[i] in index_mapping:
                index_mapping[s[i]] = None
            else:
                index_mapping[s[i]] = i
        index = len(s)
        for key, value in index_mapping.items():
            if value == None:
                continue
            index = min(index, value)
        return index if index < len(s) else -1