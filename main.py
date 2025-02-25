import sqlite3

conn = sqlite3.connect('BDD_Voiture.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS voitures (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        transmission TEXT,
        puissance INTEGER,
        kpl INTEGER,
        reservoir INTEGER,
        engin TEXT,
        annee INTEGER,
        marque TEXT,
        typev TEXT,
        sieges INTEGER,
        espace INTEGER,
        prix_utilise INTEGER,
        prix_nouveau INTEGER
    )
""")

class Voiture:
    def __init__(self, id, nom, transmission, puissance, kpl, reservoir, engin, annee, marque, typev, sieges, espace, prix_utilise, prix_nouveau):
        self.id = id
        self.nom = nom
        self.transmission = transmission
        self.puissance = puissance
        self.kpl = kpl
        self.reservoir = reservoir
        self.engin = engin
        self.annee = annee
        self.marque = marque
        self.typev = typev
        self.sieges = sieges
        self.espace = espace
        self.prix_utilise = prix_utilise
        self.prix_nouveau = prix_nouveau

def afficher_voitures():
    cursor.execute("SELECT * FROM voitures")
    voitures = cursor.fetchall()
    bold = "\033[1m"
    reset = "\033[0m"
    print(f"\n{bold}Liste des Voitures:{reset}")
    print("-" * 50)
    print(f"{bold}ID  | Nom                | Année | Type{reset}")
    print("-" * 50)
    for voiture in voitures:
        print(f"{voiture[0]:<4} | {voiture[1]:<18} | {voiture[7]} | {voiture[9]}")
    print("-" * 50)

def afficher_voiture_details(id):
    cursor.execute("""
        SELECT nom, transmission, puissance, kpl, reservoir, engin, annee, marque, typev, sieges, espace, prix_utilise, prix_nouveau
        FROM voitures
        WHERE id = :id
    """, {'id': id})
    voiture = cursor.fetchone()

    if voiture:
        print("\n" + "=" * 50)
        print(f"{'Détails de la Voiture':^50}")
        print("=" * 50)
        print(f"Nom:               {voiture[0]}")
        print(f"Transmission:      {voiture[1]}")
        print(f"Puissance (ch):    {voiture[2]}")
        print(f"Kilométrage (kpl): {voiture[3]}")
        print(f"Réservoir (L):     {voiture[4]}")
        print(f"Type d'engin:      {voiture[5]}")
        print(f"Année:             {voiture[6]}")
        print(f"Marque:            {voiture[7]}")
        print(f"Type de voiture:   {voiture[8]}")
        print(f"Nombre de sièges:  {voiture[9]}")
        print(f"Espace (L):        {voiture[10]}")
        print(f"Prix Utilisé ($):  {voiture[11]}")
        print(f"Prix Neuf ($):     {voiture[12]}")
        print("=" * 50 + "\n")
    else:
        print("Aucune voiture trouvée avec cet ID.")

def filtrer_voitures():
    filters = {}
    filters['nom'] = input("Filtrer par nom [vide pour ignorer]: ") or None
    filters['marque'] = input("Filtrer par marque [vide pour ignorer]: ") or None
    filters['typev'] = input("Filtrer par type de voiture [vide pour ignorer]: ") or None
    filters['transmission'] = input("Filtrer par transmission [vide pour ignorer]: ") or None
    filters['engin'] = input("Filtrer par type d'engin [vide pour ignorer]: ") or None
    filters['annee_min'] = input("Filtrer par année minimale [vide pour ignorer]: ") or None
    filters['annee_max'] = input("Filtrer par année maximale [vide pour ignorer]: ") or None
    filters['prix_utilise_min'] = input("Filtrer par prix utilisé minimal [vide pour ignorer]: ") or None
    filters['prix_utilise_max'] = input("Filtrer par prix utilisé maximal [vide pour ignorer]: ") or None

    query = "SELECT * FROM voitures WHERE 1=1"
    params = []

    if filters['nom']:
        query += " AND LOWER(nom) LIKE ?"
        params.append(f"%{filters['nom'].lower()}%")
    if filters['marque']:
        query += " AND LOWER(marque) LIKE ?"
        params.append(f"%{filters['marque'].lower()}%")
    if filters['typev']:
        query += " AND LOWER(typev) LIKE ?"
        params.append(f"%{filters['typev'].lower()}%")
    if filters['transmission']:
        query += " AND LOWER(transmission) LIKE ?"
        params.append(f"%{filters['transmission'].lower()}%")
    if filters['engin']:
        query += " AND LOWER(engin) LIKE ?"
        params.append(f"%{filters['engin'].lower()}%")
    if filters['annee_min']:
        query += " AND annee >= ?"
        params.append(int(filters['annee_min']))
    if filters['annee_max']:
        query += " AND annee <= ?"
        params.append(int(filters['annee_max']))
    if filters['prix_utilise_min']:
        query += " AND prix_utilise >= ?"
        params.append(float(filters['prix_utilise_min']))
    if filters['prix_utilise_max']:
        query += " AND prix_utilise <= ?"
        params.append(float(filters['prix_utilise_max']))

    cursor.execute(query, params)
    results = cursor.fetchall()

    if results:
        print("\n" + "=" * 50)
        print(f"{'Résultats de la Recherche':^50}")
        print("=" * 50)
        for result in results:
            print(f"ID: {result[0]} | Nom: {result[1]} | Année: {result[7]} | Type: {result[9]}")
        print("=" * 50)

        detail_option = input("Voulez-vous voir les détails d'une voiture? (oui/non): ").lower()
        if detail_option == 'oui':
            id_input = input("Entrez l'ID de la voiture: ")
            if id_input.isdigit():
                afficher_voiture_details(int(id_input))
            else:
                print("Entrée invalide. Veuillez entrer un ID valide.")
    else:
        print("Aucun résultat trouvé.")

def ajouter_voiture():
    nom = input("Nom du Voiture: ")
    transmission = input("Transmission: ")
    puissance = int(input("Puissance: "))
    kpl = float(input("Kilométrage: "))
    reservoir = float(input("Réservoir: "))
    engin = input("Type d'engin: ")
    annee = int(input("Année: "))
    marque = input("Marque: ")
    typev = input("Type de voiture: ")
    sieges = int(input("Nombre de sièges: "))
    espace = float(input("Espace: "))
    prix_utilise = float(input("Prix Utilisé: "))
    prix_nouveau = float(input("Prix Neuf: "))

    cursor.execute("""
        INSERT INTO voitures (nom, transmission, puissance, kpl, reservoir, engin, annee, marque, typev, sieges, espace, prix_utilise, prix_nouveau)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (nom, transmission, puissance, kpl, reservoir, engin, annee, marque, typev, sieges, espace, prix_utilise, prix_nouveau))
    conn.commit()
    print("Voiture ajoutée avec succès!")

