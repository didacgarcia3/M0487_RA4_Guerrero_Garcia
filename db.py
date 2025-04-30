import sqlite3

def connect_db():
    """Connecta a la base de dades SQLite."""
    try:
        conn = sqlite3.connect('grups_musicals.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error al connectar amb la base de dades: {e}")
        return None

def crear_taula():
    """Crea la taula si no existeix."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS grups_musicals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    any_inici INTEGER NOT NULL CHECK (any_inici >= 1960),
                    tipus TEXT NOT NULL,
                    num_integrants INTEGER NOT NULL CHECK (num_integrants > 0)
                )
            ''')
            conn.commit()
            print("Taula creada o ja existent.")
        except sqlite3.Error as e:
            print(f"Error al crear la taula: {e}")
        finally:
            conn.close()
    else:
        print("No es pot connectar a la base de dades.")

def afegir_grup(nom, any_inici, tipus, num_integrants):
    """Afegeix un nou grup a la base de dades."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO grups_musicals (nom, any_inici, tipus, num_integrants)
                VALUES (?, ?, ?, ?)
            ''', (nom, any_inici, tipus, num_integrants))
            conn.commit()
            print(f"Grup '{nom}' afegit amb èxit!")
        except sqlite3.Error as e:
            print(f"Error en afegir el grup: {e}")
        finally:
            conn.close()

def consultar_grup(nom):
    """Consulta un grup per nom."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grups_musicals WHERE nom=?', (nom,))
            grup = cursor.fetchone()
            return grup
        except sqlite3.Error as e:
            print(f"Error en la consulta del grup: {e}")
        finally:
            conn.close()
    return None

def llistar_grups():
    """Llista tots els grups."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grups_musicals')
            grups = cursor.fetchall()
            return grups
        except sqlite3.Error as e:
            print(f"Error al llistar els grups: {e}")
        finally:
            conn.close()
    return []

def actualitzar_grup(id, nom, any_inici, tipus, num_integrants):
    """Actualitza un grup existent."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE grups_musicals
                SET nom=?, any_inici=?, tipus=?, num_integrants=?
                WHERE id=?
            ''', (nom, any_inici, tipus, num_integrants, id))
            conn.commit()
            print(f"Grup '{nom}' actualitzat amb èxit!")
        except sqlite3.Error as e:
            print(f"Error en actualitzar el grup: {e}")
        finally:
            conn.close()

def eliminar_grup(id):
    """Elimina un grup de la base de dades."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM grups_musicals WHERE id=?', (id,))
            conn.commit()
            print(f"Grup eliminat amb èxit!")
        except sqlite3.Error as e:
            print(f"Error al eliminar el grup: {e}")
        finally:
            conn.close()
