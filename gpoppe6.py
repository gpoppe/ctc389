#Garrett Poppe


students = ["Alfred","Bataman","Catwoman","Dave","Elizabeth"]

print("Current Student List")
for i in students:
    print(i)

print("Menu")
print("option #1: add student to list")
print("option #2: modify student name")
print("option #3: remove student")

choice = int(input("Enter choice: "))

if choice == 1:
    name =  input("enter a name to add: ")
    students.append(name)
    for i in students:
        print(i)

elif choice == 2:
    c = 0
    for i in students:
        c = c + 1
        print(c,i)
    x = int(input("which student do you want to change? "))
    name = input("enter name to change to: ")
    students[x-1] = name
    for i in students:
        print(i)

elif choice == 3:
    c = 0
    for i in students:
        c = c + 1
        print(c,i)
    x = int(input("which student do you want to remove? "))
    students.pop(x-1)
    for i in students:
        print(i)


