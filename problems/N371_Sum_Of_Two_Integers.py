"""
Two's Complement binary for Negative Integers:

Negative numbers are written with a leading one instead of a leading zero.
So if you are using only 8 bits for your twos-complement numbers,
then you treat patterns from "00000000" to "01111111" as the whole numbers from 0 to 127,
and reserve "1xxxxxxx" for writing negative numbers.
A negative number, -x, is written using the bit pattern for (x-1) with all of the bits complemented (switched from 1 to 0 or 0 to 1).
So -1 is complement(1 - 1) = complement(0) = "11111111",
and -10 is complement(10 - 1) = complement(9) = complement("00001001") = "11110110".
This means that negative numbers go all the way down to -128 ("10000000").

Of course, Python doesn't use 8-bit numbers.
It USED to use however many bits were native to your machine, but since that was non-portable,
it has recently switched to using an INFINITE number of bits.
Thus the number -5 is treated by bitwise operators as if it were written "...1111111111111111111011".

x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,
and it's the complement of the bit in x if that bit in y is 1.

"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        if b == 0:
            return a

        mask = 2**32 - 1

        while b != 0:
            c = a & b
            a = (a ^ b) & mask
            b = (c << 1) & mask
        # if a > mask, it means for 32bit number , a should be negative, but python use more than 32 bits, so the 33rd bit is still zero
        # so python see a is a positive number > mask.
        # What we do here is now shift all bits which larger than 32nd bit(33,34,...) python uses into 'one', so python can know it's a negative number.
        # so we first XOR with mask, then shift all bits.
        """
        a :       000000 1101100
        a^mask :  000000 0010011
        ~(a^mask):111111 1101100  at this time all bits (33, 34...) are 'one', so python will know this is a negative number . 
        
        We use ~(a^mask) to keep the number's bits same as before , but just shift the sign bit . 
        """
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a

    def getSum_(self, a, b):
        mask = 0xffffffff
        while b & mask:
            a, b = a ^ b, (a & b) << 1
        return a & mask if b > mask else a