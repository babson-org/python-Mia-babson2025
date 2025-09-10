from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
number = int(input("Please enter a number:"))
if number > 0:
    print("Positive")
elif number < 0: 
    print("Negative")
elif number == 0:
    print("Zero")



pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
number = int(input("Please enter a number:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")



pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
num1 = int(input("Please enter a number here:"))
num2 = int(input("Please enter another number here:"))
if num1 and num2 >= 0:
    print("Both are positive")
elif num2 < 0 and num1 >= 0:
    print("The first number is positive")
elif num2 >= 0 and num1 < 0:
    print("The second number is positive")
elif num1 and num2 < 0:
    print("Neither are positive")



pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
#just multiples of 3
for i in range (0,21,3):
    print(i)

#excluding multiples of 3
for i in range(0,21):
    if i % 3 != 0:
        print(i)


pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
secret_number = 3
number = int(input("Guess a number:"))
while number != secret_number:
    print("Incorrect, try again!")
    number = int(input("Guess a number:"))
else:
   print("Correct, good guess!")



pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
c = 0
while c < 11:
    c = c+1
    if c == 3:
        continue
    elif c == 8:
        break
    print(c)




pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
number = int(input("Please enter a number:"))
def square(number):
    return number ** .5
print("The square root is", square(number))

    """
    Purpose: 
    """
    
# end def



pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
def add_item(lst, item):
    lst.append(item)

my_list = [1, 2, 3]
print(my_list)
add_item(my_list, 6)
print(my_list)

    """
    Purpose: 
    """
    
# end def



pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
name = input("Enter your name:")
def greet(name):   #defining the function             


    print(name)       
    """ 
This asks for input from the user
and then the program will say Hello to that person
greeting them with their name
    
    """
response = "Hello " + name
print(response)                    


pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
name1 = input("Enter a name:")
name2 = input("Enter another name:")
name3 = input("Enter another name:")
name4 = input("Enter another name:")
name5 = input("Enter another name:")

my_list = [name1, name2, name3, name4, name5]
my_list.sort()


print(my_list)
 


pause=input('pause')
clear_screen()