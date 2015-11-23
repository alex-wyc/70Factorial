from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/results")
def results():
    results = ['a', 'b', 'c']
    return render_template('results.html', results)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug = True)
