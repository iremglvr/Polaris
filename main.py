# Project Polaris
# Day 5
# Founder: İrem

print("Hello, I'm Po!")

name = input("What's your name? ")

if name == "İrem":
    print("Welcome back Founder!")
else:
    print(f"Nice to meet you, {name}!")

age = input(f"How old are you, {name}? ")

print()

print("====== PO ======")
print("1 - Greetings")
print("2 - Tell me my age")
print("3 - Exit")
print()

choice = input("Your choice: ")

if choice == "1":
    if name == "İrem":
        print("Welcome back Founder!")
    else:
        print(f"Nice to meet you again, {name}!")

elif choice == "2":
    print(f"You are {age} years old, {name}.")

elif choice == "3":
    print(f"Goodbye, {name}!")

else:
    print("Invalid choice. Please try again.")