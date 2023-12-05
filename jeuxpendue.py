import random

# Liste des mots possibles pour le jeu du pendu
mots = ["chien", "chat", "maison", "soleil", "arbre", "ecole", "livre", "jardin", "plage", "voiture",
        "fleur", "montagne", "rire", "cadeau", "bonheur", "musique", "ami", "pizza", "couleur", "ballon"]

# Dictionnaire pour stocker les informations du joueur
informations_joueur = {
    'parties_jouees': 0,
    'victoires': 0,
    'defaites': 0,
}

print(">> Bienvenue dans le pendu <<")

while True:
    # Sélection aléatoire d'un mot à deviner
    mot_a_deviner = random.choice(mots)
    
    # Initialisation de l'affichage du mot avec des underscores
    affichage_mot = "_ " * len(mot_a_deviner)
    
    # Initialisation de la liste des lettres déjà trouvées
    lettres_trouvees = ""
    # Initialisation du nombre de tentatives
    tentatives_restantes = 7

    while tentatives_restantes > 0:
        print("\nMot à deviner : ", affichage_mot)
        
        # Proposition de l'utilisateur (saisie de la première lettre)
        proposition = input("Proposez une lettre : ")[0].lower()

        if proposition in mot_a_deviner:
            # Ajout de la lettre à la liste des lettres trouvées
            lettres_trouvees += proposition
            print("-> Bien vu!")