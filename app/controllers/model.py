from flask import Blueprint, request,jsonify,redirect
import app.modules.model1 as model1

model = Blueprint('model',__name__)
  

@model.route('', methods=['GET'])
def getResult():
    return model1.getResult()
  
