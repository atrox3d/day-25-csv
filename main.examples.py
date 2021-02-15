# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
# print(data)

import pandas

data = pandas.read_csv("data/in/weather_data.csv")
print(data)
print(data["temp"])

print(data.to_dict())
print(data["temp"].to_list())

print(data["temp"].mean())
print(data["temp"].max())

print(data.temp.mean())
print(data.temp.max())

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

print(data[data.day == "Monday"].condition)

data_dict = {
    "students": ["rob", "fab"],
    "scores": [50, 60]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("data/out/new_data.csv")





