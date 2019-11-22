from app import app
import config
if __name__ == '__main__':
  print(app.url_map)
  @app.route('/')
  def index():
      return 'server'
  app.run(port=config.PORT)
