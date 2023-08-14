from flask import send_from_directory # Remove: import Flask
import connexion
import config

app = connexion.App(__name__, specification_dir="./specs/", server_args={'static_folder': './../ui/build'})
app.add_api("openapi.yaml")
app.app.config['ENV'] = config.ENV

@app.route('/', defaults={'path':'index.html'})
@app.route('/<path:path>')
def serve_static(path):
  return send_from_directory(app.app.static_folder, path)

if __name__ == '__main__':
  app.run(port=config.PORT, debug=config.DEBUG)