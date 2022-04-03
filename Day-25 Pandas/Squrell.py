import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sqr_count = len(data[data["Primary Fur Color"] == "Gray"])
black_sqr = len(data[data["Primary Fur Color"] == "Black"])
cinn_sqr = len(data[data["Primary Fur Color"] == "Cinnamon"])



data_dist = {
    "fur_qur": ["Gray", "Black", "Cinammon"],
    "count" : [gray_sqr_count, black_sqr,cinn_sqr]
}

df= pandas.DataFrame(data_dist)
df.to_csv("Sqr_count.csv")