#dictionary
my_dictionary = {
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}

print("Name:", my_dictionary["name"])
print("Age:", my_dictionary["age"])
print("City:", my_dictionary["city"])

#list 
numbers = [1, 2, 3, 4, 5]

# Print the list
print(numbers)

#tuple
# Create a tuple of fruits
fruits = ("apple", "banana", "orange")
print(fruits)

# Create a set of colors
colors = {"red", "green", "blue"}
print(colors)

#set another

# Create a set of numbers
numbers = {1, 2, 3, 4, 5}
numbers.add(4)
numbers.remove(3)
if 4 in numbers:
  print("4 is in the set")
else:
  print("no 4 number")
print(numbers)

