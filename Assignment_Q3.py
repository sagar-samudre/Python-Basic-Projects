# Q3: manage Marks
def manage_marks():
    marks = []

    print("Enter marks of 5 subjects")

    while len(marks) < 5:
        try:
            mark = float(input(f"Subject {len(marks)+1}: "))
            marks.append(mark)

        except ValueError:
            print("Invalid input! Please enter numeric marks.")

    average = sum(marks) / len(marks)
    print("\nAverage Marks:", average)
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))
    marks.sort(reverse=True)
    print("Marks in Descending Order:", marks)
manage_marks()