import math


def area_of_ellipse(x: list):
    data = x.split(",")
    if len(data) == 1:
        area = math.pi * data[0]**2
    elif len(data) == 2:
        area = math.pi * data[0] * data[1]
    elif len(data) == 4:
        a = (data[2] - data[0]) / 2
        b = (data[3] - data[1]) / 2
        area = math.pi * a * b
    else:
        area = None
    return area

# Notes for BMI_calculator test
# If dealing with numbers, check floats and negative numbers
# If dealing with strings, do null string, lb, lbs, pounds
# exercise with approximation


def add(a, b):
    c = a + b
    return c
