#Call by value
# def modify_value(x):
#     x = x + 10
#     print("Inside function:", x)
# value = 5
# modify_value(value)
# print("Outside function:", value)


#call by reference
def modify_list(my_list):
    my_list.append(4)
    print("Inside function:", my_list)

# original_list = [1, 2, 3]
# modify_list(original_list)
# print("Outside function:", original_list)
originlist = [1,2,3]
modify_list(originlist)
print(modify_list)
print("Outside function",  originlist)