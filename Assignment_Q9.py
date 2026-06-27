# Q9: Unique Words
import math
try:
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    print("\nUnique Words:")

    for word in sorted_words:
        print(word)

    print("\nTotal Unique Words^2:",
          math.pow(len(unique_words), 2))

except Exception as e:
    print("Error:", e)