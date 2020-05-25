#create class

class Car:
    def __init__(self, name, model, year_build):
        self.Name = name
        self.Model = model
        self.Year_build = year_build

#create method

    def age_of_car(self,current_year):
        return "The car is %d years old." % (current_year-self.Year_build)
        
#override the inbuilt str method
#str method always returns a string
    def __str__(self):
        return "Name of the car is %s, model is %s & year build is %d." % (self.Name,self.Model,self.Year_build)

# create object of car class      
FirstCar = Car("Audi","Q7",2015)
print(FirstCar)
print(FirstCar.age_of_car(2020))

SecondCar = Car("Ford","Mustang",2019)
print(SecondCar)
print(SecondCar.age_of_car(2020))
