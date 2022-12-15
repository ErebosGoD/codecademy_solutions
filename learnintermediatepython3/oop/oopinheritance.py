class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self): #method overriding
    super().say_id() #accessing the parent class's method
    print("I am an Admin")

class Manager(Admin): #multiple inheritance
  def say_id(self):
    print("I am in charge!")
    super().say_id()


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()