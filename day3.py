#Conditions

x = 10
y = -20

if x > 0 and y > 0:
    print("Both are positive.")
elif x > 0 or y < 0:
    print("X is positive and Y is negative.")
else:
    print("Both are negative")


#Loops

fruits = ['Apple', 'Mango','Guava']

for fruit in fruits:
    print(fruit)


colors = ('red','green','yellow','blue')
for color in colors:
    print(color)


unique_numbers = {1,2,3,4,5,6,7,8,9,0}
for number in unique_numbers:
    print(number)


student_grades = {
    'pranjal' : 90,
    'Bishal' : 20,
    'Ranjit' : 35
}
print(student_grades.values())

for student, grade  in student_grades.items():
    print(student, "scored" , grade)



for value in student_grades.values():
    print(value)


message = "I am live in Dang, Lamahi"

for char in message:
    print(char)


for num in range(1,11):
    print(num)
