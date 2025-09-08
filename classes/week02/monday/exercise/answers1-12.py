from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
def make_tea():
    print("1. Boiling water...")
    print("2. Placing a tea bag in a cup.")
    print("3. Pouring boiled water into the cup.")
    print("4. Letting the tea steep for a few minutes.")
    print("5. Removing the tea bag.")
    print("6. Adding sugar, milk, or lemon (optional).")
    print("7. Stirring the tea.")
    print("8. Tea is ready to serve!")


make_tea()



pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
list = [2, 4, 6, 8, 10]
print(list[4]+2, list[4]+4, list[4]+6) 


pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


print(f"Hello, {first_name} {last_name}!")



pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
import sys
import platform


print("Python version:", sys.version)
print("Platform:", platform.platform())



pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
num1 = float(input("Enter number here:"))
num2 = float(input("Enter a different number here:"))
print('Sum:', num1+num2)
print('Difference: ', num1 - num2)
print('Product: ', num1 * num2)
print('Standard Division: ', num1/num2)
print('Floor Division: ', num1//num2)

#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''

sentence = input("Enter a sentence here:")
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.split())


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
print("No parentheses:",float(10 + 2 * 5 / 2 - 3 ** 2))
print("Parentheses:",float((10 + 2) * 5 / (2 - 3) ** 2))


pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
food_list= ['pasta', 'pizza','burger']
food_list[2] = 'green beans'
print(food_list)


pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
tuple1 = (1, 2, 3, 4)
try:
    tuple1[0]= 8
except TypeError as e:
    print("Error:", e)
    print(tuple1)


pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
students = {'patricia':16, 'clarice':20, 'martin':17}
print(students)
students['patricia']= 18
print(students)

fav_num= [24, 7, 2]
print(fav_num)
fav_num.append(4)
print(fav_num)


pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
quote = input("Enter your favorite quote here:")

with open("quotes.txt", "w") as file:
    file.write(quote)

with open("quotes.txt", "r") as file:
    saved_quote = file.read()

print("Your saved quote is:")
print(saved_quote)


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
num1 = int(input("Enter a number here:"))
num2 = int(input("Enter another number here:"))
num3 = int(input("Enter another number here:"))
num4 = int(input("Enter another number here:"))
num5 = int(input("Enter another number here:"))

list = [num1, num2, num3, num4,num5]
print("List:",list)

import statistics
print("Sum:", sum(list))
print("Average:", statistics.mean(list))

pause=input('pause')
clear_screen()