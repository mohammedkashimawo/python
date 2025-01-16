if 5<10:
    print("try to know how indentaton works ")#this is an emple of what comment looks like
    print("can you now see that all the execution statements are ll on one line ")
    
    """
    you can use this for your multiline comment
    
    """
    
    
    student="mohammed mojeed ramadan"
    course ='MSC  Arthificial Intelligence'
    
    
    x=20
    print(x)
    
    
    y=int(41916254)
    print(type(y))
    
    x,y,z ="food","water",'house'
    print(z)
    
    
    lam=34
    girls=["shade",'tope','tayo','tade']
    first,second,third,fourth =girls #this process is called unpacking collection
    print(first + second)
    print(first,second,third,fourth) 
    #print(lam+first) #this will definitely return an error.
    
    
    x=34
    x=float(34)  
    
    print(x)
    
    
    
    import random
    print(random.randrange(100,3454))\
        
        #list
        
        
    thislist =['banaba','lesson','joy','office','lesson']
    print(len(thislist))
    
    
    code= list(('noises','ate'))
    print(code)
    
    
    
    pri = ['john','tayo','tolu',404,]
    for x in pri:
      print(pri[0])
      
      
    for a in range(len(pri)):
        print(pri[a])
        
        
social = ['facebook','instagram','twitter']

i=0#initialisation
while i< len(social):#condition
    print(social[i])
    i=i+1#iteration
    
A=30 
B=50 
print('two times hcairman of the local government i come frone') if( A>30) else print('fuck t')

print('jut have to be patient') if( B>A and (B-A == 20) ) else print('national treasurer')\
    
    
print('pay officers we have in the state') if(A < 100) or ( B > A) else print ("we are tryig to do more work")

if (B != 40):
    print('B is indedd not 40')
    


stet =('every', 'second','count','crazy')
a=0
class StaffSalary:
    def __init__(self, admin, sec, account, manager, maintenance, IT, restaurant, director):
        self.admin = admin
        self.sec = sec
        self.account = account
        self.manager = manager
        self.maintenance = maintenance
        self.IT = IT
        self.restaurant = restaurant
        self.director = director
        # This class is defined for the payment of salary for all the staff in the company

# Let's now create the payment for January, February, and March

january = StaffSalary('200', '100', '11', '80', '150', '320', '140', '270')
february = StaffSalary('200', '80', '120', '300', '115', '320', '70', '300')
March = StaffSalary('200', '80', '150', '320', '1240', '50', '70', '320')

# Print specific staff salaries for the mentioned months
print(january.sec)         # Salary of sec in January
print(March.IT)            # Salary of IT in March
print(february.maintenance) # Salary of maintenance in February


#this is just for lambda functions

figaro = lambda a, b, d : a*b*d
print(figaro(23,14,12))


def poat():
    print("youare worthy of my worshipping")
    
poat( )

def age(n):
 print(n)
age(34)#this is how to use a function in a parameter

def names(firstname,secondname):
    print(firstname + secondname)
names('mohammed','mojeed')

def scoresAverage(a,b,c,d,e,f,g,h):
    print((a+b+c+d)/4)
scoresAverage(b=12,c=34,a=55,d=12,e=14,f=45,h=37,g=11)


#by now in ur level of coding you should know that what variable can do , list can also do it


def slow(abj):
 for x in abj:
     print(x)
     
fruits = ["apple", "banana", "cherry"]

slow(fruits)


#now most times we will not need the prnting but rather need the value after the function operation

def orire(a,b):
 return a*b

print(orire(23,12))

def fullname(firstname,secondname):
    return firstname + secondname
print(fullname('mohammed','ramadan'))


#AT times you may not want to use the  function but just define the functions

def serve():
    pass
#just  add pass method or else you will get an error


