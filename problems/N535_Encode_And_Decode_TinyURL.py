import random
class Codec:
    def __init__(self):
        self.short_to_long = dict()
        self.long_to_short = dict()
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        res = ""
        while res not in self.short_to_long:
            for i in range(7):
                res += self.chars[random.randint(0,61)]
            self.short_to_long[res] = longUrl
        self.long_to_short[longUrl] = res
        return res

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_to_long[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))