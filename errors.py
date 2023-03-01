def my_function(x):
    number = x / 2
    try:
        type_in = type(numer)
    except NameError:
        type_in = type(number)

    if type_in == int:
        print("even")
    else:
        print("odd")


def main():
    x = -3
    try:
        my_function(x)
    except TypeError:
        try:
            new_num = int(x)
            answer = my_function(new_num)
            print(answer)
        except ValueError:
            print("Must enter number")
    except ValueError:
        print("Must enter positive number")


if __name__ == "__main__":
    main()
