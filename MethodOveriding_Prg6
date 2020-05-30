# create a class
# define a body
# init is a predefined method we are overriding it
# self is not a keyword, self is automatically passed & refers to the object itself

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
        return "Name of the car is %s, model is %s & year build is %d " % (self.Name,self.Model,self.Year_build)
        

#child class        
class ChildCar(Car):
    def __init__(self, mileage, *args):
        super(ChildCar,self).__init__(*args)
        self._mileage = mileage
        
#override the str method of parent class
    def __str__(self):
        return super(ChildCar,self).__str__() + "which has %d km per Litre mileage" % (self._mileage)


#create object of ChildCar Class & pass the argumments
FirstCar = ChildCar(23, "Audi", "Q3", 2019)
print(FirstCar)
