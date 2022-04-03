# List comprihenson
# ---------------------------------------------------------------------
# List2 = []
# list1 = [1,2,3]
# sum = 0
# for i in list1:
#     sum = sum + i
#     List2.append(sum)
#
# print(List2)
# ----------------------------------------------------------------------
# we can make this work simpler by list comprehensions

# numbers =[1,2,3]
# list = [n+1 for n in numbers]
# print(list)
# for n in number give n +1 [new_item for item in list]
# -------------------------------------------------------------------------
# double_number = [2*double for double in range(1,5)]
# print(double_number)
# ---------------------------Conditional list comp-----------------------------
# names = ["Priyansh", "Shreyansh", "Kunal", "Krishna", "radheShyam", "KumarAjad"]
#
# FiltList = [name.upper() for name in names if len(name)<8]
# print(FiltList)
# -------------------------------------------------------------------
# challange1 -> Squared list

# numbers = [1, 1, 2, 3, 5, 7 ,8, 12, 15]
# squred_list = [(number * number) for number in numbers]
# print(squred_list)
# -------------------------------------------------------------------------
# challange -> Even list
# numbers = [1, 1, 2, 3, 5, 7 ,8, 12, 15, 18, 20, 21, 23, 43, 44, 55, 66]
#
# even_list = [(num) for num in numbers if (num%2==0)]
# print(even_list)

# ------------------------------------------------------------------------
# Challange3 ->