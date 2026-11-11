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
    filtro = request.args.get("filtro", "todas")
    concluidas = 0
    tarefas_visiveis = []

    for indice, tarefa in enumerate(tarefas):
        if tarefa["concluida"]:
            concluidas += 1

        if filtro == "pendentes" and tarefa["concluida"]:
            continue

        if filtro == "concluidas" and not tarefa["concluida"]:
            continue

        tarefas_visiveis.append((indice, tarefa))

    pendentes = len(tarefas) - concluidas

    return render_template(
        "index.html",
        tarefas=tarefas_visiveis,
        pendentes=pendentes,
        concluidas=concluidas,
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form.get("titulo", "").strip()

    if titulo:
        tarefas.insert(0, {"titulo": titulo, "concluida": False})
        salvar_tarefas()

    return redirect(url_for("inicio"))


@app.route("/concluir/<int:indice>", methods=["POST"])
def concluir(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = not tarefas[indice]["concluida"]
        salvar_tarefas()

    return redirect(url_for("inicio"))


@app.route("/excluir/<int:indice>", methods=["POST"])
def excluir(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas()

    return redirect(url_for("inicio"))

@app.route("/editar/<int:indice>", methods=["POST"])
def editar(indice):
    titulo = request.form.get("titulo", "").strip()

    if 0 <= indice < len(tarefas) and titulo:
        tarefas[indice]["titulo"] = titulo
        salvar_tarefas()

    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)