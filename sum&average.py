# a = [10,20,30,40,50]
# b =0
# for f in a:
#     b+=f
# print(f"Array of numbers {a}")
# print(f"Sum of numbers {b}")
# result = b/len(a)
# print(f"Here the average {result}%")

# print("----------------------")

# # Example array of numbers
# numbers_array = [10, 20, 30, 40, 50]
# # Calculate the sum of numbers
# total_sum = sum(numbers_array)
# # Calculate the average
# average = total_sum / len(numbers_array) if len(numbers_array) > 0 else 0
# # Print the results
# print(f"Array of Numbers: {numbers_array}")
# print(f"Sum of Numbers: {total_sum}")
# print(f"Average of Numbers: {average:.2f}")




myDictionary = {'Name': 'Apurba','LastName': 'Dutta', 'Class': 'CST', 'CollegeName' : 'JIS college of engineering'}
print(f"Before del use {myDictionary}")
del myDictionary['Class']
print(f"After del use {myDictionary}")