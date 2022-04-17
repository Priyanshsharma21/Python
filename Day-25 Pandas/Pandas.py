# Analysing data with pandas
# Commas seprated values(CSV)

# with open("./weather_data.csv") as data:
#     all_data = data.readlines()
#     print(all_data)

# or

# import csv
# with open("./weather_data.csv") as data:
#     all_data = csv.reader(data)
#     temprature = []
#
#     for row in all_data:
#         for col in all_data:
#             temprature.append(int(col[1]))
#         print(temprature)
# or

import pandas
data = pandas.read_csv("./weather_data.csv")
print(data["temp"])
# we can also use . notation for the same
print(data.condition)
# print particular row
row = (data[data.day=='Monday'])
print(row)



# Pandas have two types of data types
# 1. Data Frame -> 'All' the data in excel sheet is considet it
# 2. Series -> A particular column like temp in our example

# opration on data frames
# csv to dictonary
myDist = data.to_dict()
print(myDist)

# to html
myDist = data.to_html
print(myDist)

# oprqation on seriues
temp_series = data["temp"]
list_of_temp = temp_series.tolist()

print(temp_series.mean())
print(temp_series.max())

# avg = sum(list_of_temp)/ len(list_of_temp)
# print(avg)

# or

# avg_of_temp = 0
# count = 0
# for temp in list_of_temp:
#     avg_of_temp += temp
#     count +=1
#
# average = avg_of_temp/count
# print(average)

# max row data temp must be max

print(data)
max_temp = data["temp"].max()
max_temp_row = (data[data.temp == max_temp])
print(max_temp_row)

# So when we fill [] with a condition we get row

monday = (data[data.day=="Monday"])
monday_temp = int(monday.temp)
monday_temp_in_f = monday_temp + 9/5 + 32
print(monday_temp_in_f)

# create a dtaFrame

student_dist = {
    "name" : ["Priyansh", "shrayensh", "Kunal"],
    "age" : [20, 16, 17]
}

new_table = pandas.DataFrame(student_dist)
new_table.to_csv("Student.csv")
print(new_table)