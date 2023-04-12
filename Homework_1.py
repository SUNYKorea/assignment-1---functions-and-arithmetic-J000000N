# Name: Joonhyeong Kim
# SBUID: 114001304
##################### SCORE ######################
####### Very good work Score:  10/10
#################################################
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 


def fahrenheit2celsius(fahrenheit): 
   celsius = 5/9 * (fahrenheit - 32)
   print(celsius)
   return celsius

def what_to_wear(celsius):
    if celsius > 20:
       print("T-shirt")
    elif celsius > 10:
       print("Light Jacket")
    elif celsius > 0:
        print("Sweater")
    elif celsius > -10:
        print("Scarf")
    else:
        print("Puffy Jacket")
    
       
       

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = 1/2 * ((x1*y2 + x2*y3 + x3*y1)-(x1 * y3 + x2 * y1 + x3 * y2))
    return abs(area)

def euclidean_distance(x1, y1, x2, y2):
    distance = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = euclidean_distance(x1, y1, x2, y2)
    s2 = euclidean_distance(x3, y3, x2, y2)
    s3 = euclidean_distance(x1, y1, x3, y3)
    parameter = s1 + s2 + s3
    return parameter



# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math



def deg2rad(deg):
    rad = (float(deg) / 180) * math.pi
    return float(rad)
  
def apothem(number_sides, length_side):
   ap = float(length_side) /(2 * math.tan(deg2rad(180 / int(number_sides))))
   return float(ap)
def polygon_area(number_sides, length_side):
   area = int(number_sides) * float(length_side) * apothem(number_sides, length_side) / 2
   return area


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

