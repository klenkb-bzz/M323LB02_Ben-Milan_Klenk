from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h2>Portfolio-Flask-App für die LB02 im Modul 323 von Ben-Milan Klenk</h2>"

@app.route("/A1G", methods=["GET"])
def smth():
    return "smth new"

if __name__ == "__main__":
    app.run(debug=True)