from flask import Flask, render_template, request
import util

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
    # TODO this is where one uses backend for loading stuff
    # NOTE that the method SHOULD BE GET
    return

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug = True)
