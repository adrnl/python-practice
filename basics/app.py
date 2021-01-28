# Imports
from math import *  # includes sqrt, floor, ciel, etc

# Hello World
print("Hello World")

# Triangle
print("\n Triangle")
print("   /|")
print("  /_|")
print(" /__|")
print("/___|")

# Vars v1
# print("There once was a man named George, ")
# print("he was 70 years old. ")
# print("He really liked the name George, ")
# print("but didn't like being 70.")

# Vars v2, variable name/age
print("\n Story")
char_name = "Adrian"
char_age = "25"

print("There once was a man named " + char_name + ", ")
print("he was " + char_age + " years old. ")
print("He really liked the name " + char_name + ", ")
print("but didn't like being " + char_age + ".")

# Strings
print("\n String Practice")
phrase = "I'm learning\n:)"
print(phrase + " right?")

# String Functions
print("\n String Functions")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase.index("\n"))
print(phrase.replace("learning", "smarter!"))

# Character Fetching
print("\n Character Fetch")
print(phrase[0])
print(phrase[10])

# Numbers
num = 5
neg_num = -5
print("\n Numbers")
print(2)
print(2.09163)
print(-123412)
print(3-2.4)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3)
print(num)
print(str(num) + " is five")
print(neg_num)
print("abs(neg_num) is " + str(abs(neg_num)))
print(pow(5, 2))
print(max(5, 2))
print(min(5, 2))
print(round(3.2823))

# Imported functions
print(sqrt(36))

# Lists
print("\n Lists")

friends = ["Cooper", "Kei", "Joel", "Jonny", "Zack"]
names = friends.copy()
numbers = [1, 2, 3, 4, 5]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[2:])
print(friends[1:3])
friends[1] = "Larissa"
print(friends)

# List Functions
friends.extend(numbers)
print(friends)
friends.append("Pete")
print(friends)
friends.remove("Zack")
print(friends)
friends.pop()
print(friends)
print(friends.index("Joel"))
print(names)
names.sort()
print(names)

# Tuples (IMMUTABLE!!!)
print("\n Tuples")

tuple = (4, 5)
tuple_list = [tuple, (6,9), (4, 20)]

print(tuple)
print(tuple_list)

# Functions
print("\n Functions")

def sayHi():
    print("Hi!")

sayHi()

def sayHi2(name):
    print("Hi " + name + "!")

sayHi2("Adrian")

# Returns
def cube(num):
    return pow(num, 3)

result = cube(3)
print(result)

# If Statements
print("\n If Statements")

# gender = input("Enter your gender: ")
# gender = gender.lower()
male = True
tall = False

if male and tall:
    print("You're a big guy.")
elif male or tall:
    print("You're a person.")
else:
    print("You're a small gal.")

def tester():
    word = input("say \"cheese\", or else: ")

    if word != "cheese":
        tester()
    else:
        print("you may live...")

# Dictionaries
print("\n Dictionaries")

monthAbbrs = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

monthNums = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(monthAbbrs["Nov"])
print(monthAbbrs.get("Aug"))
print(monthAbbrs.get("Luv", "Not a valid key"))
print(monthNums[12])
print(monthNums.get(69, "N/A"))

# Loops
print("\n Loops")

def looper():
    i = 1
    while i <= 10:
        print(i)
        i += 1

    print("Done")

looper()
