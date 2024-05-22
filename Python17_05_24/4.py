class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name=name
        self.age=age
        self.salary=salary

    def display_info(self):
        print(f"Details of Employee\nName of employee {self.name}\nAge of employee {self.age}\nSalary  of employee {self.salary}")


e=Employee("Paras", 20, 6000)
e.display_info()