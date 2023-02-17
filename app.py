from flask import Flask, render_template

from controllers.store_controller import albums_blueprint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