def position(g):
    if g < 20:
        gh = position(g + 1)  # Recursive call to position with g+1
        print(gh)  # Print the returned value from recursion
        return gh
    else:
        return g  # Base case: return the value when g reaches 20 or highe
    
    
import datetime
x= datetime.datetime.now()
print(x)
print(x.year)
print(x.hour)
print(x.day)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%d"))
print(x.strftime("%m"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%H"))
print(x.strftime("%I"))
#now let us dive into  making the outputed value much more readable
    #lets deal with the date and time modules and methods in python
    


x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)



"""The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:"""

import math
x= math.sqrt(192)
print(x)

"""there aare several other maths methos in python when you  look down to theri reference


math.acos()	Returns the arc cosine of a number
math.acosh()	Returns the inverse hyperbolic cosine of a number
math.asin()	Returns the arc sine of a number
math.asinh()	Returns the inverse hyperbolic sine of a number
math.atan()	Returns the arc tangent of a number in radians
math.atan2()	Returns the arc tangent of y/x in radians
math.atanh()	Returns the inverse hyperbolic tangent of a number
math.ceil()	Rounds a number up to the nearest integer
math.comb()	Returns the number of ways to choose k items from n items without repetition and order
math.copysign()	Returns a float consisting of the value of the first parameter and the sign of the second parameter
math.cos()	Returns the cosine of a number
math.cosh()	Returns the hyperbolic cosine of a number
math.degrees()	Converts an angle from radians to degrees
math.dist()	Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
math.erf()	Returns the error function of a number
math.erfc()	Returns the complementary error function of a number
math.exp()	Returns E raised to the power of x
math.expm1()	Returns Ex - 1
math.fabs()	Returns the absolute value of a number
math.factorial()	Returns the factorial of a number
math.floor()	Rounds a number down to the nearest integer
math.fmod()	Returns the remainder of x/y
math.frexp()	Returns the mantissa and the exponent, of a specified number
math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
math.gamma()	Returns the gamma function at x
math.gcd()	Returns the greatest common divisor of two integers
math.hypot()	Returns the Euclidean norm
math.isclose()	Checks whether two values are close to each other, or not
math.isfinite()	Checks whether a number is finite or not
math.isinf()	Checks whether a number is infinite or not
math.isnan()	Checks whether a value is NaN (not a number) or not
math.isqrt()	Rounds a square root number downwards to the nearest integer
math.ldexp()	Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
math.lgamma()	Returns the log gamma value of x
math.log()	Returns the natural logarithm of a number, or the logarithm of number to base
math.log10()	Returns the base-10 logarithm of x
math.log1p()	Returns the natural logarithm of 1+x
math.log2()	Returns the base-2 logarithm of x
math.perm()	Returns the number of ways to choose k items from n items with order and without repetition
math.pow()	Returns the value of x to the power of y
math.prod()	Returns the product of all the elements in an iterable
math.radians()	Converts a degree value into radians
math.remainder()	Returns the closest value that can make numerator completely divisible by the denominator
math.sin()	Returns the sine of a number
math.sinh()	Returns the hyperbolic sine of a number
math.sqrt()	Returns the square root of a number
math.tan()	Returns the tangent of a number
math.tanh()	Returns the hyperbolic tangent of a number
math.trunc()	Returns the truncated integer parts of a number


"""
x= math.cos(45)
print(x)
x=math.sin(50)
print(x)
x =math.tan(60)
x= math.log(123)

"""Math Constants
Constant	Description
math.e	Returns Euler's number (2.7182...)
math.inf	Returns a floating-point positive infinity
math.nan	Returns a floating-point NaN (Not a Number) value
math.pi	Returns PI (3.1415...)
math.tau	Returns tau (6.2831...)"""


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)#try to note the load method the opposite of it is called the dupm method 

# the result is a Python dictionary:
print(y["age"])


#Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)#ths is used to convert python to json

# the result is a JSON string:
print(y)




print(20/10)

try:
  print('kkkkk')
