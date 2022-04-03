# dict_name = {new_key:new_value for key in dict}
# dict_name = {new_key:new_value for (key,value) in dict.item}
# dict_name = {new_key:new_value for (key,value) in dict.item if test}

# ex1->
# import random
#
# names = ["Priyansh", "Shreyansh", "Kunal", "Daya", "Michio", "Maki"]
#
# student_dict1 = {student : random.randint(30, 100) for student in names }
# print(student_dict1)
#
# student_dict2 = {student : random.randint(30, 100) for student in names if student[0]=="M"}
# print(student_dict2)
#
# passed_students = {student : marks for (student,marks) in student_dict1.items() if marks >=40}
# print(passed_students)

# ------------------------------------------------------------------------------------

# sentance = "What is the AirSpeed Velocity of an unladen Swallow"
#
# list_of_sentance = sentance.split(" ")
# print(list_of_sentance)
#
# count_of_word = [len(word) for word in list_of_sentance]
# print(count_of_word)
#
# word_dist = {word : len(word) for word in list_of_sentance}
# print(word_dist)

# ---------------------------------------------------------------------------

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day : (temp*1.8+32) for (day,temp) in weather_c.items()}
# print(weather_f)

# -------------------------------------------------------------------------------
# How to iterate to pandas row
import pandas

studant_detail = {
    "Student" : ["Priyansh", "Shreyansh", "Kunal"],
    "Scores" : [90, 89, 87]
}

student_csv = pandas.DataFrame(studant_detail)
print(student_csv)

# to print particular row we can use pandas method iterrow

for (index, row) in student_csv.iterrows():
    print(row)
    print(row.Student)