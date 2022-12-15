class Employee():
    def __init__(self):
        self.id = None
        self._id = 1
        self.__id = 2

e = Employee()
print(dir(e))