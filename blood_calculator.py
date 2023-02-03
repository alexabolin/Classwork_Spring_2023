def interface():
    print("Blood claculator")
    keep_running = True
    while keep_running:
        print("Optional")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Cholesterol")
        print("9 - Quit")
        choice = input("Select an option: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            Chol_driver()
    print("Program ending")


def generic_input(test_name):
    test_value = input("Enter the {} results: ".format(test_name))
    test_value = int(test_value)
    return test_value


def HDL_driver():
    HDL_in = generic_input("HDL")
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)


def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def HDL_output(HDL_value, HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value, HDL_analy))
    return


def LDL_driver():
    LDL_in = generic_input("LDL")
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_analy)


def LDL_analysis(LDL_int):
    if LDL_int < 130:
        answer = "Normal"
    elif 130 <= LDL_int < 160:
        answer = "Borderline High"
    elif 160 <= LDL_int < 190:
        answer = "High"
    else:
        answer = "Very High"
    return answer


def LDL_output(LDL_value, LDL_analy):
    print("The LDL result of {} is considered {}".format(LDL_value, LDL_analy))
    return


def Chol_driver():
    Chol_in = generic_input(" total cholesterol")
    Chol_analy = Chol_analysis(Chol_in)
    Chol_output(Chol_in, Chol_analy)


def Chol_analysis(Chol_int):
    if Chol_int >= 240:
        answer = "High"
    elif 200 <= Chol_int < 240:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer


def Chol_output(Chol_value, Chol_analy):
    print("The total cholesterol result of {} is considered {}"
          .format(Chol_value, Chol_analy))
    return


if __name__ == "__main__":
    interface()
