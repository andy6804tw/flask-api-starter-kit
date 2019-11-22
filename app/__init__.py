import config
from flask import Flask,request,render_template
from flask_cors import CORS
from app.controllers.model import model 
from app.controllers.upload import upload, upFile
from flask_uploads import configure_uploads

app=Flask(__name__)
CORS(app)
app.config.from_object(config) # 由config.py管理環境變數
configure_uploads(app, upFile)

app.register_blueprint(model, url_prefix='/model')
app.register_blueprint(upload, url_prefix='/upload')