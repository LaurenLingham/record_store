from flask import Flask, render_template

from controllers.store_controller import albums_blueprint

app = Flask(__name__)

app.register_blueprint(albums_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
