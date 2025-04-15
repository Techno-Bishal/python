def greet(name):
    print(f"Hello {name}")

greet('Pranjal') 
greet('Sanskrit') 


def addNumbers(num1, num2):
    print(f"Sum of two numbers is {num1 + num2}")

addNumbers(2, 3)
addNumbers(1000320, 23423)



#using lamba(Anynomous Fucntion)

add = lambda a,b : a+b
multiply = lambda x,y : x*y

print("Multiplication of two number is : ", multiply(2,3))
print(add(1,2))


def even_numbers(number):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd.")

even_numbers(10)