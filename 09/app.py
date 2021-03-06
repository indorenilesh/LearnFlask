from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  

    def __repr__(self):
        return "Blog post " + str(self.id)

all_posts = [ 
    { 'title' : 'Post 1' , 'author' : 'Nilesh Indore', 'containt' : 'This is a containt of post 1'},
    { 'title' : 'Post 2' , 'containt' : 'This is a containt of post 2'}
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title,author=post_author,content=post_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/post')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('post.html',posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
