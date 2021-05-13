def calculate():
    try:
        base = float(input("Input the base: "))
        hight = float(input("Input the hight: "))
        side_1 = float(input("Input the side 1: "))
        side_2 = float(input("Input the side 2: "))
        side_3 = float(input("Input the side 3: "))
        area = (base * hight) / 2
        if side_1 < 0 or side_2 < 0 or side_3 < 0:
            print("Please input positive numbers")
            calculate()
        if side_1 == side_2 and side_3 == side_1:
            type = "Equilatero"
        elif side_1 == side_2 or side_3 == side_1 or side_2 == side_3:
            type = "Isosceles"
        else:
            type = "Escaleno"
        print(
            f"The area of the triangle ({type}) with base of {base} and hight of {hight} is {area}")
    except ValueError:
        print("Please input positive numbers")
        calculate()


def title():
    print("Welcome to the triangles's area calculator")


def run():
    title()
    calculate()


if __name__ == "__main__":
    run()
