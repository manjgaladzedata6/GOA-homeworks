# 1)
#მომხმარებელს შემოვაყვანინოთ ინფორმაცია დ აგავარკვიოთ შეუძლია თუ არა მას კინოში შესვლა
age = int(input("Please enter your age: "))
has_ticket = str(input("Do you have the ticket: "))
print(age >= 12 and has_ticket == "yes")

# 2) 
num1 = int(input("Please enter your number: "))
num2 = int(input("Please enter your second number: "))
print(num1 == 100 or num2 == 100)

# 3)
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
is_student = input("Are you a student: ")
print(age >= 18 and is_student == "yes")

# 4)

is_sunny = True
is_warm = False

print(is_sunny and not is_warm)
