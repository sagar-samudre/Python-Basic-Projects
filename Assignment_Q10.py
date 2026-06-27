# Q10: Smart Calculator & Data Manager
import math
import random
history = {}
while True:
    print("\n===== MENU =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Number")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")
    choice = input("Enter Choice: ")

    if choice == "1":
        try:
            a = float(input("First Number: "))
            b = float(input("Second Number: "))
            print("Addition:", a + b)
            print("Subtraction:", a - b)
            print("Multiplication:", a * b)
            print("Division:", a / b)
            result = a + b
        except ZeroDivisionError:
            print("Division by zero not allowed.")

        except ValueError:
            print("Invalid Input.")

    elif choice == "2":
        try:
            n = float(input("Enter Number: "))
            result = math.sqrt(n)
            print("Square Root:", result)

        except ValueError:
            print("Invalid Number.")

    elif choice == "3":
        result = random.randint(1, 100)
        print("Random Number:", result)

    elif choice == "4":
        time = input("Enter Timestamp: ")
        history[time] = result
        print("Result Stored.")

    elif choice == "5":
        if len(history) == 0:
            print("No History Available.")
        else:
            for key, value in history.items():
                print(key, ":", value)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")