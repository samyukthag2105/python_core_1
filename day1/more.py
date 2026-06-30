# ==========================
# LISTS
# ==========================
numbers = []
for i in range(1, 6):
    numbers.append(i)

print(numbers)

# ==========================
# DICTIONARY COMPREHENSION
# ==========================
squares = {i: i * i for i in range(1, 6)}
print(squares)
# ==========================
# TRY AND EXCEPT
# ==========================
try:
    number = int(input("enter a number: "))
    print(f"you entered {number}")

except ValueError:
    print("that is not a valid number !")


# ==========================
# WRITING TO A FILE
# ==========================
with open("day1/output.txt", "w") as files:
    files.write("hello from python!\n")
    files.write("this file was created by samyuktha.\n")
print("file written successfully!")







# ==========================
# WORD FREQUENCY COUNTER
# ==========================
try:
    with open("day1/sample.txt", "r") as file:
         text = file.read().lower()
         
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print(frequency)
except FileNotFoundError:
    print("the file does not exist,")
finally:
    print("program finished")