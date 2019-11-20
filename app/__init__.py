from flask import Flask,request,render_template
from flask_cors import CORS
import config

app = Flask(__name__, static_folder='public')
CORS(app)
app.config.from_object(config)

