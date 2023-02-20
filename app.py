from flask import Flask, render_template

from controllers.album_controller import albums_blueprint
from controllers.artist_controller import artists_blueprint

app = Flask(__name__)

app.register_blueprint(albums_blueprint)
app.register_blueprint(artists_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
