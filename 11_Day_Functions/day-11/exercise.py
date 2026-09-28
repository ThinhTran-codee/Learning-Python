#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    sum = a + b
    return sum
print(add_two_numbers(3, 5))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area
print(area_of_circle(3))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else: 
            return "All arguments must be numbers."
    return total
print(add_all_nums(1, 2, 3, 4, 5))