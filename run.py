# from app import app
from flask import *

app = Flask(__name__)
import config
if __name__ == '__main__':
  # print(app.url_map)
  @app.route('/')
  def index():
    # return 'server started on '+str(config.PORT)+' PORT '+str(config.ENV)
    return'sadsadsad'
  # app.run(port=config.PORT)
  app.run(debug=True)
