# Q4: Student Class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []
    def add_mark(self, mark):
        try:
            mark = float(mark)
            if 0 <= mark <= 100:
                self.marks_list.append(mark)
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid marks entered.")
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)
    def display_info(self):
        print("\nStudent Information")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks_list)
        print("Average :", self.get_average())
name = input("Enter Name: ")
roll = input("Enter Roll No: ")
student = Student(name, roll)
for i in range(5):
    mark = input(f"Enter Mark {i+1}: ")
    student.add_mark(mark)
student.display_info()