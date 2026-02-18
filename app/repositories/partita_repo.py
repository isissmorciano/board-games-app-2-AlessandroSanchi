from app.db import get_db

def get_partita_by_id(gioco_id):
    
    db = get_db()

    query = """
        SELECT gioco_id, data, vincitore, punteggio_vincitore
        FROM partite
        WHERE gioco_id = ?
    """

    partita = db.execute(query,(gioco_id,)).fetchall()
    if partita:
     return partita
    else:

     return None
    

def create_partita(gioco_id, data, vincitore, punteggio_vincitore):
    """Crea una nuova partita."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (?, ?, ?, ?)", (gioco_id, data, vincitore, punteggio_vincitore)
    )
    db.commit()
    return cursor