# height = int(input("ENter your height"))
# weight = int(input("Enter your weight"))
#
# if height>3:
#     raise ValueError("Mazak Matt kar bhai, height sahi dal chal")
# else:
#     bmi = weight / height **2
#     print(bmi)
#
#
    # ----------------------Index error---------------#

# exercis1
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)

# -----------------------------Key error---------------------------------------
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        print(f"No 'Like' key Found in {post}")
        pass




print(total_likes)