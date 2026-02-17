from app.db import get_db


def get_all_games():
    """Recupera tutti i giochi dalla tabella `giochi`.

    Restituisce una lista di dizionari con le colonne principali.
    """
    db = get_db()
    query = """
        SELECT id, nome, numero_giocatori_massimo, durata_media, categoria
        FROM giochi
        ORDER BY nome
    """
    games = db.execute(query).fetchall()
    return [dict(g) for g in games]

def get_game_by_id(game_id):
    
    db = get_db()

    query = """
        SELECT id, nome, numero_giocatori_massimo, durata_media,categoria
        FROM giochi
        WHERE id = ?
    """

    game = db.execute(query,(game_id,)).fetchone()
    if game:
     return game
    else:

     return None

    
