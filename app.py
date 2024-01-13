import os

from flask import Flask

from routes import blueprints


app = Flask(__name__, static_folder="static")

for blueprint, url in blueprints:
    app.register_blueprint(blueprint, url_prefix=url)

if __name__ == "__main__":
    tmp = "tmp"
    if not os.path.isdir(tmp):
        if os.path.exists(tmp):
            os.remove(tmp)
        os.mkdir(tmp)

    app.run(host="localhost", port=9000, debug=True)
