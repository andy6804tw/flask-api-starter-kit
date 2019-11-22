
def uploadFile(request):
    if request.method == 'POST' and 'videoFile'  in request.files:
      videoName=request.form['fileName']
      request.files['videoFile'].filename=videoName
      filename = upFile.save(request.files['videoFile'])
      # file_url = upFile.url(filename)
      return 'don'
    elif request.method == 'POST' and 'imageFile'  in request.files:
      imageName=request.form['fileName']
      request.files['imageFile'].filename=imageName
      filename = upFile.save(request.files['imageFile'])
      # file_url = upFile.url(filename)
      return 'don'
    else:
      return 'error'
