# main.py file
import functions
from prettytable import PrettyTable



# city = 'amsterdam'
# functions.get_data(city)

while True:

    functions.menu()

    choise = input("\nWhat would you like to do? \n")

    if choise == "1":
        functions.view_data(0)

    elif choise == "2":
        functions.add_data()

    elif choise == "3":
        functions.data_options()

    elif choise == "4":
        functions.delete_data()

    elif choise == "5":
        print("\n Goodbye\n")
        exit()

    else:
       print("\n Not Valid Choice Try again\n")









