
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My app is live on Render 🚀"

if __name__ == "__main__":
    app.run()
``
