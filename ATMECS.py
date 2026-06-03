'''
Problem - 4:  ATMECS

Input = Number
Output = List of Special Numbers 

Special number = sum of (digit^(pos of digit)) = number 

Example = 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
'''

def is_special_number(n):
    total_sum = 0
    for index, digit in enumerate(str(n), start=1):
        total_sum += int(digit) ** index
    return total_sum == n

def find_special_numbers(limit):
    special_nums = []
    for num in range(1, limit + 1):
        if is_special_number(num):
            special_nums.append(num)
    return special_nums

def main():
    limit = 10000
    results = find_special_numbers(limit)
    print(f"Special Numbers between 1 and {limit}:")
    print(" ".join(map(str, results)))
    print(f"\nTotal Special Numbers: {len(results)}")

main()