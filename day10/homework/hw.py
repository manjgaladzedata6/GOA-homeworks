# 3)
positive = 0
negative = 0
zero = 0
even = 0
odd = 0

for i in range(10):
    number = int(input("Enter a number: "))

    if number > 0:
        print("Positive")
        positive += 1
    elif number < 0:
        print("Negative")
        negative += 1
    else:
        print("Zero")
        zero += 1

    if number % 2 == 0:
        print("Even")
        even += 1
    else:
        print("Odd")
        odd += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
print("Even numbers:", even)
print("Odd numbers:", odd)

# 2)
n = int(input("Enter the number of products: "))

total = 0

for i in range(n):
    price = float(input("Enter product price: "))
    total += price

if total > 200:
    total = total - total * 0.15
elif total >= 100:
    total = total - total * 0.10

print("Total amount to pay:", total, "GEL")

# 3)
secret_number = 42
attempts = 0

guess = int(input("Guess the number: "))

while guess != secret_number:
    attempts += 1

    if guess > secret_number:
        print("The number is too high!")
    else:
        print("The number is too low!")

    guess = int(input("Try again: "))

attempts += 1

print("Congratulations! You guessed the number!")
print("Number of attempts:", attempts)

# 4)
for i in range(5):
    name = input("Enter student name: ")
    grade = int(input("Enter student grade: "))

    if grade >= 90:
        result = "Excellent"
    elif grade >= 70:
        result = "Good"
    elif grade >= 50:
        result = "Satisfactory"
    else:
        result = "Failed"

    print(name, "", result)

# 5)
total = 0
count = 0
positive = 0

number = int(input("Enter a number: "))

while number != 0:
    total += number
    count += 1

    if number > 0:
        print("Positive")
        positive += 1
    else:
        print("Negative")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

    number = int(input("Enter a number: "))

print("Sum:", total)
print("Number of numbers:", count)
print("Positive numbers:", positive)