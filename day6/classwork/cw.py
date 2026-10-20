#მოიყვანეთ ლოგიკური ოპერატორების გამოყენების მაგალითები (and, or, not), and ოპერატორზე და or ოპერატორზე უნდა მოიყვანოთ 4-4 მაგალითი (4 შესაძლო ვარიანტი როგორც შეიძლება დასრულდეს პირობა) და not ოპერატორზე სულ 2 მაგალითი.
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

print(not True)         # False
print(not False)        # True

#print(false or true)

print(True and not 5 < 6 or (90 > 81) and not 76 == 83)
#(false or true)
# შესაბამისად ეს იქნება "true"

print(10 >= 10 and 9 < 81 or not True and not 90 >= 90)
#(true or false)
# ეს იქნება true
