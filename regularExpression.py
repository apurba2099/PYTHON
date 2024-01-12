import re
def validate_email(email):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(email_pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

# Test the function with the given email address
validate_email("apurbadutta2099@gmail.com")


a = "hello my name is apurba dutta, i am from india" 
word = re.search(r'apurba', a)
print("Indexing start: ", word.start())
print("indexing end: ",word.end())


def SumOfNumbers(numbers):
    evennum = 0
    for num in numbers:
        if num % 2 == 0:
            evennum += num
    return evennum
listNumber = [1,2,3,4,5,6,7,8,9,10]
results=SumOfNumbers(listNumber)
print(f"Sum of all even number:{results}")