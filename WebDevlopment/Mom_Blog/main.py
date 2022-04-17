from flask import Flask,render_template,request
import requests
from smtplib import SMTP

EMAIL = "piyuindia220@gmail.com"
PASSWORD = "Piyu@412002"

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form['username']
    email = request.form['email']
    phno = request.form['phno']
    message = request.form['message']
    send_email(name,email,phno,message)

    return "Successfully message send"

def send_email(name,email,phno,message):
    message = f"Name : {name}\n Email: {email}\n Contact Number : {phno}\n Message: {message}"
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="piyuindia4@gmail.com",
                            msg=f"Subject: New User On Blog \n\n {message}")


if __name__=="__main__":
    app.run(debug=True)