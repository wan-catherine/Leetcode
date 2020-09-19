class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        length = len(clips)
        clips.sort(key=lambda li: (li[0], -li[1]))
        if clips[0][0] != 0:
            return -1
        right = clips[0][1]
        if right >= T:
            return 1
        index = 0
        ans = 1
        while index < length:
            next_right = right
            while index < length and clips[index][0] <= right:
                next_right = max(next_right, clips[index][1])
                index += 1
            if next_right == right:
                return -1
            ans += 1
            if next_right >= T:
                return ans
            right = next_right
        return -1

