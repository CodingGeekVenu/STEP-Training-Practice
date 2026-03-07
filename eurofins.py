'''
Problem - 2:  Eurofins

Generate all prime numbers from 1 to 10,000 that end with the digit 9

Output:  - Display results in Groups of 100
         - Total number of prime numbers found

Example - 
        Number of prime numbers from 0 to 99 = 5 
        19  29  59  79  89 
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def analyze_primes_ending_in_9():
    total_primes_count = 0
    
    for start in range(0, 10000, 100):
        end = start + 99
        primes_in_range = []
        
        for num in range(start + 9, end + 1, 10):
            if is_prime(num):
                primes_in_range.append(num)
        
        count = len(primes_in_range)
        total_primes_count += count
        
        print(f"Number of prime numbers from {start} to {end} = {count}")
        if count > 0:
            print("  ".join(map(str, primes_in_range)))
            
    print(f"Total prime numbers from 1 to 10000 ending with 9 = {total_primes_count}")

analyze_primes_ending_in_9()