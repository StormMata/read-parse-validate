# ---------------------------------------------
# import package to read json
# ---------------------------------------------

# import json
# import math

# # ---------------------------------------------
# #  write function to load file and parse json
# # ---------------------------------------------

# def readJson(file):
#     with open(file) as p:
#         return json.load(p)

# # ---------------------------------------------
# #  call 'readJson', load salaries
# # ---------------------------------------------

# salaries = readJson('./data.json')
# print(salaries)

# # ---------------------------------------------
# #  print all salaries
# # ---------------------------------------------

# for salary in salaries['data']:
#     print(salary[18])

# # ---------------------------------------------
# # loop through list, only print salary field
# # ---------------------------------------------


# # ---------------------------------------------
# #  add all salaries
# # ---------------------------------------------

# for salary in salaries['data']:
#     salary = float(salary[18])

# total = sum(salary)

# print(total)

from faker import Faker
import random
fake = Faker()

for x in range(50):
    print(fake.isbn10())