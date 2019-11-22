from flask import Blueprint, request,jsonify,redirect
import app.modules.data as dataModule

dataCtrl = Blueprint('data',__name__)
  

@dataCtrl.route('', methods=['GET'])
def getResult():
    return dataModule.getResult()
  