def mettre_a_jour_voiture():
    id_input = input("Entrez l'ID de la voiture à mettre à jour: ")
    if id_input.isdigit():
        afficher_voiture_details(int(id_input))
        nom = input("Nouveau nom [vide pour ignorer]: ") or None
        transmission = input("Nouvelle transmission [vide pour ignorer]: ") or None
        puissance = input("Nouvelle puissance [vide pour ignorer]: ") or None
        kpl = input("Nouveau kilométrage [vide pour ignorer]: ") or None
        reservoir = input("Nouveau réservoir [vide pour ignorer]: ") or None
        engin = input("Nouveau type d'engin [vide pour ignorer]: ") or None
        annee = input("Nouvelle année [vide pour ignorer]: ") or None
        marque = input("Nouvelle marque [vide pour ignorer]: ") or None
        typev = input("Nouveau type de voiture [vide pour ignorer]: ") or None
        sieges = input("Nouveau nombre de sièges [vide pour ignorer]: ") or None
        espace = input("Nouvel espace [vide pour ignorer]: ") or None
        prix_utilise = input("Nouveau prix utilisé [vide pour ignorer]: ") or None
        prix_nouveau = input("Nouveau prix neuf [vide pour ignorer]: ") or None

        query = "UPDATE voitures SET "
        params = []
        if nom:
            query += "nom = ?, "
            params.append(nom)
        if transmission:
            query += "transmission = ?, "
            params.append(transmission)
        if puissance:
            query += "puissance = ?, "
            params.append(int(puissance))
        if kpl:
            query += "kpl = ?, "
            params.append(float(kpl))
        if reservoir:
            query += "reservoir = ?, "
            params.append(float(reservoir))
        if engin:
            query += "engin = ?, "
            params.append(engin)
        if annee:
            query += "annee = ?, "
            params.append(int(annee))
        if marque:
            query += "marque = ?, "
            params.append(marque)
        if typev:
            query += "typev = ?, "
            params.append(typev)
        if sieges:
            query += "sieges = ?, "
            params.append(int(sieges))
        if espace:
            query += "espace = ?, "
            params.append(float(espace))
        if prix_utilise:
            query += "prix_utilise = ?, "
            params.append(float(prix_utilise))
        if prix_nouveau:
            query += "prix_nouveau = ?, "
            params.append(float(prix_nouveau))

        query = query.rstrip(", ")

        query += " WHERE id = ?"
        params.append(int(id_input))

        cursor.execute(query, params)
        conn.commit()
        print("Voiture mise à jour avec succès!")
    else:
        print("Entrée invalide. Veuillez entrer un ID valide.")

def supprimer_voiture():
    nom = input("Nom de la voiture à supprimer: ")
    cursor.execute("DELETE FROM voitures WHERE nom = ?", (nom,))
    conn.commit()
    print("Voiture supprimée avec succès!")

def main():
    while True:
        print("\n" + "=" * 50)
        print(f"{'Menu Principal':^50}")
        print("=" * 50)
        print("1. Afficher les voitures")
        print("2. Filtrer les voitures")
        print("3. Ajouter une voiture")
        print("4. Mettre à jour une voiture")
        print("5. Supprimer une voiture")
        print("6. Quitter")
        print("=" * 50)
        option = input("Choisissez une option: ")

        if option == '1':
            afficher_voitures()
            detail_option = input("Voulez-vous voir les détails d'une voiture? (oui/non): ").lower()
            if detail_option == 'oui':
                id_input = input("Entrez l'ID de la voiture: ")
                if id_input.isdigit():
                    afficher_voiture_details(int(id_input))
                else:
                    print("Entrée invalide. Veuillez entrer un ID valide.")
        elif option == '2':
            filtrer_voitures()
        elif option == '3':
            ajouter_voiture()
        elif option == '4':
            mettre_a_jour_voiture()
        elif option == '5':
            supprimer_voiture()
        elif option == '6':
            break
        else:
            print("Erreur: option invalide.")

if __name__ == "__main__":
    main()
