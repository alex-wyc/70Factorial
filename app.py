from flask import Flask, render_template, request
import util

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def root():
    if request.method == "GET":
        return render_template('index.html')
    else:
        query = request.form['sumName']
        #results = 
        return render_template('results.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug = True)
