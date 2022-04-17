from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def data_recived():
    error = None
    if request.method == 'POST':
        name = request.form["name"]
        roll = request.form["roll"]
        email = request.form["email"]
        dob = request.form["dob"]
        print(f"{name}, {roll}, {email}, {dob}")

    return render_template('index.html', error=error)







if __name__=="__main__":
    app.run()