from db import afegir_grup, consultar_grup, llistar_grups, actualitzar_grup, eliminar_grup, crear_taula
from time import sleep

def intro_dades(nom=None):
    """Gestiona la introducció i validació de dades."""
    while True:
        if nom is None:
            nom = input("Introduïu el nom del grup: ")
        any_inici = input("Introduïu l'any d'inici (≥ 1960): ")
        if not any_inici.isdigit() or int(any_inici) < 1960:
            print("Any d'inici no vàlid!")
            continue
        tipus = input("Introduïu el tipus de grup: ")
        num_integrants = input("Introduïu el nombre d'integrants (≥ 1): ")
        if not num_integrants.isdigit() or int(num_integrants) <= 0:
            print("Nombre d'integrants no vàlid!")
            continue
        break
    return nom, int(any_inici), tipus, int(num_integrants)

def afegir_grup_interface():
    """Afegir un grup mitjançant la funció intro_dades."""
    nom, any_inici, tipus, num_integrants = intro_dades()
    afegir_grup(nom, any_inici, tipus, num_integrants)  
    sleep(1)

def consultar_grup_interface():
    """Consulta un grup per nom."""
    nom = input("Introduïu el nom del grup a consultar: ")
    grup = consultar_grup(nom)
    if grup:
        print(f"\nInformació detallada del grup:")
        print(f"Nom del grup: {grup[1]}")
        print(f"Any d'inici: {grup[2]}")
        print(f"Tipus de grup: {grup[3]}")
        print(f"Nombre d'integrants: {grup[4]}")
    else:
        print("Grup no trobat.")
    sleep(1)

def llistar_grups_interface():
    """Llista tots els grups."""
    grups = llistar_grups()
    if grups:
        print("\nLlistat de grups musicals:")
        for grup in grups:
            print(f"\nNom del grup: {grup[1]}")
            print(f"Any d'inici: {grup[2]}")
            print(f"Tipus de grup: {grup[3]}")
            print(f"Nombre d'integrants: {grup[4]}")
    else:
        print("No hi ha grups a la base de dades.")
    sleep(1)

def actualitzar_grup_interface():
    """Actualitza un grup existent."""
    nom = input("Introduïu el nom del grup a actualitzar: ")
    grup = consultar_grup(nom)
    if grup:
        print(f"Grup actual: {grup}")
        id = grup[0]

        print("Deixa en blanc el camp que no vols modificar.")
        nom_nou = input(f"Nou nom (actual: {grup[1]}): ")
        if not nom_nou:
            nom_nou = grup[1]  
        
        any_inici_nou = input(f"Any d'inici (actual: {grup[2]}): ")
        if not any_inici_nou:
            any_inici_nou = grup[2]  
        
        tipus_nou = input(f"Tipus (actual: {grup[3]}): ")
        if not tipus_nou:
            tipus_nou = grup[3] 
        
        num_integrants_nou = input(f"Nombre d'integrants (actual: {grup[4]}): ")
        if not num_integrants_nou:
            num_integrants_nou = grup[4]  

        actualitzar_grup(id, nom_nou, any_inici_nou, tipus_nou, num_integrants_nou)
        sleep(1)
    else:
        print("Grup no trobat.")
        sleep(1)

def eliminar_grup_interface():
    """Elimina un grup."""
    nom = input("Introduïu el nom del grup a eliminar: ")
    grup = consultar_grup(nom)
    if grup:
        id = grup[0]
        eliminar_grup(id)
        sleep(1)
    else:
        print("Grup no trobat.")
        sleep(1)

def mostrar_menu():
    """Mostra un menú per interactuar amb l'usuari."""
    while True:
        print("\n--- Gestor de Grups Musicals ---")
        print("1. Afegir un grup")
        print("2. Consultar un grup")
        print("3. Llistar tots els grups")
        print("4. Actualitzar un grup")
        print("5. Eliminar un grup")
        print("6. Sortir")
        
        opcio = input("Selecciona una opció (1-6): ")
        
        if opcio == '1':
            afegir_grup_interface()
        elif opcio == '2':
            consultar_grup_interface()
        elif opcio == '3':
            llistar_grups_interface()
        elif opcio == '4':
            actualitzar_grup_interface()
        elif opcio == '5':
            eliminar_grup_interface()
        elif opcio == '6':
            print("Sortint de l'aplicació...")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció entre 1 i 6.")
            sleep(1)

if __name__ == "__main__":
    crear_taula()  
    mostrar_menu()  