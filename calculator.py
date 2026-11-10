"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return math.log(b, a)

def exp(a, b):
    return a ** b