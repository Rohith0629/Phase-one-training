# venn diagrams
# union and intersection
s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)
print(s2.intersection(s1))


# Conditional Statements
# if, elif, else

# Sample code for "if"
if 7 > 5:
    print("True")
else:
    print("False")


# Code For Even or Odd

a = 20

if a % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")

# Prime Number Checking

b = 9
b = b//10
if b % 2 == 0:
    print("Its a Prime number")
else:
    print("Its Not  Prime Number")


# Elif statements

# Syntax for elif

''' if condition 1:
 code 1
 elif condition 2:
 code 2
 elif condition 3:
 code 3
 else:
 code 4 '''

# Sample code for elif
day = int(input("Enter a Number between one and seven:   "))
if day == 1:
    print("It is Monday")
elif day == 2:
    print("It is Tuesday")
elif day == 3:
    print("It is Wednesday")
elif day == 4:
    print("It is Thursday")
elif day == 5:
    print("It is Friday")
elif day == 6:
    print("It is Saturday")
elif day == 7:
    print("It is Sunday")
else:
    print("Enter a valid number")

# Again Run The Code For Entering New Number

'''if 0-20 and its even print weird if not print normal number
   if >30 and its even print normal if not print weird number'''

check = int(input("Enter a number that needed to be checked:   "))
if check > 0 and check < 20:
    if check % 2 == 0:
        print("Weird number")
    else:
        print("Normal Number")
elif check >= 20 and check < 30:
    print("Normal Number")
else:
    if check >= 30 and check % 2 == 0:

        print("It is normal")
    else:
        print("Weird Number")













