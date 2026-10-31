# 2)
n = int(input("Please enter your number: "))

i = 1

while i <= n:
    print(i)
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")
    i += 1

# 3)
n = int(input("Please enter your number: "))

i = 0

while i <= n:
    if i % 5 == 0:
     print("Divisible by 5")
    else:
       print(i)
    i += 1
        
# 4)
correct_password = "python123"

password = input("Please enter your password: ")


while password != correct_password:
    if password == correct_password:
        print("Access Granted!")
    else:
        print("Wrong password!")
        password = input("try again: ")

print("Access Granted!")

# 5)
n = int(input("Please enter your number: "))

i = 1
for i in range(1, n + 1):
    if i % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
        
i += 1

# 6)
n = int(input("Please enter your number: "))
i = 1
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)
    else:
        print("Not divisible by 3")
        