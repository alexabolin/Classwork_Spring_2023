# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:41:56 2023

@author: hboli
"""
import pytest


def test_add():
    from add_classwork import add
    answer = add(0.1, 0.2)
    print(pytest.approx(0.3))
