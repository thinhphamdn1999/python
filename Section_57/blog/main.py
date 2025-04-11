from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)


@app.route("/")
def home():
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts_response = requests.get(posts_url)
    posts_data = posts_response.json()
    posts = []
    for post in posts_data:
        post_dict = Post(
            title=post["title"],
            body=post["body"],
            subtitle=post["subtitle"],
            id=post["id"],
        )
        posts.append(post_dict)
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    post_url = f"https://api.npoint.io/c790b4d5cab58020d391/{post_id - 1}"
    post_response = requests.get(post_url)
    post_data = post_response.json()
    post_dict = Post(
        id=post_data["id"],
        title=post_data["title"],
        body=post_data["body"],
        subtitle=post_data["subtitle"],
    )
    return render_template("post.html", post=post_dict)


if __name__ == "__main__":
    app.run(debug=True)
