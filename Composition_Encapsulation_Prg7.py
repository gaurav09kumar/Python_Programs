class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
        
    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) + 
               "\n \tOptimal pressure: " + str(self.opt_pressure))
        
class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
        
    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))
        
class Body:
    def __init__(self, size):
        self.size = size
        
    def __str__(self):
        return "Body:\n \tSize: " + self.size

#create class        
class Car:
    def __init__(self, tyres, engine, body):
        self.tyres = tyres
        self.engine = engine
        self.body = body
        
    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body)

#create objects pf Tyres, Engine & Body classes  
t = Tyres('MRF', True, 2.0)
e = Engine('Petrol', 3)
b = Body('Medium')

#create object & pass the previous objects as args to Car class
c = Car(t, e, b)
print(c)
