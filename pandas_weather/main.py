# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(data)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_temp = data["temp"]
print(temp_temp.mean())
# print(sum(temp_temp)/len(temp_temp))