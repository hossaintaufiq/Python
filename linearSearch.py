def linearSearch(arr, target): 
    for i in range(len(arr)): 
        if arr[i] == target: 
            return i
    return -1

mylist = [1, 2, 3, 4, 5]; 
x=4 

result =linearSearch(mylist,x)

if result!=-1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
