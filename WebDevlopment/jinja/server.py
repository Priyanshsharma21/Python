from flask import Flask, render_template
import random
from datetime import date
import requests
app = Flask(__name__)

URL = 'https://api.agify.io?'

@app.route('/')
def home():
    year = date.today()
    rnum = random.randint(1, 10)
    return render_template("index.html", num=rnum, date=year.year)

@app.route('/guess/<name>')
def idguess(name):
    res = requests.get(f"{URL}name={name}")
    data = res.json()
    return render_template("index.html", name=data["name"], age=data["age"], count=data["count"])

@app.route('/blog/<num>')
def get_blog(num):
    url = 'https://api.npoint.io/c790b4d5cab58020d391'
    res = requests.get(url)
    allPosts = res.json()
    return render_template('blog.html', posts=allPosts)

if __name__ == "__main__":
    app.run(debug=True)