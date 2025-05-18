from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form['user']
        pwd = request.form['password']
        if user == "admin" and pwd == "123":  # autenticação fraca proposital
            return "Bem-vindo, admin"
        return "Credenciais inválidas"
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
