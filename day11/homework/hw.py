# 2)
numbers = [30, 20, 16, 98, 43, 87, 96, 10, 13, 90, 120, 86, 99, 68, 69, 14, 45, 18, 19, 89]
total = 0
for number in numbers:
    total += number
    print("Ricxvebis jami", total)

# 3)
names = ["Lasha", "Data", "Gio", "Sandro", "Beqa", "Mari", "Lizi", "Kato", "Irakli", "Fotola", "Iosebi"]

for name in names:
    print("Hello", name, "!")

# 4)
mixed_list = [1, 2, 3, "Lasha", "Data", "Gio", 4, 5, 6, "Sandro", "Beqa", "Mari", 7, 8, 9, "Lizi", "Kato", "Irakli", 10, 11, 12]
reversed_list = ""
i = len(mixed_list) - 1
while i >= 0:
    reversed_list += str(mixed_list[i]) + " "
    i -= 1
print(reversed_list)

# 5)

ages = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39]
for age in ages:
    if age >= 18:
        print("User is an adult!")
    else:
        print("User is not an adult!")
