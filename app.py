from flask import Flask
import util

app = Flask(__name__)

@app.route("/")
def root():
    return ""

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug = True)
