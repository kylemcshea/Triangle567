# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from classify_triangle import classify_triangle
from classify_triangle import check_right

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5,12,13),'Right','5,12,13 is a Right triangle')
        self.assertEqual(classify_triangle(9,12,15),'Right','9,12,15 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classify_triangle(13,12,5),'Right','5,12,13 is a Right triangle')
        self.assertEqual(classify_triangle(9,15,12),'Right','9,12,15 is a Right triangle')

    def testScalene(self):
        self.assertEqual(classify_triangle(112,43,79),'Scalene','112,43,79 is a Scalene triangle')
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(2,2,2),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(100,100,100),'Equilateral','1,1,1 should be equilateral')
    def testInvalid(self):
        self.assertEqual(classify_triangle(-1,1,1),'InvalidInput','-1,1,1 should be invalid')
        self.assertEqual(classify_triangle(300,1,1),'InvalidInput','300,1,1 should be invalid')
        self.assertEqual(classify_triangle("lol",1,1),'InvalidInput','lol,1,1 should be invalid')
    def testRight(self):
        self.assertEqual(check_right(3,4,5),True,'3,4,5 should return true')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

