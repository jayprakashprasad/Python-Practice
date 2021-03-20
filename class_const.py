
#can also be done byb without returning

class Car:
    def __init__(self,type,model,price,milesDrive,owner):
        self.Type=type
        self.Model=model
        self.Price=price
        self.MilesDrive=milesDrive
        self.owner=owner

    def GetType(self):
        return self.Type
    def GetModel(self):
        return self.Model
    def GetPrice(self):
        return self.Price
    def GetMilesDrive(self):
        return self.MilesDrive
    def GetOwner(self):
        return self.owner

    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive() *10)
    
    #different by including other def function
    def myFunc(self):
        print("iam:{}".format(self.owner))


p1=Car("bmw",2015,20000,14,"jay")
print(5-5)
print(p1.Type)
print(p1.Model)

print(p1.Price)
print(p1.MilesDrive)
print(p1.owner)
print("my name is :{}--{}".format(p1.owner,p1.Price))
print("price:{}--".format(p1.GetPrice()-p1.GetMilesDrive()))
print("price:{}--".format(p1.Price-p1.MilesDrive*10 ))
p1.myFunc()

#can also set afterwards
p1.Price=100000
print(p1.Price)








#class in class by init
###
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
  #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()


########2
class Operations:
    def __init__(self,type,model):
        self.Type=type
        self.Model=model
    def sum(self,n1,n2):
        return  n1+n2
    def div(self,n1,n2):
        return n1+n2

class MultiOperations(Operations):
    def mul(self,n1,n2):
        return n1*n2
    def sum(self,n1,n2):

        return  (n1+n2)*2
    #pass .for no error
mop=Operations("bmn","tt")





