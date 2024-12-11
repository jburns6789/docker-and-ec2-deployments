from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/languages")
def languages():
    return render_template('languages.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

#jsonify
# @app.route("/data")
# def get_data():
#     data = {
#         'message': 'Hello from Flask API!'
#     }
#     return jsonify(data)

if __name__ == "__main__":
    # Updated to listen on all interfaces
    app.run(host="0.0.0.0", port=5005, debug=True)
