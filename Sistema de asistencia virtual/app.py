from flask import Flask, render_template, request, redirect, url_for
from asistente import comandos, speech_to_text, text_to_speech

app = Flask(__name__, static_folder='static')


# @app.route("/", metho*ds=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         nombre = request.form.get("nombre")
#         return f"<h1>Hola, {nombre}!</h1>"
#     return render_template("index.html")


@app.route("/")
def index():
    leido = request.args.get("leido", "false").lower() == "true"
    texto = request.args.get("texto", "")
    return render_template("menu.html", leido=leido, texto=texto)


@app.route("/texto_voz", methods=["POST"])
def texto_voz():
    texto = request.form.get("texto", "").strip()

    if texto:
        text_to_speech(texto, "es")

    return redirect(url_for("index", leido="true", texto=texto))


@app.route("/voz_texto")
def voz_texto():
    texto = speech_to_text()
    return redirect(url_for("index", leido="true", texto=texto))


@app.route("/operaciones")
def operaciones():
    texto = comandos()
    return redirect(url_for("index", leido="true", texto=texto))


if __name__ == "__main__":
    app.run(debug=True)
