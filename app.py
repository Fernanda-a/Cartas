from flask import Flask, render_template, request, redirect, flash
from models import save_carta, save_carta_txt

app = Flask(__name__)
app.secret_key = "algo"

@app.route("/", methods=["GET", "POST"])
def login():
	arquivo = open("login.txt", "r")

	if request.method == "POST":
		nome = request.form.get("nome")
		senha = request.form.get("senha")

		users = arquivo.readlines()

		if nome + '-' + senha + "\n" in users:
			return redirect("/carta")

		else:
			arquivo = open("login.txt", "a")
			arquivo.write(f"{nome}-{senha}\n")
			arquivo.close()

			flash("Usuário criado com sucesso")

			return render_template("login.html")

	return render_template("login.html")

@app.route("/carta", methods=["GET", "POST"])
def make():
	if request.method == "POST":
		data = request.form.get("data")
		dest = request.form["destinatario"]
		mens = request.form["mensagem"]
		reme = request.form["remetente"]
		file_name = request.form["file_name"]

		carta = "Data: " + data + "\n\nDestinatário: " + dest + "\n\nMensagem:\n" + mens + "\n\nRemetente: " + reme
		save_carta_txt(carta, file_name)
		save_carta(file_name)

		return render_template("mcarta.html")

	return render_template("mcarta.html")


if __name__ == "__main__":
    app.run(debug=True)
