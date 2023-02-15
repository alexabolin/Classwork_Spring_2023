# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:23:06 2023

@author: hboli
"""
def input_fruit(filename):
    in_file = open("input_data.txt", "r")
    fruits = in_file.readlines()
    print(fruits)
    in_file.close()
    in_file = open("input_data.txt", "r")
    first_fruit = in_file.readline()
    second_fruit = in_file.readline()
    return fruits, first_fruit, second_fruit

def read_file(filename):
    in2_file = open("input_data.txt", "r")
    line1 = in2_file.readlines()[6]
    patient_data = line1.strip("\n").split("=")
    patient_id = int(patient_data[1])
    return patient_id


def test_read_file():
    from module import read_file
    filename = "input_data.txt"
    answer = read_file(filename)
    expected = 50
    assert answer == expected
