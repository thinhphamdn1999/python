from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 100)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>", methods=["GET"])
def guess(name):
    params = {"name": name}
    
    agify_url = "https://api.agify.io"
    agify_response = requests.get(agify_url, params=params)
    age = agify_response.json().get("age")

    genderize_url = "https://api.genderize.io"
    genderize_response = requests.get(genderize_url, params=params)
    gender = genderize_response.json().get("gender")

    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_response.raise_for_status()  # Check for request errors
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
