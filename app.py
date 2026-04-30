# Simple Flask app for CI/CD demo
from flask import Flask

app = Flask(__name__)


# Root route — returns a greeting
@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    # Run the dev server on port 5000
    app.run(host="0.0.0.0", port=5000)
