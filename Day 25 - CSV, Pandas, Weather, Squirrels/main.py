# import csv
import pandas
# # with open("weather_data.csv") as weather_data:
# #     weather_list = csv.reader(weather_data)
# #     temperatures = []
# #     int_temperatures = []
# #     for row in weather_list:
# #         temperatures.append(row[1])
# # for num in range(1, 7):
# #     int_temp = temperatures[num]
# #     int_temperatures.append(int_temp)
# #
# # print(int_temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # temp_list = data["temp"]
# # sum = sum(temp_list)
# # average = sum / len(temp_list)
# # print(average)
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# mon_temp = int(monday.temp)
# print((mon_temp * (9/5)) + 32)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = data["Primary Fur Color"] == "Gray"
print(gray.sum())
cinnamon = data["Primary Fur Color"] == "Cinnamon"
print(cinnamon.sum())
black = data["Primary Fur Color"] == "Black"
print(black.sum())
squirrel_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[gray.sum(), cinnamon.sum(), black.sum()]
}

pan_squirrel_dict = pandas.DataFrame(squirrel_dict)
print(pan_squirrel_dict)