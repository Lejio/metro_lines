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


def plan_trip(starting_station, ending_station):
    trip_planner.append(starting_station)

    if starting_station == ending_station:
        return

    elif len(stations[starting_station]) == 0:
        trip_planner.remove(starting_station)

    for line in stations[starting_station]:
        for key in line:
            if ending_station in trip_planner:
                return
            else:
                plan_trip(line[key][1], ending_station)


def display_trip():
    is_there_train = False
    if len(trains) > 0:
        is_there_train = True

    print("Start on ")

    # for station in trip_planner:
    #     for i in range(len(stations[station])):
    #         for key in stations[station][i]:
    #             if stations[station][i][key][0] == station:
    #                 print(stations[station][i][key][0])
    #                 print(key)
    # print("")
    # print("")

    # print(trip_planner)
    # for i in range(len(trip_planner)):
    #     print(trip_planner[i])
    #     for dict in stations[trip_planner[i]]:
    #         print(dict)

    # for j in range(len(stations[trip_planner[i]])):
    #     print(len(stations[trip_planner[i]]), trip_planner[i])


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

        if user_split[0] == "connect" and user_split[1] == "stations":
            connect_stations(user_split[2], user_split[3], user_split[4])

        if user_split[0] == "plan" and user_split[1] == "trip":
            plan_trip(user_split[2], user_split[3])
            display_trip()
        user_input = answer_prompt(system)

    print(stations)
    print(trains)


def answer_prompt(system):
    user_input = input(f"[{system}] {USER_INPUT}")
    return user_input


if __name__ == '__main__':
    trip_planner = []
    stations = {'A': [{'A-B': ['A', 'B']}, {'A-C': ['A', 'C']}], 'B': [{'B-D': ['B', 'D']}, {'B-E': ['B', 'E']}],
                'C': [{'C-D': ['C', 'D']}], 'D': [], 'E': []}
    trains = {'AB-Train': ['A-B', 'A'], 'AC_Train': ['A-C', 'A'], 'BD-Train': ['B-D', 'D'], 'CD-Train': ['C-D', 'C']}
    # metro_name = input(USER_INPUT)
    metro_station("Alphabet System")
