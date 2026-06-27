# Q2: Analyze String
def analyze_string(s):
    if s == "":
        print("String is empty.")
        return

    print("Length:", len(s))
    print("Reverse:", s[::-1])
    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)
    print("\nCharacter\tPositive Index\tNegative Index")

    for i in range(len(s)):
        print(f"{s[i]}\t\t{i}\t\t{i-len(s)}")

string = input("Enter a string: ")
analyze_string(string)