from flask import Flask, render_template

app = Flask(__name__)

all_posts = [ 
    { 'title' : 'Post 1' , 'author' : 'Nilesh Indore', 'containt' : 'This is a containt of post 1'},
    { 'title' : 'Post 2' , 'containt' : 'This is a containt of post 2'}
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/allposts')
def post():
    return render_template('post.html',posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
