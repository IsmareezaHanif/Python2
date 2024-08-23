# Define a function called greet_user that:
# Takes one argument, name.
# Prints a greeting message that includes the name.

def greet(name):
    print(f"{name}! Welcome to Python!")

greet("Fariezz")

# Modify the greet_user function:
# Add a second optional argument, greeting, with a default value of "Hello".
# The function should print the greeting followed by the name.

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("Fariezz", "Lockman")

# Create a function sum_numbers that:
# Takes two arguments, a and b.
# Returns the sum of a and b.

def sum(x, y):
    return x + y

result = sum(5, 5)
print(result)

# Work with the following list: fruits = ["apple", "banana", "cherry", "date"].
# Add "elderberry" to the end of the list.
# Remove "banana" from the list.
# Insert "blueberry" at the second position in the list.
# Sort the list in alphabetical order.

fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.remove("banana")
fruits.insert(1, "blueberry")
fruits.sort()
print(fruits)

# Write a loop that:
# Prints numbers from 1 to 10.
# Stops the loop if the number is 7 (use the break statement).

count = 0

while True:
    count += 1
    print("Current count:", count)
    
    if count == 7:
        print("Breaking the loop at count 7")
        break

# Write a loop that:
# Prints numbers from 1 to 10.
# Skips the numbers that are multiples of 3 (use the continue statement).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for num in numbers:
    
    if num % 3 == 0:
        print(f"Skipping the multiple of 3: {num}")
        continue
    
    print(f"Number without multiple of 3: {num}")













