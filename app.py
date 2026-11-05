import json
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

ARQUIVO_TAREFAS = Path(__file__).parent / "tarefas.json"


def carregar_tarefas():
    if ARQUIVO_TAREFAS.exists():
        with ARQUIVO_TAREFAS.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []


def salvar_tarefas():
    with ARQUIVO_TAREFAS.open("w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


tarefas = carregar_tarefas()


@app.route("/")
def inicio():
    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form.get("titulo", "").strip()

    if titulo:
        tarefas.append({
            "titulo": titulo,
            "concluida": False,
        })
        salvar_tarefas()

    return redirect(url_for("inicio"))


@app.route("/concluir/<int:indice>", methods=["POST"])
def concluir(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas()

    return redirect(url_for("inicio"))


@app.route("/excluir/<int:indice>", methods=["POST"])
def excluir(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas()

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)