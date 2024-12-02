from flask import Flask, render_template

# Tentukan folder template khusus
app = Flask(__name__, template_folder='html')

@app.route("/")
def login_page():
    return render_template("add.html")

@app.route("/daftar")
def daftar_page():
    return render_template("daftar.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
