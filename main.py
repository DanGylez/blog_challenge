from flask import Flask, render_template
import requests

app = Flask(__name__)


def fetch_posts():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    return response.json()


@app.route('/')
def home():
    all_posts = fetch_posts()
    return render_template("index.html", posts=all_posts)


@app.route('/entry/<index>')
def get_entry(index):
    all_posts = fetch_posts()
    return render_template("post.html", post=all_posts[int(index)])


if __name__ == "__main__":
    app.run(debug=True)
