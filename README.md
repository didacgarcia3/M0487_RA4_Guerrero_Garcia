## DESCRIPCIÓ DEL PROJECTE

Aquest projecte consisteix en el desenvolupament d’una aplicació en Python per gestionar grups musicals,
com a part del mòdul *Entorns de Desenvolupament* (M0487) del cicle formatiu de grau superior DAM.

L’objectiu és consolidar bones pràctiques de programació, com la reutilització de funcions, 
la documentació clara amb docstrings, la creació de tests automatitzats i l’ús col·laboratiu de Git i GitHub.

# Funcionalitats principals

- Afegir un nou grup musical
- Consultar un grup pel seu nom
- Llistar tots els grups
- Actualitzar les dades d’un grup
- Eliminar un grup
- Validació de dades
- Ús de SQLite per emmagatzemar la informació

# Objectius del projecte

- Refactoritzar i millorar codi existent
- Documentar correctament el projecte (README)
- Treballar en equip amb control de versions (Git, GitHub)
- Aplicar testing amb el mòdul "unittest"
- Registrar l’evolució del projecte amb "HISTÒRIC.md"

# Tecnologies i eines utilitzades

- Python 3
- SQLite "sqlite3"
- Git i GitHub
- unittest 
- git graph

## ESTRUCTURA DEL CODI

El projecte està dividit en dos arxius principals:
1. db.py

Conté totes les operacions relacionades amb la base de dades:

    crear_taula() – Crea la taula si no existeix.

    afegir_grup(...) – Afegeix un nou grup musical.

    consultar_grup(nom) – Cerca un grup pel seu nom.

    llistar_grups() – Mostra tots els grups musicals.

    actualitzar_grup(...) – Actualitza un grup existent.

    eliminar_grup(id) – Elimina un grup a partir del seu identificador.

2. gestor_grups.py

És la interfície principal que gestiona la interacció amb l’usuari:

    intro_dades(...) – Funció reutilitzable per introduir i validar dades del grup.

    afegir_grup_interface() – Fa servir intro_dades() per afegir un grup.

    consultar_grup_interface() – Mostra informació detallada d’un grup.

    llistar_grups_interface() – Mostra tots els grups en format llegible.

    actualitzar_grup_interface() – Permet modificar dades d’un grup, deixant valors en blanc si no es volen canviar.

    eliminar_grup_interface() – Permet eliminar un grup pel nom.

    mostrar_menu() – Menú interactiu amb l’usuari que crida les funcions anteriors.


## CRÈDITS I AUTORIA

El treball ha sigut realitzat per Dídac García Molina i Denís Guerrero Rodríguez.