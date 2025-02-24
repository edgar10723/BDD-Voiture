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
    bold = "\033[1m"
    reset = "\033[0m"
    for voiture in voitures:
        print(voiture[0],f"{bold}{voiture[1]}{reset} | ",voiture[7],voiture[9])

def afficher_voiture_details(id):
    cursor.execute("SELECT nom, transmission, puissance, kpl, reservoir, engin, annee, marque, typev, sieges, espace, prix_utilise, prix_nouveau FROM voitures WHERE id = :id", {'id': id})
    voiture = cursor.fetchone()

def insert_voiture(voiture):
    with conn:
        cursor.execute("""
            INSERT INTO voitures (id, nom, transmission, puissance, kpl, reservoir, engin, annee, marque, typev, sieges, espace, prix_utilise, prix_nouveau)
            VALUES (:id, :nom, :transmission, :puissance, :kpl, :reservoir, :engin, :annee, :marque, :typev, :sieges, :espace, :prix_utilise, :prix_nouveau)
        """, {
            'id': voiture.id,
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
            UPDATE voitures SET nom = :nom, transmission = :transmission, puissance = :puissance, kpl = :kpl, reservoir = :reservoir, engin = :engin, annee = :annee, marque = :marque, typev = :typev, sieges = :sieges, espace = :espace, prix_utilise = :prix_utilise, prix_nouveau = :prix_nouveau
            WHERE id = :id
        """, {
            'id': voiture.id,
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

def add_voiture():
    nouveau_nom = input("Nom du Voiture:")
    nouveau_transmission = input("Nom du Voiture:")
    nouveau_puissance = input("Nom du Voiture:")
    nouveau_kpl = input("Nom du Voiture:")
    nouveau_reservoir = input("Nom du Voiture:")
    nouveau_engin = input("Nom du Voiture:")
    nouveau_annee = input("Nom du Voiture:")
    nouveau_marque = input("Nom du marque:")
    nouveau_typev = input("Nom du Voiture:")
    nouveau_sieges = input("Nom du Voiture:")
    nouveau_espace = input("Espace:")
    nouveau_prix_u = input("prix U")
    nouveau_prix_n = input("prix n")

    return Voiture(cursor.execute("SELECT COUNT() FROM voitures").fetchone()[0] + 1, nouveau_nom, nouveau_transmission, nouveau_puissance, nouveau_kpl, nouveau_reservoir, nouveau_engin,
                   nouveau_annee, nouveau_marque, nouveau_typev, nouveau_sieges, nouveau_espace, nouveau_prix_u, nouveau_prix_n)


def main():
    connection = lien_fichier('BDD_Voiture.db')
    
    if connection:
        voitures = [
            Voiture(1, 'Ford Mustang', 'RWD', 450, 10, 60, 'Petrol', 2022, 'Ford', 'Coupe', 4, 300, 70000, 120000),
            Voiture(2, 'Honda CR V', 'AWD', 190, 12, 57, 'Petrol', 2025, 'Honda', 'SUV', 5, 700, 80000, 100000),
            Voiture(3, 'BMW X5', 'RWD', 335, 11, 83, 'Petrol', 2008, 'BMW', 'SUV', 5, 650, 100000, 180000),
            Voiture(4, 'Toyota Camry', 'RWD', 203, 15, 60, 'Petrol', 2001, 'Toyota', 'Sedan', 5, 500, 40000, 80000),
            Voiture(5, 'Chevrolet Camaro', 'RWD', 455, 9, 63, 'Petrol', 2023, 'Chevrolet', 'Coupe', 4, 250, 75000, 130000),
            Voiture(6, 'Nissan Rogue', 'AWD', 170, 26, 54, 'Petrol', 2024, 'Nissan', 'SUV', 5, 800, 32000, 42000),
            Voiture(7, 'Volkswagen Passat', 'FWD', 174, 29, 62, 'Petrol', 2020, 'Volkswagen', 'Sedan', 5, 400, 28000, 36000),
            Voiture(8, 'Tesla Model 3', 'AWD', 283, 15, 75, 'Electric', 2022, 'Tesla', 'Sedan', 5, 425, 35000, 50000),
            Voiture(9, 'Ford F-150', '4WD', 400, 10, 80, 'Petrol', 2023, 'Ford', 'Truck', 5, 1000, 40000, 60000),
            Voiture(10, 'Hyundai Elantra', 'FWD', 147, 35, 50, 'Petrol', 2021, 'Hyundai', 'Sedan', 5, 400, 20000, 25000),
            Voiture(11, 'Mazda CX-5', 'AWD', 187, 28, 56, 'Petrol', 2022, 'Mazda', 'SUV', 5, 800, 28000, 35000),
            Voiture(12, 'Subaru Outback', 'AWD', 182, 26, 60, 'Petrol', 2021, 'Subaru', 'Wagon', 5, 750, 27000, 33000),
            Voiture(13, 'Porsche 911', 'RWD', 379, 20, 64, 'Petrol', 2022, 'Porsche', 'Coupe', 2, 300, 80000, 120000),
            Voiture(14, 'Jeep Wrangler', '4WD', 285, 22, 66, 'Petrol', 2023, 'Jeep', 'SUV', 4, 800, 35000, 45000),
            Voiture(15, 'Kia Soul', 'FWD', 147, 31, 58, 'Petrol', 2022, 'Kia', 'Hatchback', 5, 400, 22000, 28000),
            Voiture(16, 'Volvo XC90', 'AWD', 250, 24, 70, 'Petrol', 2023, 'Volvo', 'SUV', 7, 900, 55000, 75000),
            Voiture(17, 'Chrysler Pacifica', 'FWD', 287, 22, 80, 'Petrol', 2022, 'Chrysler', 'Minivan', 7, 700, 35000, 45000),
            Voiture(18, 'Dodge Charger', 'RWD', 370, 19, 60, 'Petrol', 2022, 'Dodge', 'Sedan', 5, 500, 32000, 42000)
        ]
        
        if cursor.execute("SELECT COUNT() FROM voitures").fetchone()[0] == 0:
            print("yes")
            for voiture in voitures:
                insert_voiture(voiture)
            print("done")
            
        while True:
            print(" ")
            print("Menu:")
            print("1. Afficher les voitures")
            print("2. Filtrer les voitures")
            print("3. Ajouter une voiture")
            print("4. Mettre à jour une voiture")
            print("5. Supprimer une voiture")
            print("6. Quitter")
            option = input("Choisissez une option: ")
            print(" ")

            if option == '1':
                afficher_voitures()
                detail_option = input("Voulez-vous voir les détails d'une voiture? (oui/non): ").lower()
                if detail_option == 'oui':
                    id_input = input("Entrez l'ID de la voiture: ")
                    if id_input.isdigit():
                        afficher_voiture_details(id)
                    else:
                        print("Entrée invalide. Retour au menu.")
            elif option == '2':
                filters = {}
                filters['nom'] = input("Filtrer par nom [vide pour ignorer]: ") or None
                filters['transmission'] = input("Filtrer par transmission [vide pour ignorer]: ") or None
                results = select_voiture(filters)
                for result in results:
                    print(result)
            elif option == '3':
                n_voiture = add_voiture()
                insert_voiture(n_voiture)

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


#BUGS TO FIX:    
#FIX IGNORE GOES BACK TO MAIN
#FIX METTRE A JOUR
#FIX CLARITY OF INFORMATION
#FIX FILTER ONLY WORKS ON FIRST TWO CAUSE WE ONLY PUT TWO
