def interface():
    print("Blood claculator")
    keep_running = True
    while keep_running:
        print("Optional")
        print("9 - Quit")
        choice = input("Select an option: ")
        if choice == "9":
            keep_running = False
    print("Program ending") 


interface()