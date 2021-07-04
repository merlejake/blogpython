from flask import Flask, render_template
from post import Post
import requests

BLOG_ENDPOINT = 'https://api.npoint.io/e42b353ee387383898c7'
post_data = requests.get(url=BLOG_ENDPOINT).json()
post_objs = []

for posts in post_data:
    new_post = Post(blog_id=posts['id'], body=posts['body'], date=posts['date'], image=posts['image'], title=posts['title'], author=posts['author'],
                    subtitle=posts['subtitle'])
    post_objs.append(new_post)

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html', posts=post_data)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post_page(post_id):
    print()
    for current_post in post_objs:
        if current_post.id == post_id:
            return render_template('post.html', post=current_post)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000,
        host='127.0.0.1'
    )
