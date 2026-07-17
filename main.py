# Project Polaris
# Day 7
# Founder: İrem
version="v0.1.0"

from datetime import datetime

print("Hello, I'm Po!")

#get user information
name = input("What's your name? ")

if name == "İrem":
    print("Welcome back Founder!")
else:
    print(f"Nice to meet you, {name}!")

age = input(f"How old are you, {name}? ")

menu=1
#main menu loop
while menu==1 :
    print()

    print("====== PO ======")
    print("1 - Greetings")
    print("2 - My age")
    print("3 - Today's Date")
    print("4 - About Po")
    print("5 - Exit")
    print()

    choice = input("Your choice: ")

    aboutPo=f"""========== ABOUT PO ==========
Hello!

My name is Polaris.
You can call me Po.

I was born on July 6, 2026.

I am your personal AI assistant.
Version: {version}
=============================="""


    #process user's selection
    if choice == "1":
        if name == "İrem":
            print("How can I help you today?")
        else:
            print(f"Hello again, {name}!")

    elif choice == "2":
        print(f"You are {age} years old, {name}.")

    elif choice == "3":
        today=datetime.now()
        print(f"Today's Date: {today.strftime("%d.%m.%Y")}")

    elif choice == "4":
        print(aboutPo)

    elif choice == "5":
        print(f"Goodbye, {name}!")
        print("Have a great day!")
        menu=0

    else:
        print("Invalid choice. Please try again.")