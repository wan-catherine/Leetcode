import collections


class Solution(object):
    """
    The input size is < 300, so we can use three loops
    Use prefix_xor
    arr[i]^...arr[j] = (arr[0]^...arr[i-1]) ^ ((arr[0]^...arr[i-1])^arr[i]^...^arr[j])
    x^x = 0
    0^x = x

    define: prefix_xor[i] = arr[0]^...arr[i-1]

    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] = prefix_xor[i] ^ prefix_xor[j]
    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = prefix_xor[j] ^ prefix_xor[k+1]
    """
    def countTriplets_triple(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        length = len(arr)
        prefix_xor = [0] * (length + 1)  # 0^x=x
        for i in range(length):
            prefix_xor[i+1] = arr[i] ^ prefix_xor[i]
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j, length):
                    a = prefix_xor[i]^prefix_xor[j]
                    b = prefix_xor[j]^prefix_xor[k+1]
                    if a == b:
                        res += 1
        return res

    """
    same idea for prefix_xor
    
    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
    a == b -> a^b = 0 ->
    arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0
    arr[0]^...arr[i-1] ^ a ^ b = arr[0]^...arr[i-1] ^ 0 = arr[0]^...arr[i-1]
    
    so we can find i and k which arr[0]^...arr[i-1]^...arr[k] == arr[0]^...arr[i-1] ->
    prefix_xor[i] == prefix_xor[k+1]
    
    After we get i and k , then j can be any one of between (i, k] ****
    a^b^c = (a^b)^c = a^(b^c) ->
    arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0
    so we can choice j in (i,k] : add '()' in any of the position which in (i,k] :
    (arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]) ^ (arr[j] ^ arr[j + 1] ^ ... ^ arr[k]) = 0
    -> a == b
    """
    def countTriplets_double(self, arr):
        res = 0
        length = len(arr)
        prefix_xor = [0] * (length + 1)
        for i in range(length):
            prefix_xor[i + 1] = arr[i] ^ prefix_xor[i]

        for i in range(length):
            for k in range(i+1,length):
                if prefix_xor[i] == prefix_xor[k+1]:
                    res += k - i
        return res

    """
    YouToBe : https://www.youtube.com/watch?v=30A0Z2KDvaA
    
    x[n] = x[i] = x[j] = x[k] =>
    res = (j - i - 1) +
          (k - i - 1) + (k - j - 1) + 
          (n - i - 1) + (n - j - 1) + (n - k - 1)
    """
    def countTriplets(self, arr):
        res = 0
        length = len(arr)
        freq = collections.defaultdict(int)
        freq[0] = 1
        sum = collections.defaultdict(int)
        x = 0
        for i in range(length):
            x ^= arr[i]
            res += freq[x] * i - sum[x]
            freq[x] += 1
            sum[x] += i + 1
        return res