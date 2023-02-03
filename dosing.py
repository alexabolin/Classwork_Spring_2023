"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def dose_amount():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    if diagnosis == 1:
        weight_input = patient_weight_input()
        weight = patient_weight_parse(weight_input)
        dosage = patient_dosage(weight, 1)
        output(weight, dosage)
    elif diagnosis == 2:
        weight_input = patient_weight_input()
        weight = patient_weight_parse(weight_input)
        dosage = patient_dosage(weight, 2)
        output(weight, dosage)
    elif diagnosis == 3:
        weight_input = patient_weight_input()
        weight = patient_weight_parse(weight_input)
        dosage = patient_dosage(weight, 3)
        output(weight, dosage)
    elif diagnosis == 4:
        weight_input = patient_weight_input()
        weight = patient_weight_parse(weight_input)
        dosage = patient_dosage(weight, 4)
        output(weight, dosage)
    return


def patient_weight_input():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    return weight_input


def patient_weight_parse(weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    return weight


def patient_dosage(weight, diagnosis):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day


def output(weight, dosage):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage))
    return


if __name__ == '__main__':
    dose_amount()
