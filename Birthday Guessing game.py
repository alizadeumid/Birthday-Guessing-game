m = 0
i = 0
set1 = 1
set2 = 2
set3 = 4
set4 = 8
set5 = 16
input("Welcome to the Birthday Guessing Game!")
print("Is your number in this list?: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]")
i =int(input("Enter 0 for No and 1 for Yes: "))
if i == 1:
    m += set1
print("Is your number in this list?: [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]")
i =int(input("Enter 0 for No and 1 for Yes: "))
if i == 1:
    m += set2
print("Is your number in this list?: [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]")
i =int(input("Enter 0 for No and 1 for Yes: "))
if i == 1:
    m += set3
print("Is your number in this list?: [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]")
i =int(input("Enter 0 for No and 1 for Yes: "))
if i == 1:
    m += set4
print("Is your number in this list?: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]")
i =int(input("Enter 0 for No and 1 for Yes: "))
if i == 1:
    m += set5
print(f"Your number is: {m}")

    