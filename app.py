from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        h = int(request.form.get("hours"))
        m = int(request.form.get("minutes"))
        s = int(request.form.get("seconds"))

        total_seconds = h * 3600 + m * 60 + s

        return render_template("index.html", total=total_seconds)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
