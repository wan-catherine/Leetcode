"""
^ : adding without carry
& : get the carry for example : 01&01 = 01, then move 1 bit to left, then we get carry : 10.

sum(a,b)
we need to stop when there is no carry (b == 0)
"""

def get_sum(a, b):
    while b:
        temp = a ^ b
        b = (a & b) << 1
        a = temp
        print(f"a={a} {bin(a)}")
        print(f"b={b} {bin(b)}")
    return a

if __name__ == '__main__':
    a = get_sum(12, 7)