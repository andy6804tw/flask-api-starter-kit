from flask import Flask
from flask import render_template

app = Flask(__name__)
# set the absolute path to the static folder
app.static_folder= 'public/'

if __name__ == '__main__':
    app.debug=True
    app.run()