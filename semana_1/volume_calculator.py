import math


def select_figure():
    try:
        figure = float(input("""
    Please select a figure (type the number):
    1) Cylinder
    2) Cube
    Figure: """))
        return figure
    except ValueError:
        pass


def formula():
    figure = select_figure()
    if figure == 1:
        r = float(input("Input radius: "))
        h = float(input("Input height: "))
        area = 2 * math.pi * h * r
        print(f"The area of the cylinder ({r} x {h}) is {area}")
    elif figure == 2:
        h = float(input("Input height: "))
        w = float(input("Input width: "))
        l = float(input("Input length: "))
        area = h * w * l
        print(f"The area of the cube ({h} x {w} x {l}) is {area}")
    else:
        print("Please select a valid option")
        formula()


def run():
    formula()


if __name__ == "__main__":
    run()
