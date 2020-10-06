class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        mask1, mask2, mask3, mask4, mask = 0, 224, 240, 248, 128
        i, length = 0, len(data)
        while i < length:
            if data[i] & mask4 == mask3:
                if i + 3 >= length or data[i+1] & mask != 128 or data[i+2] & mask != 128 or data[i+3] & mask != 128:
                    return False
                i += 4
                continue
            if data[i] & mask3 == mask2:
                if i + 2 >= length or data[i+1] & mask != 128 or data[i+2] & mask != 128:
                    return False
                i += 3
                continue
            if data[i] & mask2 == 192:
                if i + 1 >= length or data[i+1] & mask != 128:
                    return False
                i += 2
                continue
            if data[i] & mask == 0:
                i += 1
                continue
            return False
        return True