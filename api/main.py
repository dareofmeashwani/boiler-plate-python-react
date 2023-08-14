from flask import Flask, send_from_directory
import config


app = Flask(__name__, static_folder='../ui/build')
app.config['ENV'] = config.ENV

@app.route('/', defaults={'path':'index.html'})
@app.route('/<path:path>')
def serve_static(path):
  return send_from_directory(app.static_folder, path)


@app.route('/api/v1/healthz')
def healthz():
  return "OK"

if __name__ == '__main__':
  app.run(port=config.PORT, debug=config.DEBUG)