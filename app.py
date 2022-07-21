from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Thisissocool_dude"

@app.route("/")
def home():
    flash("What's your name?")
    return render_template("home.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hello " + str(request.form['name_input']) + ", pleasure to meet you! ")
    request.form['name_input']
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/techsiulutions")
def techsiulutions():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
