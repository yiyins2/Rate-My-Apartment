from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the home page.'

@app.route('/tuna')
def tune():
    return '<h2>Tuna is good</h2>'

@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hey there %s<h2>" % username

@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2>Post ID is %s<h2>" % post_id

if __name__=="__main__":
    app.run()
