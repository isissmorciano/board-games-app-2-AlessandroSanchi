from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import giochi_repo

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