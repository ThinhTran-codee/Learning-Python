#Calculator an area of the triangle
print('Enter base: ')
base = float(input())

print('Enter height: ')
height = float(input())

area = 0.5 * base * height
print('The area of the triangle is', area)

#Calculate the perimeter of the triangle
print('Enter side a: ')
a = float(input())

print('Enter side b: ')
b = float(input())

print('Enter side c: ')
c = float(input())

perimeter = a + b + c
print('The perimeter of the triangle is', perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print('Enter length: ')
length = float(input())

print('Enter width: ')
width = float(input())

area = length * width
perimeter = 2 * (length + width)

print('The area of the rectangle is', area)
print('The perimeter of the rectangle is', perimeter)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print('Enter radius: ')
radius = float(input())

pi = 3.14
areaCircle = pi * radius ** 2
circumference = 2 * pi * radius

print('The area of circle is', areaCircle)
print('The circumference of circle is', circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slopeTask8 = 2
y_intercept = -2 #Solving for y when x = 0: y = 2(0) - 2 => y = -2
x_intercept = 1  # Solving for x when y = 0: 0 = 2x - 2 => x = 1

print('The slope is', slopeTask8)
print('The y-intercept is', y_intercept)
print('The x-intercept is', x_intercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

slopeTask9 = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print('The slope is', slopeTask9)
print('The Euclidean distance is', euclidean_distance)

# Compare the slopes in tasks 8 and 9
if slopeTask8 > slopeTask9:
    print("The slope in task 8 is steeper than in task 9.")
elif slopeTask8 < slopeTask9:
    print("The slope in task 9 is steeper than in task 8.")
else:
    print("The slopes in tasks 8 and 9 are the same.")

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
x = float(input('Enter x: '))
y = x ** 2 + 6 * x + 9
print('The value of y is', y)


#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len('python')
dragon_length = len('dragon')
print('Length of python: ', python_length)
print('Length of dragon: ', dragon_length)
print('Falsy comparison (python == dragon): ', python_length == dragon_length)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("The substring 'on' is found in both 'python' and 'dragon'.")
else:
    print("The substring 'on' is not found in both 'python' and 'dragon'.")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
if 'jargon' in sentence:
    print("The word 'jargon' is found in the sentence.")
else:
    print("The word 'jargon' is not found in the sentence.")

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour = float(input('Enter hours: '))
rate_per_hour = float(input('Enter rate per hour:'))
pay = hour * rate_per_hour
print('The pay of the person is', pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter number of years: '))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_in_a_year
print('The number of seconds a person can live is', total_seconds)

#Write a Python script that displays the following table
print("Number\tSquare\tCube")
for i in range(1, 6):
    print(f"{i}\t{i**2}\t{i**3}")
    
