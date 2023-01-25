import blood_calculator as bc

from blood_calculator import *

HDL = 55

HDL_analysis = bc.HDL_analysis(HDL)

print("The HDL analysis is {}".format(HDL_analysis))

bc.generic_input("Other Test")
print(LDL_analysis(13))