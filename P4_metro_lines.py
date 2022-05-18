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
    stations[first_station].append({line_name: [first_station, second_station]})
    possible_stations[first_station].append({line_name: [first_station, second_station]})


def plan_trip(starting_station, ending_station):
    counter = 0
    trip_planner.append(starting_station)
    print(trip_planner)

    if starting_station == ending_station:
        # completed_trip = trip_planner
        return

    elif len(stations[starting_station]) == 0:
        # print(f"Removing {starting_station}")
        trip_planner.remove(starting_station)
        return

    # elif len(stations[starting_station]) == 0

    for line in stations[starting_station]:
        # print(line, "line")
        for key in line:
            # print(line[key][1])
            if ending_station in trip_planner:
                return
            else:
                plan_trip(line[key][1], ending_station)
        counter += 1
        # print(counter, starting_station)
        if counter == len(stations[starting_station]) and ending_station not in trip_planner:
            trip_planner.remove(starting_station)

    # stations = {
    # 'A': [{'A-B': ['A', 'B']}, {'A-C': ['A', 'C']}],
    # 'B': [{'B-D': ['B', 'D']}],
    # 'C': [{'C-D': ['C', 'D']}, {'C-E': ['C', 'E']}],
    # 'D': [],
    # 'E': []
    # }


def display_trip():
    is_there_train = False
    if len(trains) > 0:
        is_there_train = True

    print("Start on the")
    # for i in range(len(trip_planner)):
    #     if


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


# def get_station_info(station_name):
#     pass
#
#
# def get_train_info(train_id):
#     pass
#
#
# def exit():
#     pass


def metro_station(system):
    user_input = answer_prompt(system)
    while user_input != "exit":
        user_split = user_input.split()

        if user_split[0] == "create" and user_split[1] == "station":
            create_station(user_split[2])

        if user_split[0] == "create" and user_split[1] == "train":
            create_train(user_split[2], user_split[3], user_split[4])

        if user_split[0] == "display" and user_split[1] == "stations":
            display_stations()

        if user_split[0] == "display" and user_split[1] == "trains":
            display_trains()

        if user_split[0] == "connect" and user_split[1] == "stations":
            connect_stations(user_split[2], user_split[3], user_split[4])

        if user_split[0] == "plan" and user_split[1] == "trip":
            plan_trip(user_split[2], user_split[3])
            print(trip_planner)
            display_trip()
            # trip_planner = []
        user_input = answer_prompt(system)

    print(stations)
    print(trains)
    print(len(stations))


def answer_prompt(system):
    user_input = input(f"[{system}] {USER_INPUT}")
    return user_input


if __name__ == '__main__':
    trip_planner = []
    completed_trip = []
    stations = {
    'A': [{'A-B': ['A', 'B']}, {'A-C': ['A', 'C']}],
    'B': [{'B-D': ['B', 'D']}],
    'C': [{'C-D': ['C', 'D']}, {'C-E': ['C', 'E']}],
    'D': [{'D-F': ['D', 'F']}, {'D-G': ['D', 'G']}],
    'E': [],
    'F': [],
    'G': []
    }
    possible_stations = {'A': [{'A-B': ['A', 'B']}, {'A-C': ['A', 'C']}], 'B': [{'B-D': ['B', 'D']}],
                'C': [{'C-D': ['C', 'D']}, {'B-E': ['B', 'E']}], 'D': [], 'E': []}
    trains = {'AB-Train': ['A-B', 'A'], 'AC_Train': ['A-C', 'A'], 'BD-Train': ['B-D', 'D'], 'CD-Train': ['C-D', 'C']}
    # metro_name = input(USER_INPUT)
    metro_station("Alphabet System")
