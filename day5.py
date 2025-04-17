def add(a,b):
     return a+b 

result = add(1,2)
print(result)

class Calculation :
     def add(self,a,b):
          return a+b
     
calculator = Calculation()
result2 = calculator.add(2,3)
print(result2)


#Inheritance
class Animal:
    def __init__(self,name):
        print("Animal constructor is called ", name)
        self.name = name

    def eat(self):
            print("I can eat")

    def sleep(self):
                print("I can sleep")

class Dog(Animal):
    def bark(self):
        print(" I can bark..")

dog1 = Dog("German Shephered.")
dog1.eat()
    