from decimal import *
getcontext().prec = 3

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    divide = num1/float(num2)
    return Decimal(divide)

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2
