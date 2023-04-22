from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
return render_template('index.html')
@app.route('/')
def welcome_world():
    return render_template('welcome.html')