from flask import Flask
import random

app = Flask(__name__)

def random_number():
    random_number = random.randint(0, 10)
    return random_number


@app.route('/')
def message_logger():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<iframe src="https://giphy.com/embed/eikX1hbwlRkAQR8LAk" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/nails-polish-gel-eikX1hbwlRkAQR8LAk">via GIPHY</a></p>'

@app.route('/<int:number>')
def detect(number):
    random_numbers = random_number()
    if number<random_numbers:
        return '<h1>Little Low</h1>' \
               '<iframe src="https://giphy.com/embed/2A1HVPlfT4SvvMABqq" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/DealorNoDeal-howie-mandel-howiemandel-2A1HVPlfT4SvvMABqq">via GIPHY</a></p>'
    elif number==random_numbers:
        return 'You got the number' \
               '<iframe src="https://giphy.com/embed/9xt5eMX6WhOhvfWajw" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cool-9xt5eMX6WhOhvfWajw">via GIPHY</a></p>'
    else:
        return '<h1>Little high</h1>' \
               '<iframe src="https://giphy.com/embed/PR3585ZZSvcHO9pa76" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/abcnetwork-abc-joel-mchale-card-sharks-PR3585ZZSvcHO9pa76">via GIPHY</a></p>'






if __name__== "__main__":
    app.run(debug=True)