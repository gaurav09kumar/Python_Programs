#multiple inheritance

class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def test(self):
        print("This is class A statement")
        
class B:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def test(self):
        print("This is class B statement")
        
class C(A,B):
    object_A = A(1,2)
    object_B = B(3,4)
    object_A.test()
    object_B.test() 
