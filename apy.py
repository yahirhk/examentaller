from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("examen.html")

if __name__ == "__main__":
    app.run(port=4000, host="0.0.0.0")
