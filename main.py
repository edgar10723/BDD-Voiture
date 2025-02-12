import sqlite3

conn = sqlite3.connect('BDD_Voiture.db')
cursor = conn.cursor()

def lien_fichier(db_file):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        print("Connection to the database established.")

if __name__ == "__main__":
    lien_fichier('Voiture.db')

#REQUETE------------------------------------------------------------------------------------------------------------------------------------
#LIST DE V
id_voiture_1 = Voiture('Ford Mustang', 'RWD', 450, 10, 60, 'Petrol', 2022, 'Ford', 'Coupe', 4, 300, 70000, 120000)


#INSERT

def insert_voiture(voiture):
  with conn: #for insert, update, remove use with conn:
    cursor.execute("INSERT INTO voitures VALUES (:nom,	:transmission,	:puissance,	:kpl,	:reservoir,	:engin,	:annee,	:marque,	:type,	:sieges,	:espace,	:prix_utlise,	:prix_nouveau)",  {
    'nom': voiture.nom,
    'transmission': voiture.transmission,
    'puissance': voiture.puissance,
    'kpl': voiture.kpl,
    'reservoir': voiture.reservoir,
    'engin': voiture.engin,
    'annee': voiture.annee,
    'marque': voiture.marque,
    'type': voiture.type,
    'sieges': voiture.sieges,
    'espace': voiture.espace,
    'prix_utlise': voiture.prix_utlise,
    'prix_nouveau': voiture.prix_nouveau
})


#SUPPRIMER

def rm_voiture(voiture):
    with conn:
        cursor.execute("DELETE FROM voitures WHERE nom = :nom", {
            'nom': voiture.nom
        })
























#OLD VERSION OLD VERSION OLD VERSION OLD VERSION OLD VERSION OLD VERSION OLD VERSION OLD VERSION OLD VERSION OLD VERSION OLD VERSION OLD VERSION 


#FILTRE
cursor.execute('''
SELECT * FROM voitures
WHERE nom = {attribut}) 
AND transmission = {attribut}) 
AND puissance BETWEEN {value} AND {value} 
AND kpl BETWEEN {value} AND {value}
AND
reservoir BETWEEN {value} AND {value}
AND
engin = {attribut}
AND
annee BETWEEN {value} AND {value}
AND
marque {attribut}
AND
type {attribut}
AND
siege {attribut}
AND
espace BETWEEN {value} AND {value}
AND
prix_utilise BETWEEN {value} AND {value}
AND
prix_nouveau BETWEEN {value} AND {value}
AND
classement = {attribut}
''')

#REQUETE UTILISATEUR

def add_voiture(nom, transmission,	puissance,	kpl,	reservoir,	engin,	annee,	marque,	type,	sieges,	espace,	prix_utlise,	prix_nouveau):
    nom = input("Nom de la voiture: ")
    transmission = 
    puissance = float(input("Entrer la puissance du vehicule: "))
    kpl = float(input("Entrer le KPL(kilometre par littre: "))
    reservoir = float(input("Entrer le KPL(kilometre par littre: "))
    engin = input("Type d'engin")
    annee = float(input("Entrer le KPL(kilometre par littre: "))
    marque = input("Nom de la marque")
    type = 
    sieges = float(input("Entrer le KPL(kilometre par littre: "))
    espace = float(input("Entrer le KPL(kilometre par littre: "))
    prix_utilise = float(input("Entrer le KPL(kilometre par littre: "))
    prix_nouveau = float(input("Entrer le KPL(kilometre par littre: "))


    cursor.execute('''
    INSERT INTO voiture VALUES()
    ''', (nom, transmission,	puissance,	kpl,	reservoir,	engin,	annee,	marque,	type,	sieges,	espace,	prix_utlise,	prix_nouveau))
    conn.commit()

def update_voiture(nom, transmission,	puissance,	kpl,	reservoir,	engin,	annee,	marque,	type,	sieges,	espace,	prix_utlise,	prix_nouveau):
    cursor.execute('''
    UPDATE INTO voiture VALUES()
    ''', (nom, transmission,	puissance,	kpl,	reservoir,	engin,	annee,	marque,	type,	sieges,	espace,	prix_utlise,	prix_nouveau))
    conn.commit()

def delete_voiture(nom, transmission,	puissance,	kpl,	reservoir,	engin,	annee,	marque,	type,	sieges,	espace,	prix_utlise,	prix_nouveau):
    cursor.execute('''
    DELETE FROM voiture VALUES()
    ''', (nom, transmission,	puissance,	kpl,	reservoir,	engin,	annee,	marque,	type,	sieges,	espace,	prix_utlise,	prix_nouveau))
    conn.commit()




#MAIN------------------------------------------------------------------------------------------------------------------------


def main():
    if lien_fichier('BDD_Voiture.db') = True
        print("Menu:")
        print("1 Afficher les voitures")
        print("2 Filtrer les voitures")
        print("3 Ajouter une voiture")
        print("4 Mettre à jour une voiture")
        print("5 Supprimer une voiture")
        print("6 Quitter")
        option = input("Choisissez une option: ")
        if option == '1':
            afficher_voitures()
        if option == '2':
            filtre_voitures()
        if option == '3':
            add_voitures()
        if option == '4':
            update_voitures()
        if option == '5':
            delete_voitures()
        if option == '6':
            exit()
        else:
            print("Erreur")
            
       

def afficher_voitures():
    cursor.execute("SELECT voiture FROM voitures")
    voiture = cursor.fetchall()
    print(voitures)


def filtre():
nom = input("Filtrer par nom [vide pour ignorer]: ") 
transmission = input("Filtrer par transmission [vide pour ignorer]: ")  #cm
puissance = input("Filtrer par nom [vide pour ignorer]: ") #cm
kpl = input("Filtrer par nom [vide pour ignorer]: ") #cm
reservoir = input("Filtrer par nom [vide pour ignorer]: ") #cm
engin = input("Filtrer par nom [vide pour ignorer]: ") #cm
annee = input("Filtrer par nom [vide pour ignorer]: ") 
marque = input("Filtrer par nom [vide pour ignorer]: ") 
type = input("Filtrer par nom [vide pour ignorer]: ") 
siege = input("Filtrer par nom [vide pour ignorer]: ") 
espace = input("Filtrer par nom [vide pour ignorer]: ") 
prix_utilise = input("Filtrer par nom [vide pour ignorer]: ") 
prix_nouveau = input("Filtrer par nom [vide pour ignorer]: ") 
classement = 
