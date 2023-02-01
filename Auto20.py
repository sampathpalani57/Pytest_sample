class Employee():
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def emp_detail(self):
        print("this is eployee name:", self.name)
        print("this is employee rollno:", self.rollno)

    def set_salary(self, salary, personal):
        self._salary = salary
        self.__personal = personal
    def get_salary(self):
        return self._salary
    def _protected(self):
        print("this is protected method:")
        print("this is health issue:", self.__personal)

samp = Employee('sampath', 121)
print(samp.emp_detail())
print(samp.set_salary(10000, 'sugar'))
samp._protected()