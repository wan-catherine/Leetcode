import collections
import sys
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        ss = set()
        for s in stickers:
            ss.update(set(c for c in s))
        st = set(target)
        if st.difference(ss):
            return -1
        ct = collections.Counter(target)
        mapping = collections.defaultdict(dict)
        for st in stickers:
            count = collections.Counter(st)
            for key in ct.keys():
                if key not in count:
                    continue
                mapping[st][key] = count[key]

        memo = {}
        def dfs(state):
            if state in memo :
                return memo[state]
            if not state:
                return 0
            val = sys.maxsize
            for w in mapping:
                old_state = dict(state)
                flag = False
                for k in old_state.keys():
                    if k in mapping[w]:
                        old_state[k] -= mapping[w][k]
                        flag = True
                if flag:
                    old_state = {k:v for k, v in old_state.items() if v > 0}
                    val = min(val, dfs(tuple(old_state.items())) + 1)
            memo[state] = val
            return val
        pairs = ct.items()
        return dfs(tuple(pairs))

    def minStickers_DP(self, stickers: List[str], target: str) -> int:
        length = len(target)
        dp = [sys.maxsize] * (1 << length)
        dp[0] = 0
        def find_next_status(state, st):
            nonlocal target, length
            for c in st:
                for i in range(length):
                    if state & (1 << i) or target[i] != c:
                        continue
                    state |= (1 << i)
                    break
            return state

        def get_next_state(cur, sticker):
            counter = collections.Counter(sticker)
            for i in range(length):
                if cur & (1 << i):
                    continue
                if target[i] in counter and counter[target[i]] > 0:
                    cur |= (1 << i)
                    counter[target[i]] -= 1
            return cur

        for state in range(1 << length):
            if dp[state] == sys.maxsize:
                continue
            for st in stickers:
                nxt = find_next_status(state, st)
                if nxt == state:
                    continue
                dp[nxt] = min(dp[nxt], dp[state] + 1)  # here we update the late status.
        return dp[-1] if dp[-1] != sys.maxsize else -1