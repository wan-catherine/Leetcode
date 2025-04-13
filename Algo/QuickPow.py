MOD = 10**9+7
def quick_pow(base, exp):
    if exp == 0:
        return 1
    half = quick_pow(base, exp/2) % MOD
    if exp % 2 == 0:
        return half * half % MOD
    else:
        return half * half % MOD * base % MOD

def pow(x, n):
    ans = 1
    while n:
        if n % 2:
            ans = (ans * x) % MOD
        n //= 2
        x = (x * x) % MOD
    return ans