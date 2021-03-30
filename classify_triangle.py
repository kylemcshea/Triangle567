# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk

Your correct code goes here...  Fix the faulty logic below until the code passes all of 
you test cases.
    
This function returns a string with the type of triangle from three integer values
corresponding to the lengths of the three sides of the Triangle.
    
return:
If all three sides are equal, return 'Equilateral'
If exactly one pair of sides are equal, return 'Isoceles'
If no pair of  sides are equal, return 'Scalene'
If not a valid triangle, then return 'NotATriangle'
If the sum of any two sides equals the squate of the third side, then return 'Right'
      
BEWARE: there may be a bug or two in this code
"""
def classify_triangle(side1,side2,side3):
    '''Takes in 3 side parematers, returns the classification'''
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(side1,int) and isinstance(side2,int) and isinstance(side3,int)):
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200
    if side1 > 200 or side2 > 200 or side3 > 200:
        return 'InvalidInput'
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return 'InvalidInput'
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (side1 >= (side2 + side3)) or (side2 >= (side1 + side3)) or (side3 >= (side1 + side2)):
        return 'NotATriangle'
    # now we know that we have a valid triangle 
    if side1 == side2 and side2 == side3:
        return 'Equilateral'
    if check_right(side1,side2,side3):
        return 'Right'
    if side2 not in (side1, side3):
        return 'Scalene'
    return 'Isoceles'

def check_right(side1,side2,side3):
    '''Takes in 3 side parameters and checks if triangle is right'''
    if ((side1 ** 2)+(side2 ** 2))==(side3 ** 2) or ((side2 ** 2)+(side3 ** 2))==(side1 ** 2) or ((side1 ** 2)+(side3 ** 2))==(side2 ** 2):
        return True
    return False
