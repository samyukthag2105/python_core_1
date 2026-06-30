print("progam started")
age = 16
if age >=18:
    print("you can watch the movie")
else:
    print("sorry,you are too young")
print("program finished")

score = 85 

if score >= 90:
    print("grade A")
elif score >= 80:
    print("grade B")
elif score >= 70:
    print("grade C")
else:
    print("grade F")

# ==========================
# FOR LOOP
# ==========================

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

for fruit in fruits:
    print(fruit)

# ===========================
# RANGE
# ===========================
for number in range(5):
    print(number)



# ===========================
# WHILE LOOP
# ===========================

count = 6

while count <= 5:
    print(count)
    count = count + 1

# ===========================
# BREAK
# ===========================
fruits = ["apple","banana","orange","mango","grapes"]

for fruit in fruits:
    print(f"checking{fruit}")

    if fruit == "orange":
        print("found orange")
        break
    # ==========================
# ENUMERATE
# ==============================

students = ["alice","bob","charli","david"]

for index, student in enumerate(students):
    print(index, student)


# ==========================
# FUNCTIONS
# ==========================

def greet():
    print("hello, samyuktha")

greet()
# ==========================
# FUNCTION WITH PARAMETERS
# ==========================

def greet(name):
    print(f"hello, {name}!")

greet("samyuktha")
greet("alice")
greet("bob")

# ==========================
# RETURN
# ==========================

def add(a, b):
    return a + b

result = add(5, 3)
print(result)
answer = add(10, 20)
print(answer) 
# ==========================
# DEFAULT ARGUMENTS
# ==========================

def greet(name="Friend"):
    print(f"Hello, {name}!")

greet()
greet("Samyuktha")
greet("Alice")

# ==========================
# DOCSTRINGS
# ==========================
def add(a, b):
    """returns the sum of teo numbers"""
    return a + b
print(add(5, 7))
print(10 % 2)
print(11 % 2)
# ==========================
# FUNCTION 1 : IS EVEN
# ==========================
def is_even(number):
    """returns true if te number is even""" 
    return number %2 == 0
print(is_even(4))
print(is_even(7))
print(is_even(10))
print(is_even(13))
print(is_even(100))

# =============================
# FUNCTION 2 :MAX OF LIST
# ===============================

def max_of_list(numbers):
    """returns the largest numbers in a list"""

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest
print(max_of_list([12,5,98,45,27]))
print(max_of_list([3,8,2,10,6]))
print(max_of_list([100]))

# ==========================
# FUNCTION 3 : GRADE
# ==========================

def grade(score):
    """Returns the letter grade for a score."""

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
    print(grade(95))
print(grade(82))
print(grade(74))
print(grade(60))
print(grade(100))

def square(number):
    """Returns the square of a number."""
    return number * number

print(square(5))
print(square(10))
print(square(3))
def greet(name="Friend"):
    """Greets a person."""
    return f"Hello, {name}!"

print(greet())
print(greet("Samyuktha"))
print(greet("Alice"))