import sqlite3

conn = sqlite3.connect('BDD_Voiture.db')
cursor = conn.cursor()

#LIST DE V
id_1 = BDD_Voiture(1, 'Ford Mustang', 'RWD', 450, 10, 60, 'Petrol', 2022, 'Ford', 'Coupe', 4, 300, 70000, 120000)
id_2 = BDD_Voiture(2, 'Honda CR V', 'AWD', 190, 12, 57, 'Petrol', 2025, 'Honda', 'SUV', 5, 700, 80000, 100000)
id_3 = BDD_Voiture(3, 'BMW X5', 'RWD', 335, 11, 83, 'Petrol', 2008, 'BMW', 'SUV', 5, 650, 100000, 180000)
id_4 = BDD_Voiture(4, 'Toyota Camry', 'RWD', 203, 15, 60, 'Petrol', 2001, 'Toyota', 'Sedan', 5, 500, 40000, 80000)
id_5 = BDD_Voiture(5, 'Chevrolet Camaro', 'RWD', 455, 9, 63, 'Petrol', 2023, 'Chevrolet', 'Coupe', 4, 250, 75000, 130000)
id_6 = BDD_Voiture(6, 'Nissan Rogue', 'AWD', 170, 26, 54, 'Petrol', 2024, 'Nissan', 'SUV', 5, 800, 32000, 42000)
id_7 = BDD_Voiture(7, 'Volkswagen Passat', 'FWD', 174, 29, 62, 'Petrol', 2020, 'Volkswagen', 'Sedan', 5, 400, 28000, 36000)


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

def lien_fichier(db_file):
    try:
        connection = sqlite3.connect(db_file)
        print("Connection to the database established.")
        return connection
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def afficher_voitures():
    cursor.execute("SELECT * FROM voitures")
    voitures = cursor.fetchall()
    for voiture in voitures:
        print(voiture)

def insert_voiture(voiture):
    with conn:
        cursor.execute("""
            INSERT INTO voitures (nom, transmission, puissance, kpl, reservoir, engin, annee, marque, typev, sieges, espace, prix_utilise, prix_nouveau)
            VALUES (:nom, :transmission, :puissance, :kpl, :reservoir, :engin, :annee, :marque, :typev, :sieges, :espace, :prix_utilise, :prix_nouveau)
        """, {
            'nom': voiture.nom,
            'transmission': voiture.transmission,
            'puissance': voiture.puissance,
            'kpl': voiture.kpl,
            'reservoir': voiture.reservoir,
            'engin': voiture.engin,
            'annee': voiture.annee,
            'marque': voiture.marque,
            'typev': voiture.typev,
            'sieges': voiture.sieges,
            'espace': voiture.espace,
            'prix_utilise': voiture.prix_utilise,
            'prix_nouveau': voiture.prix_nouveau
        })
        

def rm_voiture(nom):
    with conn:
        cursor.execute("DELETE FROM voitures WHERE nom = :nom", {'nom': nom})

def update_voiture(voiture):
    with conn:
        cursor.execute("""
            UPDATE voitures SET transmission = :transmission, puissance = :puissance, kpl = :kpl, reservoir = :reservoir, engin = :engin, annee = :annee, marque = :marque, typev = :typev, sieges = :sieges, espace = :espace, prix_utilise = :prix_utilise, prix_nouveau = :prix_nouveau
            WHERE nom = :nom
        """, {
            'nom': voiture.nom,
            'transmission': voiture.transmission,
            'puissance': voiture.puissance,
            'kpl': voiture.kpl,
            'reservoir': voiture.reservoir,
            'engin': voiture.engin,
            'annee': voiture.annee,
            'marque': voiture.marque,
            'typev': voiture.typev,
            'sieges': voiture.sieges,
            'espace': voiture.espace,
            'prix_utilise': voiture.prix_utilise,
            'prix_nouveau': voiture.prix_nouveau
        })

def select_voiture(filters):
    query = "SELECT * FROM voitures WHERE 1=1"
    params = {}
    
    if filters.get('nom'):
        query += " AND nom = :nom"
        params['nom'] = filters['nom']
    if filters.get('transmission'):
        query += " AND transmission = :transmission"
        params['transmission'] = filters['transmission']


    cursor.execute(query, params)
    return cursor.fetchall()

def main():
    connection = lien_fichier('BDD_Voiture.db')
    
    if connection:
        while True:
            print("Menu:")
            print("1. Afficher les voitures")
            print("2. Filtrer les voitures")
            print("3. Ajouter une voiture")
            print("4. Mettre à jour une voiture")
            print("5. Supprimer une voiture")
            print("6. Quitter")
            option = input("Choisissez une option: ")

            if option == '1':
                afficher_voitures()
            elif option == '2':
                filters = {}
                filters['nom'] = input("Filtrer par nom [vide pour ignorer]: ") or None
                filters['transmission'] = input("Filtrer par transmission [vide pour ignorer]: ") or None
                results = select_voiture(filters)
                for result in results:
                    print(result)
            elif option == '3':
                new_voiture = Voiture(7, 'New Car', 'FWD', 150, 10, 50, 'Petrol', 2023, 'Brand', 'Sedan', 5, 500, 30000, 35000)
                insert_voiture(new_voiture)
            elif option == '4':
                update_voiture(new_voiture)
            elif option == '5':
                nom = input("Nom de la voiture à supprimer: ")
                rm_voiture(nom)
            elif option == '6':
                break
            else:
                print("Erreur: option invalide.")

if __name__ == "__main__":
    main()
