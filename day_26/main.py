# Exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# Exercise 2
result = [num for num in numbers if num % 2 == 0]
print(result)

# Exercise 3
file_1 = open("day_26/file1.txt", "r")
numbers_1 = file_1.readlines()
file_2 = open("day_26/file2.txt", "r")
numbers_2 = file_2.readlines()
result = [int(num) for num in numbers_1 if num in numbers_2]
print(result)

# Exercise 4
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {}
# for word in sentence.split():
#     sentence[word] = [len(word)]
#     print(result)
result = {word: len(word) for word in sentence.split()}
print(result)

# Exercise 5
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# weather_f = {}
# for items in weather_c.items():
#     weather_f[items[0]] = (items[1] * 9/5) + 32
# print(weather_f)

weather_f = {item[0]: (item[1] * 9/5) + 32 for item in weather_c.items()}
print(weather_f)
