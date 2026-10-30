# # 1)
i = 0
while i < 20:
     print("data")
     i += 1

# # 2)
i = 0
while i <= 100:
     print(i)
     i += 2


# 3)

correct_password = "data123"

password = input("Please enter your password: ")
while password != correct_password:
    password = input("The password you entered is false")
    

if password == correct_password:
    password = input("Acces granted!")

