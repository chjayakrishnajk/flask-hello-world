from flask import Flask

app = Flask(__name__)

status = "Ntg"

@app.route('/')
def home():
    status == "Yes"
    return status
@app.route('/no')
def no():
    status == "No"
    return status
@app.route('/status')
def status():
    return status
@app.route('/about')
def about():
    return 'About'
