from bs4 import BeautifulSoup
import requests
from smtplib import SMTP

URL = "https://news.ycombinator.com/"
EMAIL = ""
PASSWORD = ""

res = requests.get(URL)
html = res.text


soup = BeautifulSoup(html, "html.parser")
print(soup.title.string)

all_articles_text = []
all_articles_link = []

articles = soup.select("td a.titlelink")
upvotes = soup.select(".score")

for article in articles:
    text = article.text
    link = article.get("href")

    all_articles_text.append(text)
    all_articles_link.append(link)


all_upvote = [int(vote.get_text().split(" ")[0]) for vote in upvotes]
largest_num = max(all_upvote)
index_of_largest_vote = all_upvote.index(largest_num)

popular_article = all_articles_text[index_of_largest_vote]
link_of_popular_article = all_articles_link[index_of_largest_vote]

print(popular_article)
print(link_of_popular_article)

with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs="",
                        msg=f"Subject:Most popular article(Hacker News)\n\n"
                            f"{popular_article}\n{link_of_popular_article}")

