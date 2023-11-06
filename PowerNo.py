def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage:
base = 10
exponent = 2
result = power(base, exponent)
print(f"{base} to the power of {exponent} is {result}")
