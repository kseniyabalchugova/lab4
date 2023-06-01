from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def calculate():
    shape = request.form["shape"]
    if shape == "cube":
        side = float(request.form["side"])
        volume = side ** 3
    elif shape == "sphere":
        radius = float(request.form["radius"])
        volume = (4/3) * 3.14 * radius ** 3
    elif shape == "cylinder":
        radius = float(request.form["radius"])
        height = float(request.form["height"])
        volume = 3.14 * radius ** 2 * height
    elif shape == "cone":
        radius = float(request.form["radius"])
        height = float(request.form["height"])
        volume = (1/3) * 3.14 * radius ** 2 * height
    return render_template("result.html", volume=volume)

if __name__ == "__main__":
    app.run(debug=True)
