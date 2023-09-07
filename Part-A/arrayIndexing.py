num=5
array=[]
print("Enter 5 array elements:")
for i in range(num):
    a=int(input())
    array.append(a)
print("Array entered is: ",array)
for i in range(num):
    print(f"Element at index {i} : {array[i]}")
index=int(input("Enter index:"))
print(f"Element at index {index} is {array[index]}")
