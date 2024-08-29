from flask import Flask, render_template, request, url_for


app =  Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logar",methods=["POST"])
def logar():
    usuario = request.form.get("login")
    senha = request.form.get("senha")
    print(f"usuario: {usuario}")
    print(f"senha: {senha}")

    if usuario == "mayck" and senha == "123":
        return render_template("main.html")
    else:
        return "<h2>Dados invalidos</h2>"

if __name__ == "__main__":
    app.run(debug=True)

