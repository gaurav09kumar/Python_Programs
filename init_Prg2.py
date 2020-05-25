# create a class
# define a body
# init is a predefined method we are overriding it
# self is not a keyword, self is automatically passed & refers to the object itself

class Car:
    def __init__(self, name, model, year_build):
        self.Name = name
        self.Model = model
        self.Year_build = year_build

# create object of car class & pass required arguments     
FirstCar = Car("Audi","Q7",2015)
SecondCar = Car("Ford","Mustang",2019)

print(FirstCar.Name,FirstCar.Model,FirstCar.Year_build)

print(SecondCar.Name,SecondCar.Model,SecondCar.Year_build)

""" 
This is a good programming practice 
where common properties are defined at first
"""
