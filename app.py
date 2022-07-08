from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    return render_template("home.html", count=count)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/techsiulutions")
def index():
    return render_template("index.html")

@app.route("/Happy_Siu")
def Happy_Siu():
    return "Welcome to Happy Siu's Website: "

if __name__ == "__main__":
    app.run()