#Functional Decomposition 
#
#flow chart:
# 1. Read input data
#    - what does data look like?
#    - input = txt file
#    - output = list of strings for each line
# 2. Parse data/separate (decomposed further)
#       a. Split strings to get test and value (output = testlist and valuelist)
#       b. convert data type (make valuelist a list of integers)
#       c. convert to dictionary (make dictionary; HR: int, BP_low: int, etc.)
# 3. Analyze data
#    - input = dictionary
#    - outpt = dictionary; HR: 'Normal', BP: 'Abnormal', etc.
# 4. Output data
#    - input = dictionary
#    - output = string: 'Normal' or 'WARNING: {} is abnormal' (HR, BP, etc.)
#
#CPAP Assignment
# - text file format = time, P2 pressure, P1_insp, P1_exp (whichever is larger is used for
#                      flow rate vs time graph)
# - flow of pressure only goes from pump to patient
# - any excess pressure coming from patient will be released through valve, turning off pump
# - higher flow = lower pressure
# - need to calculate flow and pressure drop during inhalation (pump to middle, P1_insp) and
#   exhalation (middle to patient, P1_exp)
# - if p1_insp, > p1_exp (flow towards patient), p1_exp > p1_insp (flow away from patient)
# - can hardcode file name, only reads one file at a time
# - error log if entry is non-numeric, missing, or NaN and skip the person
# - calculate flow versus time, then create dictionary 'metrics'
# - this should include duration of data, number of breaths, breath rate (bpm), times at
#   which breaths occured, apnea count (time btw breaths > 10 sec), and leakage due to mask
#   (difference between integral of gas going in (positive flow) and gas coming out (negative
#    flow)) -if leakage is negative, have warning log entry
# - save as json file (same as name of txt file)
# - breaths can be counted if exhale reaches zero (doesn't need to be negative)
# - Use MIT License
# - get everything to work with one patient, then try to tweak breath finder for other ones
# - exception handling may be helpful