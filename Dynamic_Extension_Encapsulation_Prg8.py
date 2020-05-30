class Dog:
    def __init__(self, name, year_of_birth, breed):
        self._name = name
        self._year_of_birth = year_of_birth
        self._breed = breed

    def __str__(self):
        return "%s is a %s born in %d." % (self._name, self._breed, self._year_of_birth)

DogDetails = Dog("juno", 1954, "golden retriever")


class Student:
    def __init__(self, anagraphic, student_id):
        self._anagraphic = anagraphic
        self._student_id = student_id
    def __str__(self):
        return str(self._anagraphic) + " Student ID: %d" % self._student_id


First_student = Student("john",1)
DogDetails_Student = Student(DogDetails, 2)

print(First_student)
print(DogDetails_Student)
