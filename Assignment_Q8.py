# Q8: Employee Class
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)

    def show_details(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])

employees = {}
employees[101] = Employee(101, "Sagar", "HR", 80000)
employees[102] = Employee(102, "Kapil", "IT", 45000)
employees[103] = Employee(103, "Prem", "Sales", 40000)

for emp in employees.values():
    emp.show_details()