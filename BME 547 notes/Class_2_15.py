# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:08:25 2023

@author: hboli
"""
#
# Cell Live/Die Assay:
# Image data = RGB:
# R, G, and B = 0-255.
# break picture up into red and green channels.
# if that's all we are interested in after certain threshold,
# cells are "red" or "green".
# Format:
# Image size (e.g. 8 6  8x6):
# numbers reresenting amount of color by pixel, are
# separated by commas.
# Specs:
# if number > 75, cell is alive (green) or dead (red).
# it is impossible for cell to be both red and green.
# will calculate = live/dead fraction and live/dead cell density.
# no need for input.
# determine total number of data pts in image for each patient.
# determine if test passed, failed, or tentative_pass/
# failed (aka result).
# output file = dictionary in json format with first name,
# last name, DOB, cell total, live total, dead total, result.
# REMEMBER DOCSTRINGS
# END should be after each patient
