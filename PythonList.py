#PythonList.py

#List

#Creating list:
data = [10,20,30,"Hello"]
data2 = [10,20]

print(data)

#Length of list:
print("Lenght of list is : ",len(data))

print(data[0])

print(data[1:])

print(data[:2])

print(data[0:2])

data.append("Bye")

print(data)
print(data2*2)
print(data2)

print("Updated lenght of list is : ",len(data))

print("For Loop : ")
for i in data:
    print(i)

print("For loop2 : ")
for i in range(len(data)):
    print(data[i])
        
