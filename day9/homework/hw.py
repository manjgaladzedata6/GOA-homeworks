# 2)
user_age = int(input("Please enter your age: "))
if user_age < 0:
    print("Invalid age")
elif user_age >= 18:
    print("Adult")
else:
    print("Minor")

# 3)
number = int(input("Please enter a number: "))
if number > 0 and number % 2 == 0:
    print("Positive Even")
elif number > 0 and number % 2 != 0:
    print("Positive Odd")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# # 4)
correct_username = "data"
correct_password = "1234"
username = input("Please enter your username: ")
password = input("Please enter your password: ")
if username == "data" and password == "1234":     
 print("Login successful!")
elif username != "data" and password == "1234":
 print("Incorrect username or password")

# 5)
my_number = int("45")
users_guess = int(input("Please enter your guess: "))

while users_guess != my_number:

    if users_guess > my_number:
        print("თქვენი რიცხვი მეტია ჩაფიქრებულზე")

    elif users_guess < my_number:
        print("თქვენი რიცხვი ნაკლებია ჩაფიქრებულ რიცხვზე")

    users_guess = int(input("სცადეთ თავიდან: "))

print("თქვენ წარმატებით გამოიცანით რიცხვი!")

# 6)
num = int(input("Please enter a number: "))
for i in range(1, num + 1):
    if i % 2 == 0:
        print(i, "Odd")
    else:
        print(i, "Even")

# 7)
correct_password = "python123"
user_password = input("Please enter your password: ")

while user_password != correct_password:
    print("Wrong, please try again!")
    user_password = input("Please enter your password: ")

print("Access Granted!")

# 8)
start = int(input("შეიყვანეთ საწყისი რიცხვი: "))
end = int(input("შეიყვანეთ საბოლოო რიცხვი: "))

while start <= end:
    if start > 0 and start % 2 == 0:
        print("Positive Even")
    else:
        print(start)

    start += 1

# 9)
user_age = int(input("Please enter your age: "))
user_score = int(input("Please enter your score: "))
if user_age >= 18 and user_score >=70:
    print("You passed!")
elif user_age < 18 and user_score >= 70:
    print("Good result, but you are under 18!")
else:
    print("You failed!")

# 10)
n = int(input("შეიყვანეთ რიცხვი: "))

i = 1

while i <= n:
    if i % 2 == 0 and i % 3 == 0:
        print("Special Number")

    elif i % 2 == 0:
        print("Even")

    elif i % 3 == 0:
        print("Divisible by 3")

    else:
        print(i)

    i += 1    

            


