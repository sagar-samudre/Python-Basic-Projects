# Q6: Sets, Tuples, Random and Math
import random
import math
try:
    numbers = set()
    print("Enter 10 Numbers")

    while len(numbers) < 10:
        num = int(input("Enter Number: "))
        numbers.add(num)
    number_tuple = tuple(numbers)
    print("\nUnique Numbers:", number_tuple)

    if len(number_tuple) >= 3:
        print("3 Random Numbers:",
              random.sample(number_tuple, 3))
    total = sum(number_tuple)
    print("Square Root of Sum:",
          math.sqrt(total))

except ValueError:
    print("Invalid Input.")

except Exception as e:
    print("Error:", e)