except NameError:
  print("Variable x is not defined so please try defining it")
except:
  print("Something else went wrong")
  
  
  """ususally there are two basic types of 
  
  
  n Python, errors are classified into several types, which can be broadly divided into two categories:

Syntax Errors
Exceptions (Runtime Errors)
1. Syntax Errors
A syntax error occurs when Python cannot parse the code because it doesn't conform to the correct syntax (grammar) of the language. This type of error is detected by Python during the parsing stage, before the program starts running.

Example:
python
Copy
# Missing parentheses in a print function
print "Hello, World!"  # SyntaxError: Missing parentheses in call to 'print'
In this case, the code has a syntax error because the print function requires parentheses in Python 3.

2. Exceptions (Runtime Errors)
Exceptions are errors that occur during program execution (at runtime). Python has a variety of built-in exceptions that can be raised in different situations.

Here are the most common types of exceptions in Python:

1. ArithmeticError
This is a base class for errors that occur in numeric calculations.

ZeroDivisionError: Raised when dividing by zero.
OverflowError: Raised when the result of an arithmetic operation is too large to be represented.
FloatingPointError: Raised for floating-point calculations.
Example:
python
Copy
# ZeroDivisionError
x = 10 / 0  # ZeroDivisionError: division by zero
2. IndexError
Raised when trying to access an index that is out of the range of a list or other indexable collection.

Example:
python
Copy
lst = [1, 2, 3]
print(lst[5])  # IndexError: list index out of range
3. KeyError
Raised when trying to access a dictionary with a key that does not exist.

Example:
python
Copy
my_dict = {"a": 1, "b": 2}
print(my_dict["c"])  # KeyError: 'c'
4. TypeError
Raised when an operation or function is applied to an object of inappropriate type.

Example:
python
Copy
x = "Hello"
y = 5
print(x + y)  # TypeError: can only concatenate str (not "int") to str
5. ValueError
Raised when a function receives an argument of the right type but inappropriate value.

Example:
python
Copy
x = int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
6. FileNotFoundError
Raised when trying to open a file that doesn't exist.

Example:
python
Copy
open("non_existent_file.txt")  # FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
7. NameError
Raised when trying to access a variable or function name that has not been defined.

Example:
python
Copy
print(x)  # NameError: name 'x' is not defined
8. AttributeError
Raised when an object does not have the specified attribute or method.

Example:
python
Copy
x = 10
x.append(5)  # AttributeError: 'int' object has no attribute 'append'
9. ImportError
Raised when an imported module or a name within a module cannot be found.

Example:
python
Copy
import non_existent_module  # ImportError: No module named 'non_existent_module'
10. RuntimeError
A general error that occurs during runtime and doesn't fall under other more specific exceptions.

Example:
python
Copy
def recurse():
    recurse()  # RuntimeError: maximum recursion depth exceeded
11. StopIteration
Raised by an iterator when there are no more items to return.

Example:
python
Copy
lst = [1, 2, 3]
iterator = iter(lst)
next(iterator)
next(iterator)
next(iterator)
next(iterator)  # StopIteration
12. OverflowError
Occurs when a numerical calculation exceeds the limit for a number type, such as exceeding the size of an integer.

Example:
python
Copy
import math
math.factorial(10000)  # OverflowError: (34, 'Result too large')
13. IndentationError
A subclass of SyntaxError, this error occurs when Python encounters incorrect indentation.

Example:
python
Copy
def greet():
print("Hello, World!")  # IndentationError: expected an indented block
3. Custom Errors (User-Defined Exceptions)
You can also create your own exceptions by subclassing the built-in Exception class
  
  """
  
  
  
  try:
      20/10
  except:
      print("this whould have thrown an error ")
  else:
      print('there was no error detected')
  finally:
      print('ths actually allows you the change to response....you can use it to customise the king of error,esage you want')
      
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
username = input("Enter username:")
print("Username is: " + username)