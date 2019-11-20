from app import app

if __name__ == '__main__':
  print(app.url_map)
  app.run(port=5009)
