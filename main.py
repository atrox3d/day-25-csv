import pandas

#
#   read csv into pandas
#
data = pandas.read_csv("data/in/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data.columns)
#
#   get column
#
fur_color = data['Primary Fur Color']
#
#   process count per value
#
squirrels_per_color = fur_color.value_counts()
#
#   print dataframe, dict
#
print(squirrels_per_color)
print(squirrels_per_color.to_dict())
#
#   or
#
# column = data["Primary Fur Color"]
#
#   extract manually for every color
#
gray = data[data["Primary Fur Color"] == "Gray"]
gray_count = len(gray)
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_count = len(cinnamon)
black = data[data["Primary Fur Color"] == "Black"]
black_count = len(black)
print("counts: ", gray_count, cinnamon_count, black_count)
#
#   create dict manually
#
data_dict = {
    "Fur Color": [
        "Gray",
        "Cinnamon",
        "Black",
    ],
    "Count": [
        gray_count,
        cinnamon_count,
        black_count,
    ]
}
print(data_dict)
#
#   create dataframe from dict
#
df = pandas.DataFrame(data_dict)
print(df)
#
#   write to csv
#
df.to_csv("data/out/squirrel_count.csv")
