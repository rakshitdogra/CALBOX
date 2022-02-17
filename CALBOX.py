#Copyright (c) 2022 rakshitdogra

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import cmath
import statistics
import math
import matplotlib.pyplot as plt
from fractions import Fraction
from sympy import *
from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError

def p_circle(radius):  
    para = 2 * 3.14 * radius  
    print("Perimeter of Circle:", para)  
  
def v_rectangle(height, width ,length):  
    vol = (height * length * width)
    print("Volume of Rectangle:", vol)

def v_cube(side):  
    vol = (side * side* side)
    print("Volume of Rectangle:", vol)

def v_cone(radius, height):  
    vol = (3.14*(radius**2)*(height/3))
    volcone=round(vol,2)
    print("Volume of Rectangle:", volcone)

def p_rectangle(height, width):  
    para = 2 * (height + width)  
    print("Perimeter of Rectangle:", para) 
  
def p_square(side):  
    para = 4 * side  
    print("Perimeter of Square:", para)  
  
def a_circle(radius):  
    area = 3.14 * radius * radius  
    print("Area of Circle:", area)  
  
def a_rectangle(height, width):  
    area = height * width  
    print("Area of Rectangle:", area)  
  
def a_square(side):  
    area = side * side  
    print("Area of Square:", area)

def get_combination(string, i=0):
    if i == len(string):   	 
        print("".join(string))
    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        get_combination(words, i + 1)

def isMember(a, d, x):
    if d == 0:
        return x == a
    return ((x - a) % d == 0 and
        int((x - a) / d) >= 0)

def solve(x, y):
        mp = {}
        for i in range(len(x)):
            a = x[i]
            b = y[i]
            if a not in mp:
                mp[a] = b
            else:
                return False
        return True

def compute_hcf(x, y):
        while(y):
            x, y = y, x % y
        return x

def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def equationroots( a, b, c):
    
	dis = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))

def add(num1, num2):
    return num1 + num2
  
def subtract(num1, num2):
    return num1 - num2
  
def multiply(num1, num2):
    return num1 * num2
  
def divide(num1, num2):
    return num1 / num2

def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f,var).doit()
    pprint(d)

print("****CALBOX****")  

