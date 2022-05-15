"""
File:    metro_lines.py
Author:  Gene Ni
Date:    05/07/2022
Section: 25
E-mail:  IL27770@umbc.edu
Description:

"""
USER_INPUT = ">>> "


def create_station(station_name):
    stations[station_name] = []


def connect_stations(first_station, second_station, line_name):
    pass


def plan_trip(starting_station, ending_station):
    pass


def create_train(train_id, line_name, starting_position):
    trains[train_id] = [line_name, starting_position]


def step():
    pass


def display_stations():
    for key in stations:
        print(key)


def display_trains():
    for key in trains:
        print(f"*** Information for Train {key} ***")
        print(f"Line: {trains[key][0]}")
        print(f"Current Position: {trains[key][1]}")


def get_station_info(station_name):
    pass


def get_train_info(train_id):
    pass


def exit():
    pass


def metro_station(system):
    user_input = answer_prompt(system)

    while user_input != "quit":
        user_split = user_input.split()

        if user_split[0] == "create" and user_split[1] == "station":
            create_station(user_split[2])

        if user_split[0] == "create" and user_split[1] == "train":
            create_train(user_split[2], user_split[3], user_split[4])

        if user_split[0] == "display" and user_split[1] == "stations":
            display_stations()

        if user_split[0] == "display" and user_split[1] == "trains":
            display_trains()

        user_input = answer_prompt(system)


def answer_prompt(system):
    user_input = input(f"[{system}] {USER_INPUT}")
    return user_input


if __name__ == '__main__':
    stations = {}
    trains = {}
    metro_name = input(USER_INPUT)
    metro_station(metro_name)
