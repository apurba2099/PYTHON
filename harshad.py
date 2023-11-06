def is_harshad_number(n):
    sum_of_digits = sum(int(digit) for digit in str(n))
    return n % sum_of_digits == 0

# Example usage:
n = int(input("Enter a number: "))
if is_harshad_number(n):
    print(f"{n} is a Harshad number.")
else:
    print(f"{n} is not a Harshad number.")
