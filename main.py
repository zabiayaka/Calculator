from calculator.evaluation import evaluate
from calculator.convertor import convert

def add(x,y):
    return x+y

def subtraction(x,y):
    return x-y


def subtramultiplicationction(x,y):
    return x*y


def division(x,y):
    return x/y
try:
    x = int(input("Enter any number: "))
    y = int(input("Enter any number: "))
    print("1 is addition, 2 is subtraction, 3 is multiplication, 4 is division")
    z = int(input("Enter any number from 1 to 4: "))
    if z > 4:
        raise Exception
    elif z < 1:
        raise Exception
    print("1 is decimal and 2 is binary")
    result_format = int(input("Enter number 1 or 2: "))
    if result_format > 2:
        raise Exception
    elif result_format < 1:
        raise Exception
    result_2 = evaluate(x,y,z)
except ValueError as r:
    print("Value is not an int")
except Exception as r:
    print("Value should be in range")

print(convert(result_format, result_2))

