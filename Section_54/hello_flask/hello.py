# from flask import Flask

# def make_bold(f):
#     def wrapper(*args, **kwargs):
#         return f"<b>{f(*args, **kwargs)}</b>"
#     return wrapper
# def make_italic(f):
#     def wrapper(*args, **kwargs):
#         return f"<i>{f(*args, **kwargs)}</i>"
#     return wrapper
# def make_underline(f):
#     def wrapper(*args, **kwargs):
#         return f"<u>{f(*args, **kwargs)}</u>"
#     return wrapper

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# @app.route("/<username>")
# def hello_name(username):
#     return f"<p>Hello, {username}!</p>"

# @app.route("/bye")
# @make_bold
# @make_italic
# @make_underline
# def bye():
#     return "<p>Bye!</p>"


# if __name__ == "__main__":
#     app.run(debug=True)


def logging_decorator(f):
    def wrapper(*args):
        print(f"You called {f.__name__}{args}")
        print(f"It returned: {f(*args)}")
        return f(*args)

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
