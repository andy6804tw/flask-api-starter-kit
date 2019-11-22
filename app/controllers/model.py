from flask import Blueprint, request,jsonify,redirect

model = Blueprint('model',__name__)
  

@model.route('', methods=['GET'])
def getModel():
    return "<h1>Hello Flasddddk!</h1>"
  
