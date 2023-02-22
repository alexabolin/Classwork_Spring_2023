# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:56:40 2023

@author: hboli
"""
import numpy as np

# %% Exercise 1
input1 = ["apple", "banana", "cranberry", "date", "eggplant", "fennel", "guava"]

lessthan = []
overthan = []

def exercise1(grocery):
    for i in grocery:
        if len(i) <= 5:
            lessthan.append(i)
        else:
            overthan.append(i)
    return

def output1():
    print("Less than or equal to 5 letters:")
    for i in lessthan:
        print("{}".format(i))
    print("More than 5 letters:")
    for i in overthan: 
        print("{}".format(i))
    return
        
def program1():
    print("Exercise 1")
    exercise1(input1)
    output1()
    return

program1()
    

# %% Exercise 2
roots = []
final = []

print("\nExercise 2")
inputa = input("Insert value for a:")
inputb = input("Insert value for b:")
inputc = input("Insert value for c:")
a = int(inputa)
b = int(inputb)
c = int(inputc)
 
def exercise2_1(number):
    if number >= 0:
        return "True"
    else:
        return "False"
 
def exercise2_2(a,b,c):
    sol1 = (-b + np.sqrt((b**2)-(4*a*c)))/(2*a)
    sol2 = (-b - np.sqrt((b**2)-(4*a*c)))/(2*a)
    return [sol1, sol2]

def output2():
    for i in roots:
        final.append(exercise2_1(i))
    if final[1] == final[0]:
        print("same sign")
    else:
        print("different sign")
    return

def program2():
    roots.clear()
    final.clear()
    roots.append(exercise2_2(a,b,c)[0])
    roots.append(exercise2_2(a,b,c)[1])
    output2()
    return 

program2()

    
    
    
    


    

       

    
        
        
        
        
        