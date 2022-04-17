from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapperFunction():
        return "<strong>" + function() + "<strong>"
    return wrapperFunction

def make_italic(function):
    def wrapperFunction():
        return "<em>" + function() + "<em>"
    return wrapperFunction

def make_underline(function):
    def wrapperFunction():
        return "<u>" + function() + "<u>"
    return wrapperFunction


@app.route('/')
@make_bold
@make_italic
@make_underline
def hello_world():
    return 'Hello, World!'


@app.route('/user/<name>/<int:number>')
def greet(name, number):
    return f"<h1>Hello {name} and {number}</h1> <input placeholder='name' />"


# @app.route('/secrets/ <path :secret>')
# def greet(secret):
#     return f"{secret}"

if __name__ == "__main__":
    app.run(debug=True)  # Dbug mode on
