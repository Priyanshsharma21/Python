# we can use pip install flask
from flask import Flask
app = Flask(__name__)
 # name here tells us the name of the file module

# @app is a decorator function gives additional functionality to existing function
# we treet function as first class args -> means we can treet them as any other argument and pass them as args

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()


