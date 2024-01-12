from flask import Flask

from routes import blueprints


app = Flask(__name__)

for blueprint, url in blueprints:
    app.register_blueprint(blueprint, url_prefix=url)

if __name__ == "__main__":
    app.run(host="localhost", port=9000)
