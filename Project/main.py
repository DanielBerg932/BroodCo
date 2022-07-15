from classes.BroodCo import BroodCo


def main():
    terminalUI()


def terminalUI():
    bc = BroodCo()

    def menu():
        print("Welcome to the BroodCo")
        print("1. (Her)Start het programma")
        print("2. Koop brood als client")
        print("3. Exit")
        choice = input("Please choose an option: ")
        return choice

    choice = menu()
    if choice == "1":
        bc.start()
    elif choice == "2":
        bc.buyBreadInteractive()
        bc.printClientStatus()
    elif choice == "3":
        exit()
    else:
        print("Kies een geldige optie")
    terminalUI()


if __name__ == '__main__':
    main()
