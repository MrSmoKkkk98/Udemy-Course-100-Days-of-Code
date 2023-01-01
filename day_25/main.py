import pandas

data = pandas.read_csv("day_25\weather_data.csv")
print(type(data))
temp_list = data["temp"].to_list()
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
to_fahrenheit = int(monday.temp) * 1.8 + 32
print(to_fahrenheit)  

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
data.to_csv("day_25/new_data.csv")
print(data)