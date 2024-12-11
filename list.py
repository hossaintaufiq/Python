marks=[95,98,97,99,100,85]

print(marks)

# individual elements of the list 

print(marks[2])

# int index value can be negative and that case the counting will start from the end 
print(marks[-1]) # this will print the last element of the list 

# to limit the list we have to use the starting index : and the last index to print the value \

print(marks[0:2]) #this will print the 0 the and 1st index element (95,98)


# print the values with loop 

# for score in marks: 
#     print(score)

i=0 
while i<len(marks): 
    print(marks[i])
    i=i+1


marks.clear()
print(marks)
