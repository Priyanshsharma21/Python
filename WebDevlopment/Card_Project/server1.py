from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)



# Tips ->
# html5up.com
# use -> document.body.contentEditable = true