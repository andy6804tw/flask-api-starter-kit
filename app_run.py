from flask import *
from datetime import datetime
from dbModel import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    return "Deploying a Flask App To Heroku"



if __name__ == '__main__':
    app.run(debug=True)