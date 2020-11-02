class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        length = len(num)
        res = []
        def dfs(pos, prev, last, prev_s):
            if pos == length:
                if prev == target:
                    res.append(prev_s)
                return
            for i in range(pos+1, length+1):
                cur_s = num[pos:i]
                if len(cur_s) > 1 and cur_s[0] == '0':
                    continue
                cur = int(cur_s)
                if pos == 0:
                    dfs(i, cur, cur, cur_s)
                else:
                    dfs(i, prev + cur, cur, prev_s + '+' + cur_s)
                    dfs(i, prev - cur, -cur, prev_s + '-' + cur_s)
                    dfs(i, prev - last + last * cur, last * cur, prev_s + '*' + cur_s)
        dfs(0, 0, 0, "")
        return res
                
