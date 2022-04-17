from bs4 import BeautifulSoup


with open("index.html", encoding="utf-8") as data:
    html = data.read()

# object of soup
soup = BeautifulSoup(html, "html.parser")

# -------------------Tags--------------------------------
# print(soup.prettify()) # Whole Html
# print(soup.title) # title tag
# print(soup.a)
# print(soup.a.string) # text inside

a_tags = soup.find_all(name="a")

for tag in a_tags:
    print(tag.get_text())
    print(tag.get("href"))

# -----------------------------------------------------------
# id
heading = soup.find(name="h1", id="name")
print(heading)

# class
heading2 = soup.find(name="h3", class_="heading")
print(heading2.text)
# -------------------------------------------------------------
# selector
company_url = soup.select_one(selector="p a")

# selector h1 with heading class
head = soup.select_one("h1#name")
print(head.text)

head = soup.select_one("h3.heading")
print(head.text)


