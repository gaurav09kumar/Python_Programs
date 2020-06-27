#normal distribution
import math

mean_ = 10 #mean 
variance_ = 4 #variance
data1 = 13 #normal random variable

#create function
def distribution(m,v,x):
  result =  1 / ((math.sqrt(2*(math.pi)*v))) * (math.exp(-(pow((x-m),2)/(2*v))))
  return result

print( "Probability that a current measurement will exceed 13 mA P(Z>13) is : ", distribution(mean_,variance_,data1))

# to compute P between 9 & 11mA
data2 = 9
data3 = 11

var1 = distribution(mean_,variance_,data2)
var2 = distribution(mean_,variance_,data3)

print("Probability that a current measurement is between 9 and 11mA -> P(9<X<11) is : ", (var1)+(var2))
