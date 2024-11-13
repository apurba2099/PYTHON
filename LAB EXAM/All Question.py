# 1. Find maximum of three numbers in python using defined function.
def find_max(a, b, c):
    return max(a, b, c)
num1 = 10
num2 = 20
num3 = 15
print("Maximum of three numbers:", find_max(num1, num2, num3))


# 2. Find the length of the list and simply swap first element with (n-1)th element.
def swap_first_last(lst):
    length = len(lst)
    if length >= 2:
        lst[0], lst[length - 1] = lst[length - 1], lst[0]
    return lst
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
print("After swapping first and last elements:", swap_first_last(my_list))


# 3. WAP to find reverse words in a given string in python.
def reverse(a):
    b=a[::-1].lower()
    return b
c = input("Enter a string: ")
d= reverse(c)
print(f"Before swap the string {c}\nAfter swap the string {d}")


# 4. WAP to find row-wise element addition in tuple matrix.
def row_sum(matrix):
    row_sums = [sum(row) for row in matrix]
    return row_sums
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Matrix:", matrix)
print("Row-wise sums:", row_sum(matrix))


# 5. WAP to find factors of a number.
def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
number = 12
print("Factors of", number, ":", find_factors(number))


# 6. Define a python function which performs addition of two fractions.
from fractions import Fraction

def add_fractions(fraction1, fraction2):
    return fraction1 + fraction2
frac1 = Fraction(1, 2)
frac2 = Fraction(1, 3)
print("Sum of fractions:", add_fractions(frac1, frac2))


# 7. WAP to sort python dictionary by key in python.
def sort_dict_by_key(dictionary):
    return dict(sorted(dictionary.items()))
my_dict = {'b': 2, 'a': 1, 'c': 3}
print("Original Dictionary:", my_dict)
print("Sorted Dictionary by Key:", sort_dict_by_key(my_dict))

