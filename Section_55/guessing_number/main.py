from flask import Flask
from number import RandomNumber

MIN_VALUE = 0
MAX_VALUE = 9

app = Flask(__name__)
random_number = RandomNumber(MIN_VALUE, MAX_VALUE)


@app.route("/")
def create_guess_number():
    random_number.generate()
    return (
        f"<h1>Guess a number between {MIN_VALUE} and {MAX_VALUE}</h1>"
        f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='guessing'/>"
    )


@app.route("/<int:guess>")
def guess_number(guess):
    if random_number.number == guess:
        return (
            f"<h1 style='color:green'>You guessed it right! The number was {random_number.number}.</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='guessing'/>"
        )
    elif random_number.number > guess:
        return (
            "<h1 style='color:red'>Too low! Try again.</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='guessing'/>"
        )
    else:
        return (
            "<h1 style='color:blue'>Too high! Try again.</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='guessing'/>"
        )

if __name__ == "__main__":
    app.run(debug=True)
