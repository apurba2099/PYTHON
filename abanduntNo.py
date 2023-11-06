def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def is_abundant_number(n):
    return sum_of_divisors(n) > n

# Example usage:
n = 12  # You can change this number
if is_abundant_number(n):
    print(f"{n} is an abundant number.")
else:
    print(f"{n} is not an abundant number.")
