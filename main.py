# print("hello, world!")
# first = input("Type word:\n")
# first = first.capitalize()
# name = "alex"
# name = name.capitalize()
# phrase = f"{first}, {name}!"
# print(phrase.upper())
# print(name + first)

# a = input("Type word:\n")
# b = "guys"
# b = b.capitalize()
# c = f"{a}, {b}!"
# print(c)
# print(c.upper())
# print(a + b)

# Boolean
# print(10 > 9)
# print(bool(12))

# ===================functions and conditions============

# def check_abilities(drink_age, fuck_age, drive_age):
#     age = int(input("type your age:\n"))
#     sex = input("choose sex M or F:\n").upper()
#     is_married = input("type anything if you are married or leave it empty if you are single:\n")
#     result = []

#     if age >= drink_age and sex == "M":
#         result.append("can drink")
#     else:
#         result.append("cannot drink")

#     if age >= fuck_age and is_married:
#         result.append("can f**k")
#     else:
#         result.append("cannot f**k")

#     if age >= drive_age and ((not is_married and sex == "F") or sex == "M"):
#         result.append("can drive")
#     else:
#         result.append("cannot drive")

#     return result

# list_result = check_abilities(21, 18, 16)
# list_result = map(str.capitalize, list_result)
# string_result = "\n".join(list_result)

# print(string_result)

# ============= build in datatypes ================

# my_list = ["red", "green", "blue", "red"]
# print(list(set(my_list)))
# my_set = {"red", "green", "blue", "red"}
# print(my_set)

# my_tuple = "green", "red", "black"
# my_tuple = ("green", "red", "black")

# my_var1, my_var2, my_var3 = my_tuple
# print(my_var1)
# print(my_tuple[0])

# my_dict = {"color123456": "green", "color123456": "red", "color3": "black"}
# print(my_dict)

# my_dict = {"color1": "green", "color2": "red", "color3": "black"}
# print(my_dict)

# ================ loops ===============

# color_list = ["red", "green", "blue", "red"]
# for item in range(0, len(color_list)):
#     print(color_list[item])
#     color_list[item] = 0

# print(color_list)

# number_sum = 0
# for number in range(0, 1000000):
#     number_sum += number
#     print(number)
# print(number_sum)

# import time
# from time import sleep
# number_sum = 0
# while True:
#     number_sum += 1
#     print(number_sum)
#     sleep(3)

people = [
    {
        "name": "John",
        "age": 36,
        "sex": "M",
        "cars": [
            {
                "model": "Toyota",
                "year": 2024,
                "color": "green",
             },
             {
                "model": "Honda",
                "year": 2023,
                "color": "blue",
             }
        ]
    },
    {
        "name": "Alex",
        "age": 30,
        "sex": "F",
        "cars": [
            {
                "model": "Ford",
                "year": 2024,
                "color": "black",
             },
             {
                "model": "Mazda",
                "year": 2021,
                "color": "white",
             }
        ]
    }
]

name = input("name:\n")
car = input("car:\n")

for person_key in range(0, len(people)):
    if name == people[person_key]["name"]:
        print(people[person_key])
        break
    for car_key in range(0, len(people[person_key]["cars"])):
        if car == people[person_key]["cars"][car_key]["model"]:
            print(people[person_key]["cars"][car_key])
            break