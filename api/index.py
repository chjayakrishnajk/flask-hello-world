from flask import Flask

app = Flask(__name__)

status = "Ntg"

@app.route('/')
def home():
    if(status == "Ntg"):
        status == "Yes"
    return status
@app.route('/no')
def home():
    status == "No"
    return status
@app.route('/status')
def home():
    return status
@app.route('/about')
def about():
    return 'About'
