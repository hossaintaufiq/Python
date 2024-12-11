first= input("Enter your 1st number: ")
operator = input("Enter your operator: ")
second = input("Enter your second number: ")


if operator== '+':
    result= int(first) + int(second)

elif operator== '-': 
    result= int(second) - int(first)

elif operator== '*': 
    result= int(first) * int(second)
elif operator== '/':
    result= int(first) / int(second)
elif operator== '%': 
    result= int(first) % int(second)

else: 
    print("Invalid operator")


print(result)    