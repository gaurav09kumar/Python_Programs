#inheritance
#Parent class

class Person:
    def __init__(a, name, surname, year_of_birth):
        a.name = name
        a.surname = surname
        a.year_of_birth = year_of_birth

        
#child class  
# *args means we are calling all the variables from parent class
class Student(Person):
    def __init__(self, student_id, *args):
        super(Student,self).__init__(*args)
        self._student_id = student_id

#create object of child class        
john = Student(1,'John','Smith',2006)

print(john._student_id)
print(john.year_of_birth)
print(john.surname)
print(type(john))
print(isinstance(john,Person))
print(isinstance(john,object))
