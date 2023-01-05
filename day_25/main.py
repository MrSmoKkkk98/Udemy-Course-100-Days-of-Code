import pandas

# data = pandas.read_csv("day_25\weather_data.csv")
# print(type(data))
# temp_list = data["temp"].to_list()
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# to_fahrenheit = int(monday.temp) * 1.8 + 32
# print(to_fahrenheit)  

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
print(data_dict)
data = pandas.DataFrame(data_dict)
data.to_csv("day_25/new_data.csv")
print(data)

data = pandas.read_csv("day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_data = data["Primary Fur Color"].to_list()
all_squirrels = {}
for color in color_data:
    squirrel_color = []
    squirrel_count = []
    if color == "Gray":
        grey_color_count = color_data.count("Gray")
    elif color == "Cinnamon":
        red_color_count = color_data.count("Cinnamon")
    elif color == "Black":
        black_color_count = color_data.count("Black")
squirrel_color.append("grey")
squirrel_color.append("red")
squirrel_color.append("black")
squirrel_count.append(grey_color_count)
squirrel_count.append(red_color_count)
squirrel_count.append(black_color_count)

all_squirrels["Fun Color"] = squirrel_color
all_squirrels["Count"] = squirrel_count

data = pandas.DataFrame(all_squirrels)
data.to_csv("day_25/squirrel_count.csv")
 