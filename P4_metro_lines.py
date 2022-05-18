"""
File:    metro_lines.py
Author:  Gene Ni
Date:    05/07/2022
Section: 25
E-mail:  IL27770@umbc.edu
Description:
"""
USER_INPUT = ">>> "


def create_station(station_name, stations):
    stations[station_name] = []


def connect_stations(first_station, second_station, line_name, stations):
    if line_name in stations[first_station]:
        stations[first_station][line_name].append(second_station)
        stations[second_station][line_name].append(first_station)
    else:
        stations[first_station].append({line_name: [first_station, second_station]})
        stations[second_station].append({line_name: [second_station, first_station]})


def plan_trip(starting_station, ending_station, trip_planner, stations, lines,):
    counter = 0
    if starting_station in trip_planner:
        lines.remove(lines[-1])
        return
    else:
        trip_planner.append(starting_station)

    if starting_station == ending_station:
        print("returning")
        return

    elif len(stations[starting_station]) < 1:
        trip_planner.remove(starting_station)
        lines.remove(lines[-1])

        return

    for line in stations[starting_station]:
        for key in line:
            if ending_station in trip_planner:
                return
            else:
                lines.append(key)
                plan_trip(line[key][1], ending_station, trip_planner, stations, lines)
        counter += 1

        if counter == len(stations[starting_station]) and ending_station not in trip_planner:
            trip_planner.remove(starting_station)
            lines.remove(lines[-1])


def display_trip(trip_planner, lines):
    cnt = 0
    print(f"Start on the {lines[0]}", "-->", end=" ")
    for i in range(len(lines) - 1):
        if i != len(lines):
            if lines[i] == lines[i + 1] and cnt == 0:
                cnt += 1
                print(trip_planner[i], "-->", trip_planner[i + 1], end=" ")
            elif lines[i] == lines[i + 1]:
                print("-->", trip_planner[i + 1], end=" ")
            else:
                print(f"{trip_planner[i]} --> At {trip_planner[i + 1]} transfer from the {lines[i]} line to the "
                      f"{lines[i + 1]} line.", end=" ")
        else:
            print(trip_planner[-1])
            return
    if (len(lines) - 1) == 0:
        # print(trip_planner)
        print(trip_planner[0], "-->", trip_planner[1])
    else:
        print("-->", trip_planner[-1])


def create_train(train_id, line_name, starting_position, trains):
    trains[train_id] = [line_name, starting_position]


def step():
    pass


def display_stations(stations):
    for key in stations:
        print(key)


def display_trains(trains):
    for key in trains:
        print(f"*** Information for Train {key} ***")
        print(f"Line: {trains[key][0]}")
        print(f"Current Position: {trains[key][1]}")


def get_station_info(station_name, stations):
    print(station_name, "Station")
    print(f"Line(s) that run through {station_name} Station: ", end="")
    # print(stations[station_name])
    for i in range(len(stations[station_name])):
        for key in stations[station_name][i]:
            if (i + 1) == len(stations[station_name]):
                print(key)
            else:
                print(f"{key}, ")


def get_train_info(train_id, trains):
    print(f"*** Information for Train {train_id} ***")
    print(f"Line: {trains[train_id][0]}")
    print(f"Current Position: {trains[train_id][1]}")


def exit():
    pass


