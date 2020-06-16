class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if not IP:
            return "Neither"

        if '.' in IP:
            return self.isIPv4(IP)

        if ':' in IP:
            return self.isIPv6(IP)

        return "Neither"

    def isIPv4(self, ip):
        ranges = ip.split('.')
        if len(ranges) != 4:
            return "Neither"
        for range in ranges:
            try:
                num = int(range)
            except ValueError :
                return "Neither"
            if num < 0 or num > 255:
                return "Neither"
            if len(str(num)) != len(range):
                return "Neither"
        return "IPv4"

    def isIPv6(self, ip):
        letters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
        ranges = ip.split(':')
        if len(ranges) != 8:
            return "Neither"
        for range in ranges:
            if len(range) < 1 or len(range) > 4:
                return "Neither"
            for letter in range:
                if letter not in letters:
                    return "Neither"
        return "IPv6"