while True:  
    print("\nMAIN MENU")
    print("1. Simple calculator")
    print("2. Calculate Perimeter")
    print("3. Calculate Area")  
    print("4. Calculate Volume")
    print("5. Find Permutaion and Combination")
    print("6. Find Prime or not")
    print("7. Find factorial")
    print("8. Find Square root") 
    print("9. Converter")
    print("10. Convert Decimal to Binary, Octal and Hexadecimal")
    print("11. Find HCF & LCM") 
    print("12. Find Factors of a number") 
    print("13. Find Roots of Quadratic Equation")
    print("14. Find probability")
    print("15. Find Intrest")
    print("16. Coordinate geometry")
    print("17. Statistics")
    print("18. Arithmetic Progression")
    print("19. Find Limit")
    print("20. Find Derivative")
    choice1 = int(input("Enter the Choice: "))

    if choice1 == 1:
        print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
        select = int(input("Select operations form 1, 2, 3, 4 :"))
  
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
  
        if select == 1:
            print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
        elif select == 2:
            print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
        elif select == 3:
            print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
        elif select == 4:
            print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
        else:
            print("Invalid input")

    elif choice1 == 2:  
        print("\nCALCULATE PARAMETER")  
        print("1. Circle")  
        print("2. Rectangle")  
        print("3. Square")  
        print("4. Exit")  
        choice2 = int(input("Enter the Choice: "))  
  
        if choice2 == 1:  
            radius = int(input("Enter Radius of Circle:"))  
            p_circle(radius)  
              
        elif choice2 == 2:  
            height = int(input("Enter Height of Rectangle:"))  
            width = int(input("Enter Width of Rectangle:"))  
            p_rectangle(height, width)  
              
        elif choice2 == 3:  
            side = int(input("Enter Side of Square:"))  
            p_square(side)  
  
        elif choice2 == 4:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 3:  
        print("\nCALCULATE AREA")  
        print("1. Circle")  
        print("2. Rectangle")  
        print("3. Square")  
        print("4. Exit")  
        choice3 = int(input("Enter the Choice: "))  
  
        if choice3 == 1:  
            radius = int(input("Enter Radius of Circle:"))  
            a_circle(radius)  
              
        elif choice3 == 2:  
            height = int(input("Enter Height of Rectangle:"))  
            width = int(input("Enter Width of Rectangle:"))  
            a_rectangle(height, width)  
              
        elif choice3 == 3:  
            side = int(input("Enter Side of Square:"))  
            a_square(side)  
  
        elif choice3 == 4:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  

    elif choice1 == 4:  
        print("\nCALCULATE Volume")  
        print("1. Cone")  
        print("2. Rectangle")  
        print("3. Square")  
        print("4. Exit")  
        choice3 = int(input("Enter the Choice: "))  
  
        if choice3 == 1:  
            radius = int(input("Enter Radius of Cone: "))
            height = int(input("Enter height of Cone: "))  
            v_cone(radius,height)  
              
        elif choice3 == 2:  
            height = int(input("Enter Height of Rectangle:"))  
            width = int(input("Enter Width of Rectangle:"))
            length = int(input("Enter length of Rectangle:"))  
            v_rectangle(height, width, length)  
              
        elif choice3 == 3:    
            side = int(input("Enter Side of square:"))  
            print(side**3)  
  
        elif choice3 == 4:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
    
    elif choice1 == 5:
        permnumber = input("Enter: ")
        print(get_combination(permnumber))

    elif choice1 == 6:
            numprime = int(input("Enter a number: "))
            if numprime > 1:
                for i in range(2,numprime):
                    if (numprime % i) == 0:
                        print(numprime,"is not a prime number")
                        print(i,"times",numprime//i,"is",numprime)
                        break
                    else:
                        print(numprime,"is a prime number")
                else:
                    print(numprime,"is not a prime number")

    elif choice1 == 7:
        num = int(input("Enter a number: "))
        factorial = 1

        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,num + 1):
                factorial = factorial*i
            print("The factorial of",num,"is",factorial)

    elif choice1 == 8:  
        print("\nCALCULATE Square Root")  
        print("1. Find Square root")  
        print("2. Find Square root of Complex Numbers")   
        print("3. Exit")  
        choice3 = int(input("Enter the Choice: "))  
  
        if choice3 == 1:  
            num = float(input('Enter a number: '))
            num_sqrt = num ** 0.5
            print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))  
              
        elif choice3 == 2:  
            num = eval(input('Enter a number: '))
            num_sqrt = cmath.sqrt(num)
            print('The square root of {0} is {1:0.3f}+{2:0.3f}j'
            .format(num ,num_sqrt.real,num_sqrt.imag))

        elif choice3 == 3:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.") 


    if choice1 == 9:  
        print("\nCONVERTER")  
        print("1. kilometers to miles")  
        print("2. miles to kilometer")  
        print("3. Celsius to fahrenheit")  
        print("4. fahrenheit to Celsius")

        choice2 = int(input("Enter the Choice: "))  
  
        if choice2 == 1:
            kilometers = float(input("Enter value in kilometers: "))
            conversion_fac = 0.621371
            miles = kilometers * conversion_fac
            print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

        if choice2 == 2:
            miles = float(input("Enter value in miles: "))
            conversion_fac = 0.621371
            kilometers = miles / conversion_fac
            print('%0.2f Miles is equal to %0.2f kilometer' %(kilometers,miles))

        if choice2 == 3:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 1.8) + 32
            print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

        if choice2 == 4:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) / 1.8
            print('%0.1f degree Celsius is equal to %0.1f fahrenheit)' %(celsius,fahrenheit))
            
    elif choice1 == 10:
        dec = eval(input('Enter a number: '))
        print("The decimal value of", dec, "is:")
        print(bin(dec), "in binary.")
        print(oct(dec), "in octal.")
        print(hex(dec), "in hexadecimal.")

    elif choice1 == 11:  
        print("\nFind LCM & HCF")  
        print("1. Find HCF")  
        print("2. Find LCM")   
        print("3. Exit")  
        choice3 = int(input("Enter the Choice: "))  
  
        if choice3 == 1:  
            number1 = float(input("Enter the 1st number: "))
            number2 = float(input("Enter the 2nd number: "))
            hcf = compute_hcf(number1, number2)
            print("The HCF is", hcf) 
              
        elif choice3 == 2:  
            number1 = float(input("Enter the 1st number: "))
            number2 = float(input("Enter the 2nd number: "))
            print("The L.C.M. is", compute_lcm(number1, number2))

        elif choice3 == 3:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.") 


    elif choice1 == 12:
        num=int(input("Enter a number: "))
        factors=[]
        for i in range(1,num+1):
            if num%i==0:
                factors.append(i)

        print ("Factors of {} = {}".format(num,factors))

    elif choice1 == 13:
        a =int(input("Enter a number1: "))
        b =int(input("Enter a number2: "))
        c =int(input("Enter a number3: "))
        dis = (b**2) - (4 * a*c)
        ans1 = (-b-cmath.sqrt(dis))/(2 * a)
        ans2 = (-b + cmath.sqrt(dis))/(2 * a)
        print('The roots are')
        print(ans1)
        print(ans2)

    elif choice1 == 14:
        a =int(input("Enter a number of Possible outcomes: "))
        b =int(input("Enter a Total possible outcomes: "))
        print ("Probability of the event: ",(Fraction(a, b)))

    if choice1 == 15:  
        print("\n FIND INTEREST MENU")  
        print("1. Find the simple interest")  
        print("2. Find the compound interest")

        choice2 = int(input("Enter the Choice: "))  
  
        if choice2 == 1:
            p =int(input("Enter the principal amount: "))
            t =int(input("Enter time period: "))
            r =int(input("Enter rate of interest: "))
            print ("Simple interest: ",((p * t * r)/100))

        if choice2 == 2:
            p =int(input("Enter the principal amount: "))
            t =int(input("Enter time period: "))
            n =int(input("Enter number of times interest applied: "))
            r =float(input("Enter rate of interest: "))
            finals=p*(1+(r/n))**(n*t)
            limited_finals=round(finals,2)
            print ("Compound interest: ",limited_finals)

    elif choice1 == 16:  
        print("\nCOORDINATE GEOMETRY")  
        print("1. Plot the graph")  
        print("2. Exit ")  
        choice54 = int(input("Enter the Choice: "))  
  
        if choice54 == 1:
            print("\nCG MENU")  
            print("1. Plot the graph of 2 points")  
            print("2. Plot the graph of 3 points")  
            print("3. Plot the graph of 4 points")  
            print("4. Exit")  
            choice16 = int(input("Enter the Choice: "))

            if choice16 == 1:
                print("Enter Coordinates of 1st point")
                x1 =int(input("Enter the value of x1: "))
                y1 =int(input("Enter the value of y1: "))
                print("Enter Coordinates of 2nd point")
                x2 =int(input("Enter the value of x2: "))
                y2 =int(input("Enter the value of y2: "))

                x=[x1,x2]
                y=[y1,y2]

                plt.plot(x, y, color="black")
                plt.xlabel('x - axis')
                plt.ylabel('y - axis')
                plt.title('The graph')
                plt.show()
                print("The graph is successfully plotted: ")

            elif choice16 == 2:
                print("Enter Coordinates of 1st point")
                x1 =int(input("Enter the value of x1: "))
                y1 =int(input("Enter the value of y1: "))
                print("Enter Coordinates of 2nd point")
                x2 =int(input("Enter the value of x2: "))
                y2 =int(input("Enter the value of y2: "))
                print("Enter Coordinates of 3rd point")
                x3 =int(input("Enter the value of x3: "))
                y3 =int(input("Enter the value of y3: "))

                x=[x1,x2,x3]
                y=[y1,y2,y3]

                plt.plot(x, y, color="black")
                plt.xlabel('x - axis')
                plt.ylabel('y - axis')
                plt.title('The graph')
                plt.show()
                print("The graph is successfully plotted: ")

            elif choice16 == 3:
                print("Enter Coordinates of 1st point")
                x1 =int(input("Enter the value of x1: "))
                y1 =int(input("Enter the value of y1: "))
                print("Enter Coordinates of 2nd point")
                x2 =int(input("Enter the value of x2: "))
                y2 =int(input("Enter the value of y2: "))
                print("Enter Coordinates of 3rd point")
                x3 =int(input("Enter the value of x3: "))
                y3 =int(input("Enter the value of y3: "))
                print("Enter Coordinates of 4th point")
                x4 =int(input("Enter the value of x4: "))
                y4 =int(input("Enter the value of y4: "))
                

                x=[x1,x2,x3,x4]
                y=[y1,y2,y3,y4]

                plt.plot(x, y,color="black")
                plt.xlabel('x - axis')
                plt.ylabel('y - axis')
                plt.title('The graph')
                plt.show()
                print("The graph is successfully plotted: ")
 
  
            elif choice16 == 4:  
                break  

    if choice1 == 17:  
        print("\nSTATISTICS MENU")  
        print("1. Find mean")  
        print("2. Find mode")  
        print("3. Find the median of grouped continuous data")  
        print("4. Find the median of grouped continuous data *(with interval)*")

        choice2 = int(input("Enter the Choice: "))  
  
        if choice2 == 1:
                lst = []
                n = int(input("Enter number of elements : "))
                for i in range(0, n):
                    ele = int(input())
                    lst.append(ele)
                x = statistics.mean(lst)
                lim_x=round(x,2)
                print("Mean is :", lim_x)

        elif choice2 == 2:
                lst = []
                n = int(input("Enter number of elements : "))
                for i in range(0, n):
                    ele = int(input())
                    lst.append(ele)
                x = statistics.mode(lst)
                lim_x=round(x,2)
                print("Mode of given data set is: % s" % (statistics.mode(lst)))


        if choice2 == 3:
                lst = []
                n = int(input("Enter number of elements you want to add in data list : "))
                for i in range(0, n):
                    ele = int(input())
                    lst.append(ele)
                x = statistics.median_grouped(lst)
                lim_x=round(x,2)
                print(statistics.median_grouped(lst))

        if choice2 == 4:
                lst = []
                n = int(input("Enter number of elements you want to add in data list : "))
                for i in range(0, n):
                    ele = int(input())
                    lst.append(ele)
                x = statistics.median_grouped(lst)
                lim_x=round(x,2)
                interval = int(input("Enter the interval (if any): "))
                print(statistics.median_grouped(lst,interval))

    elif choice1 == 18:  
        a =int(input("Enter the value of first term: "))
        x =int(input("Enter the value of the number you want to check: "))
        d =int(input("Enter the value of difference: "))
        if isMember(a, d, x):
            print( "Yes")
        else:
            print("No")
 
    elif choice1 == 19: 
        x = symbols('x')
        expr = input('Enter the expression: ');
        print("Expression : {}".format(expr))
        limit_expr = limit(expr, x, 0) 
        print("Limit of the expression tends to 0 : {}".format(limit_expr)) 

    elif choice1 == 20:
        if __name__=='__main__':
    
            f=input('Enter: ')
            var = input('Enter the variable with respect to: ')
            try:
                f = sympify(f)
            except SympifyError:
                print("Ivalid output")
            else:
                derivative(f,var)

    next_calculation = input("Do you want to do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