def metro_station(system):
    trip_planner = []
    lines = []
    trains = {}
    stations = {}

    user_input = answer_prompt(system)
    while user_input != "exit":
        user_split = user_input.split()

        if user_split[0] == "create" and user_split[1] == "station":
            create_station(user_split[2], stations)

        if user_split[0] == "create" and user_split[1] == "train":
            create_train(user_split[2], user_split[3], user_split[4], trains)

        if user_split[0] == "display" and user_split[1] == "stations":
            display_stations(stations)

        if user_split[0] == "display" and user_split[1] == "trains":
            display_trains(trains)

        if user_split[0] == "connect" and user_split[1] == "stations":
            connect_stations(user_split[2], user_split[3], user_split[4], stations)

        if user_split[0] == "get" and user_split[1] == "station" and user_split[2] == "info":
            if user_split[3] in stations:
                get_station_info(user_split[3], stations)
            else:
                print("Invalid Station")

        if user_split[0] == "get" and user_split[1] == "train" and user_split[2] == "info":
            if user_split[3] in trains:
                get_train_info(user_split[3], trains)
            else:
                print("Invalid Train")

        if user_split[0] == "plan" and user_split[1] == "trip":
            plan_trip(user_split[2], user_split[3], trip_planner, stations, lines)
            display_trip(trip_planner, lines)
            trip_planner = []
            lines = []
        user_input = answer_prompt(system)
    print(stations)


def answer_prompt(system):
    user_input = input(f"[{system}] {USER_INPUT}")
    return user_input


if __name__ == '__main__':
    # stations = {
    #     'Greenbelt': [{'Green': ['Greenbelt', 'College-Park']}],
    #     'College-Park': [{'Green': ['College-Park', 'Greenbelt']}, {'Green': ['College-Park', 'Fort-Totten']}],
    #     'Fort-Totten': [{'Green': ['Fort-Totten', 'College-Park']}]}

    # stations = {
    #  'Greenbelt': [{'Green': ['Greenbelt', 'College-Park']}],
    #  'College-Park': [{'Green': ['College-Park', 'Greenbelt']}, {'Green': ['College-Park', 'Fort-Totten']}],
    #  'Fort-Totten': [{'Green': ['Fort-Totten', 'College-Park']}, {'Green': ['Fort-Totten', 'Columbia-Heights']}],
    #  'Columbia-Heights': [{'Green': ['Columbia-Heights', 'Fort-Totten']}]}

    # stations = {
    # 'Greenbelt': [{'Green': ['Greenbelt', 'College-Park']}],
    #  'College-Park': [{'Green': ['College-Park', 'Greenbelt']}, {'Green': ['College-Park', 'Fort-Totten']}],
    #  'Fort-Totten': [{'Green': ['Fort-Totten', 'College-Park']}, {'Green': ['Fort-Totten', 'Columbia-Heights']},
    #                  {'Red': ['Fort-Totten', 'Takoma']}],
    #  'Columbia-Heights': [{'Green': ['Columbia-Heights', 'Fort-Totten']}, {'Green': ['Columbia-Heights', 'U-Street']}],
    #  'Takoma': [{'Red': ['Takoma', 'Fort-Totten']}, {'Red': ['Takoma', 'Silver-Spring']}],
    #  'Silver-Spring': [{'Red': ['Silver-Spring', 'Takoma']}, {'Red': ['Silver-Spring', 'Forest-Glen']}],
    #  'Forest-Glen': [{'Red': ['Forest-Glen', 'Silver-Spring']}],
    #  'U-Street': [{'Green': ['U-Street', 'Columbia-Heights']}, {'Green': ['U-Street', 'Shaw-Howard']}],
    #  'Shaw-Howard': [{'Green': ['Shaw-Howard', 'U-Street']}, {'Green': ['Shaw-Howard', 'Gallery-Place']}],
    #  'Mt-Vernon-Square': [], 'Gallery-Place': [{'Green': ['Gallery-Place', 'Shaw-Howard']}]}
    # trains = {'AB-Train': ['A-B', 'A'], 'AC_Train': ['A-C', 'A'], 'BD-Train': ['B-D', 'D'], 'CD-Train': ['C-D', 'C']}
    # stations = {'A': [{'A-B': ['A', 'B']}, {'A-C': ['A', 'C']}], 'B': [{'A-B': ['B', 'A']}, {'B-D': ['B', 'D']}], 'C': [{'C-D': ['C', 'D']}, {'A-C': ['C', 'A']}], 'D': [{'B-D': ['D', 'B']}, {'C-D': ['D', 'C']}]}

    metro_name = input(USER_INPUT)
    metro_station(metro_name)
