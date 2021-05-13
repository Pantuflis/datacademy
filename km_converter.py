def select_mode():
    try:
        mode = int(input("""
    Please select a mode (input the number)
    1) Miles to km
    2) Km to Miles
    
    Mode: 
    """))
        return mode
    except ValueError:
        print("Please input a number")
        convert()


def convert():
    mode = select_mode()
    if mode == 1:
        try:
            miles = float(input("Input the miles you want to convert: "))
            km = 1.609344 / miles
            print(f"{miles} miles is about {km} km")
        except ValueError:
            print("Please input a positive number")
    elif mode == 2:
        try:
            km = float(input("Input the km you want to convert: "))
            miles = km / 1.609344
            print(f"{km} km is about {miles} miles")
        except ValueError:
            print("Please input a positive number")
    else:
        print("Please input a valid option")
        convert()


def run():
    convert()


if __name__ == "__main__":
    run()
