# Q7: Lambda Function
try:
    square = lambda x: x * x

    numbers = range(1, 21)

    squares = list(map(square, numbers))

    print("Squares:")
    print(squares)

    print("\nEven Squares:")

    for i in squares:
        if i % 2 == 0:
            print(i)

except Exception as e:
    print("Error:", e)