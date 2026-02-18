from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import giochi_repo, partita_repo

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint("main", __name__)

@bp.route("/")
def index():


    # 1. Prendiamo i canali dal database
    games: list[dict] = giochi_repo.get_all_games()

    # 2. Passiamo la variabile 'games' al template
    return render_template("index.html", games=games)


@bp.route("/game/<int:id>")
def game_detail(id):

    game = giochi_repo.get_game_by_id(id)

    return render_template("game_detail.html", game=game)


@bp.route("/create", methods=("GET", "POST"))
def game_create():
        
    if request.method == "POST":
        nome = request.form["nome"]
        numero_giocatori_massimo = request.form.get("numero_giocatori_massimo", 0, type=int)
        durata_media = request.form["durata_media"]
        categoria = request.form["categoria"]
        error = None

        if not nome:
            error = "Il nome è obbligatorio."
        if not categoria:
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            # Creiamo il gioco
            giochi_repo.create_game(nome, numero_giocatori_massimo, categoria,durata_media)
            return redirect(url_for("main.index"))

        return render_template("game_create.html")




    return render_template("game_create.html")      

@bp.route("/game<int:id>/partite", methods=("GET", "POST"))
def get_partita(id):
    partita = partita_repo.get_partita_by_id(id)
    if partita is None:
        abort(404, f"Partita con id {id} non trovata.")
    return render_template("partita_detail.html", partita=partita)


@bp.route("/game<int:id>/partite/create", methods=("GET", "POST"))
def partita_create(id):
        
    if request.method == "POST":
        data = request.form["data"]
        vincitore = request.form["vincitore"]
        punteggio_vincitore = request.form.get("punteggio_vincitore", 0, type=int)
        error = None
        game_id = id

        if not data:
            error = "La data è obbligatoria."
        if not vincitore:
            error = "Il vincitore è obbligatorio."
        if not punteggio_vincitore:
            error = "Il punteggio del vincitore è obbligatorio."
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            # Creiamo il gioco
            partita_repo.create_partita(game_id, data, vincitore, punteggio_vincitore)
            return redirect(url_for("main.index"))

        return render_template("partita_create.html")
    return render_template("partita_create.html")