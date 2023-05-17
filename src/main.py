from calculator import *



def main():
    """
    This is the main program for the calculating college expenses.
    """
    calculator = Calculator()

    while True:
        """
        This is an infinite loop that displays the menu. The user will choose a option in the menu and based on the option, it will call different functions in the calculator class. The loop will only end when the user selects the "Exit program" option.
        """
        print("\nMenu:")
        print("1. Load data")
        print("2. Calculate totals")
        print("3. Sort by total cost")
        print("4. Exit program")
        if calculator.data is not None:
          print("5. Enter scholarship cost")
          print("6. See benefits for each school")

        choice = input("Select an option: ")
        if choice == "1":
            calculator.load_data()
        elif choice == "2":
            calculator.calculate_totals()
        elif choice == "3":
            calculator.sort_by_total_cost()
        elif choice == "5" and calculator.data is not None:
            calculator.subtract_scholarship()
        elif choice == "6" and calculator.data is not None:
            calculator.view_benefits()
        elif choice == "4":
            break
        else:
            print("Error: Invalid choice.")
          
if __name__ == "__main__":
    main()