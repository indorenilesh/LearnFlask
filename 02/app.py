from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello !!!"

@app.route('/string/<string:name>')
def char(name):
    return "Hello "+name+" !!!"

@app.route('/int/<int:id>')
def number(id):
    return "Hello "+str(id)+" !!!"

@app.route('/<string:user>/post/<int:postid>')
def post(user,postid):
    return "This is " + user + " user and post number is " + str(postid) 

if __name__ == "__main__":
    app.run(debug=True)
