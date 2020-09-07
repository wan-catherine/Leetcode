class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        mapping = {'&quot;':'"', "&apos;":"'", "&gt;":">", "&lt;":"<", "&frasl;":"/", "&amp;":"&",}
        for key, value in mapping.items():
            text = text.replace(key, value)
        return text