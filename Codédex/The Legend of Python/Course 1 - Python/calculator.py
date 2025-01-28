import math

print("""
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐                                                                                                                                 ▌
▐      █████╗ ██████╗ ███████╗ █████╗      ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗      ▌
▐     ██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗     ▌
▐     ███████║██████╔╝█████╗  ███████║    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝     ▌
▐     ██╔══██║██╔══██╗██╔══╝  ██╔══██║    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗     ▌
▐     ██║  ██║██║  ██║███████╗██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║     ▌
▐     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ▌
▐                                                                                                                                 ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
""")

def area_square():
    side = float(input("\nSide lenght: "))
    area_square = (side**2)
    print(f"\nThe area is {area_square}")

def area_rectangle():
    lenght = float(input("\nLenght: "))
    width = float(input("Width: "))
    area_rectangle = lenght * width
    print(f"\nThe area is {area_rectangle}")

def area_triangle():
    height = float(input("\nHeight: "))
    base = float(input("Base: "))
    area_triangle = (height*base)/2
    print(f"\nThe area is {area_triangle}")

def area_circle():
    radius = float(input("\nRadius: "))
    area_circle = math.pi * (radius**2)
    print(f"\nThe area is: {area_circle:.3f}")

def menu():
    while True:
        print("Choose which area you want to calculate:\n[1] Square\n[2] Rectangule\n[3] Triangule\n[4] Circle\n[5] Quit\n")
        try:
            escolher_opcao = int(input("Enter a number (1-5): "))
            if escolher_opcao == 1:
                area_square()
            elif escolher_opcao == 2:
                area_rectangle()
            elif escolher_opcao == 3:
                area_triangle()
            elif escolher_opcao == 4:
                area_circle()
            elif escolher_opcao == 5:
                print("Goodbye")
                break
            else:
                print("Invalid input! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    menu()