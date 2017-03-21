__author__ = "amber buckley"

# description: write an object oriented program to determine pay raise amounts depending on employee type.
# using a class called Employee and creating other employee types, inheriting from Employee

# class Employee
#   declare real raise amount
#   private string first name
#   private string last name
#   private real pay
#   private string email
# end class


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

# function string fullname()
#    return first name, last name

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# function apply raise
#   return pay raise

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# class Developer
#   set raise amount

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

# class Manager
#   
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('hannah', 'buckley', 56000, 'Python')
dev_2 = Developer('first name', 'last name', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)
print(mgr_1.print_emps())
#mgr_1.print_emps()
#mgr_1.add_employee(dev_2)
#mgr_1.print_emps()

#print(dev_1.email)
#print(dev_2.prog_lang)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)