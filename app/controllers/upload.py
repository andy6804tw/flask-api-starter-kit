import os, shutil
import app.modules.upload as uploadModule
from flask import Blueprint, request,jsonify


uploadCtrl = Blueprint('upload',__name__)

@uploadCtrl.route('', methods=['GET','POST'])
def uploadFile():
  emptyFolder()
  result=uploadModule.uploadFile(request)
  return result
  

# clear all file in folder
def emptyFolder():
  folder = 'app/static'
  print(len(os.listdir(folder)))
  if len(os.listdir(folder))>=2:
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
