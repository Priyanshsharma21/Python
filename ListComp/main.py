

with open("f1.txt") as file1:
    f1File = file1.readlines()
    list_1 = [int(num.strip()) for num in f1File]
print(list_1)
with open("f2.txt") as file2:
    f2File = file2.readlines()
    list_2 = [int(num.strip()) for num in f2File]
print(list_2)

result = [num for num in list_1 if num in list_2 ]
print(result)

# for num1 in list_1:
#     for num2 in list_2:
#         if num1 == num2:
#             print(num1)
