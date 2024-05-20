import os
from functions import menu_options


def menu():
    os.system("cls")
    print("1. Print list of all books.")
    print("2. Download list")
    print("3. Add book to system")
    print("4. Delete book from system")
    print("5. Log out.")
    for x in range(15):
        print("-", end=" ")
    print()
    option = int(input("Select option: "))
    if option == 1:
        menu_options.print_all(menu)
    elif option == 2:
        print("2")
    elif option == 3:
        print("3")
    elif option == 4:
        print("4")
    elif option == 5:
        print("5")
