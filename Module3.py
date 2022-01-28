#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:09:24 2022

@author: mohammadhovaidi-ardestani
https://edube.org/learn/pe-1/
"""

x = int(input("x: "))
if x >= 100:
    print("True")
else:
    print("False")
    
# Conditions and conditional execution
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)