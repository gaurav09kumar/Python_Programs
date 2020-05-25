#create a class
#when we dont want to define a body of a function or class we can use pass keyword

class Car:
    pass

#create a object of Car class & name it as FirstCar
FirstCar = Car()

#define properties
FirstCar.name = "Audi"
FirstCar.model = "A6"
FirstCar.build_year = 2017

#this will give the address of the FirstCar object
print(FirstCar)

print("My first car is %s %s and it's build year is %d." %
        (FirstCar.name,FirstCar.model,FirstCar.build_year))


#create a second object of Car class & name it as SecondCar
SecondCar = Car()

#define properties
SecondCar.name = "Mercedez Benz"
SecondCar.model = "C class"
SecondCar.build_year = 2020

#this will give the address of the SecondCar object
print(SecondCar)

print("My second car is %s %s and it's build year is %d." %
        (SecondCar.name,SecondCar.model,SecondCar.build_year))
        

"""

This is a bad practice of programming as when ever you want to create
a new object we need to define properties such as name, model etc everytime.
There is no proper skeleton of class in this program.

"""
