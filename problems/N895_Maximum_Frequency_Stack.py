import collections

"""
key point : 
    use many stacks to maintain the necessary information . 
    self.freq :
        key : frequency
        val : a list of the number (the latest number natually in the right side, solve the tie frequency issue)
        
    * We don't need to remove the old number when the frequency is changed by pop or push . 
    
"""

class FreqStack(object):

    def __init__(self):
        self.freq = collections.defaultdict(list)
        self.mapping = {}
        self.max = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x not in self.mapping:
            self.mapping[x] = 1
        else:
            self.mapping[x] += 1
        self.freq[self.mapping[x]].append(x)
        self.max = max(self.max, self.mapping[x])

    def pop(self):
        """
        :rtype: int
        """
        val = self.freq[self.max].pop()
        self.mapping[val] -= 1
        if not self.freq[self.max]:
            self.max -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()