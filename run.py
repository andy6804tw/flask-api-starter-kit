from app import app
import cv2
import config

@app.route('/')
def index():
  return '1server started on '+str(config.PORT)+' PORT '+str(config.ENV)

if __name__ == '__main__':
  # print(app.url_map)
  # @app.route('/')
  # def index():
  #   return 'server started on '+str(config.PORT)+' PORT '+str(config.ENV)
  app.run(port=config.PORT)
