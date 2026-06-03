import sys

def build_sieve(n):
    sieve = [1] * (n + 1)
    sieve[0] = 0
    sieve[1] = 0

    for i in range(2, n +1) :
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = 0
    return sieve

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
            a, b = b, a % b
    return a

data = list(map(int, sys.stdin.read().split()))
a, b, m = data[0], data[1], data[2]

sieve = build_sieve(a)

is_prime = False




g = gcd(a, b)
lcm = (a * b ) / g
prime_count = sum(sieve)

mul_mod = (a * b) % m
add_mod = (a + b) % m

print("Is Prime =", str(is_prime).lower())
print("GCD =", g)
print("LCM =", lcm)
print("Primes up to a =", prime_count)
print("(a * b) mod m =", mul_mod)
print("(a + b) mod m =", add_mod)