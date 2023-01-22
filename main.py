CSV_WEATHER_FILE = "weather_data.csv"

import csv
import pandas


def read_file_standard(name):
    with open(name) as data_file:
        lines = []
        for line in data_file.readlines():
            line = line.replace("\n", "").strip()
            lines.append(line)

        return lines


def read_temp_from_csv():
    with open(CSV_WEATHER_FILE) as data_file:
        data = csv.reader(data_file)
        temperature = []
        for row in data:
            if (row[1]).isdigit():
                temperature.append(int(row[1]))

        print(temperature)


def panda_read_csv():
    data = pandas.read_csv(CSV_WEATHER_FILE)
    print(data["temp"])

    print(f"\nType of data: {type(data)}\nType of temp: {type(data['temp'])}")


def panda_additional_funtions():
    data = pandas.read_csv(CSV_WEATHER_FILE)
    panda_dict = data.to_dict();
    print(panda_dict)
    temp_list = data["temp"].tolist()
    print(temp_list)
    print(f"\nMax value of series: {round(data['temp'].max(), 2)}")
    print(f"Min value of series: {round(data['temp'].min(), 2)}")
    print(f"Mean value of series: {round(data['temp'].mean(), 2)}")
    print(f"\nAvarage temp, calculated: {round(sum(temp_list) / len(temp_list), 2)}\n")

    print(f"We can specify the column as an attribute:\n{data.condition}")

    print("\nPrint a day\n")
    print(data[data.day == " Monday"])

    print("\nPrint hottest day\n")
    hottest_day = data[data.temp == data.temp.max()];
    print(hottest_day)
    highest_temp_F = round(int(hottest_day.temp) * 9 / 5 + 32, 2)
    print(f"{int(hottest_day.temp)} C = {highest_temp_F} F")


def squirrel_data():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    fur_color = data["Primary Fur Color"]
    unique_colors = []
    for color in fur_color.dropna().unique():
          unique_colors.append(color)
    colors_list = []
    colors_count = []
    for color in unique_colors:
        colors_list.append(color)
        colors_count.append(fur_color[data["Primary Fur Color"] == color].count())

    color_dict = {"color": colors_list, "count" : colors_count}
    print(color_dict)
    print("\n")

    colors_frame = pandas.DataFrame.from_dict(color_dict);
    print(colors_frame)
    colors_frame.to_csv("colors.csv")


# print(read_file_standard(CSV_WEATHER_FILE))
# read_temp_from_csv()
# panda_read_csv()
# panda_additional_funtions()
squirrel_data()
