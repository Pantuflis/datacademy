def range():
    try:
        li = float(input("Input the inferior limit: "))
        ls = float(input("Input the superior limit: "))
        comparative_number = float(input("Input the comparative number: "))
    except ValueError:
        print("Please input a number")
    if comparative_number < ls and comparative_number > li:
        print(comparative_number)
    else:
        print(comparative_number)
        range()


def run():
    range()


if __name__ == "__main__":
    run()
