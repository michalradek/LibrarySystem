from functions.log_in import log_in
from functions.menu import menu
import os


def main():
    os.system("cls")
    print("Library System.")
    print("1. Log in.")
    print("2. Exit")
    for x in range(15):
        print("-", end=" ")
    print()
    try:
        option = int(input("Select option: "))
        if option == 1:
            if log_in():
                menu()
            else:
                print("nie ok")
        elif option == 2:
            exit(1)
    except ValueError:
        input("Select option propertly. Press any key to continue")
        main()


if __name__ == "__main__":
    main()
