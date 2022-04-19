import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
# ---------------------------------------------------------------------
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
EMAIL = ""
PASSWORD = ""
# ----------------------------------------------------------------------
response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")
# -------------------------------------------------------------------------
movies_title = soup.select("div h3.title")
movies = [movie.text for movie in movies_title]
movies.reverse()

# with open(file="topMovies.txt",mode="a") as mui:
#     for movie in movies:
#         mui.write(f"{movie}\n")


with SMTP("smtp.gmail.com") as connection:
    connection.starttls();
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs="",
                        msg=f"Subject:Top Movies To Watch: \n\n"
                            f"{movies}")









