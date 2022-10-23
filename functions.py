import requests
import json
from prettytable import PrettyTable
import os

file = 'weather.json'


# def create_user(name):
#     with open("weather.json") as json_file:
#         data = json.load(json_file)
#         temp = data["user"]
#         new_user = {"naam": name}
#         temp.append(new_user)
#
#     write_json(data, file)
#
# def check_user():
#     with open(file, "r") as f:
#         temp = json.load(f)
#         for entry in temp["user"]:
#             name = entry["naam"]
#             if len(name) > 1:
#                 registered = 1
#         return registered
#
#
# def introduction(registered):
#     if registered == 0:
#         print("\nWelcome to Weather Overview!\n"
#               "The number one in overviewing the weather :)\n")
#         name = input("What is your name?\n")
#         return name


# menu options
def menu():
    print('\n')
    myTable = PrettyTable(['---Weather Overview---'])
    myTable.add_row(['1.View my list        '])
    myTable.add_row(['2.Add new city        '])
    myTable.add_row(['3.Edit weather options'])
    myTable.add_row(['4.Delete city         '])
    myTable.add_row(['5.Exit/Quit           '])
    print(myTable)


# data display
def view_data(in_delete):
    print("View my list")
    with open(file, "r") as f:
        temp = json.load(f)
        i = 0
        for city in temp["steden"]:
            naam = city["naam"]
            degrees = city["degrees"]
            windpower = city["windpower"]

            print('\n')
            myTable = PrettyTable([f"Name of city : {naam}"])
            myTable.add_row([f"Index number {i}"])
            myTable.add_row([f"Temerature in degrees : {degrees}"])
            myTable.add_row([f"Power of wind : {windpower}"])
            print(myTable)
            i=i+1

            # print("___________________________")
            # print(f"Index number {i}")
            # print(f"Name of city : {naam}")
            # print(f"Temerature in degrees : {degrees}")
            # print(f"Power of wind : {windpower}")
            # i=i+1

        if in_delete == 0:

            print("\n1.Delete city from my list")
            print("2.back to home menu")
            choise = input("\nWhat would you like to do? \n")

            if choise == "1":
                print("delete city from list")
                delete_data()

            elif choise == "2":
                print("returning")

            else:
                print("\n Not Valid Choice Try again\n")


# delete records
def delete_data():

    print("Please select the number of the city you wish to delete")

    with open(file, "r") as f:
        temp = json.load(f)
        i = 0
        for city in temp["steden"]:
            naam = city["naam"]
            degrees = city["degrees"]
            windpower = city["windpower"]
            i=i+1
            print(i)


# add a new record
def add_data():
    print("\n Add a new city")
    city = input("\n Fill in any city name\n")

    # retrieve weather data from get_data() function
    for weather_data in get_data(city):
        temperature = weather_data
        wind_speed = weather_data

    # write new city to json file using add_new() function
    add_new(city, temperature, wind_speed)
    print(city, 'is added to your list!\n')
    add_more = input("\nWould you like to add another city to the list? [yes/no]")
    if add_more == 'yes':
        add_data()
    elif add_more == 'no':
        print('Returning\n')
    else:
        print('invalid input, returning to menu')


# options for extra weather data
def data_options():
    print("\n Edit weather options")

    #return to menu option
    user_return = input("\nType 'back' to return to home menu")
    if user_return == 'back':
      print('Returning\n')


# return weather data
def get_data(city):
    weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city + ',&appid=630517a862bf4ce229855465a813477d')
    data = weather.text
    parse_json = json.loads(data)
    # print(parse_json)
    temperature = parse_json['main']['temp'] - 273.15
    wind_speed = parse_json['wind']['speed']
    return temperature, wind_speed


# write data to json file
def write_json(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


# appends new city record to json file
def add_new(city, temperature, wind_speed):
    with open("weather.json") as json_file:
        data = json.load(json_file)
        temp = data["steden"]
        new_city = {"naam": city, "degrees": temperature, "windpower": wind_speed}
        temp.append(new_city)

    write_json(data, file)

