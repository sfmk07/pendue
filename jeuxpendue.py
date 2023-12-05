import random

# Liste des mots possibles pour le jeu du pendu
mots = ["chien", "chat", "maison", "soleil", "arbre", "ecole", "livre", "jardin", "plage", "voiture",
        "fleur", "montagne", "rire", "cadeau", "bonheur", "musique", "ami", "pizza", "couleur", "ballon"]

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
        else:
            # Réduction du nombre de tentatives en cas d'erreur
            tentatives_restantes -= 1
            print("-> Nope\n")
            
            # Affichage du pendu progressif
            if tentatives_restantes == 0:
                print(" ==========Y= ")
            if tentatives_restantes <= 1:
                print(" ||/       |  ")
            if tentatives_restantes <= 2:
                print(" ||        0  ")
            if tentatives_restantes <= 3:
                print(" ||       /|\\ ")
            if tentatives_restantes <= 4:
                print(" ||       / \\ ")
            if tentatives_restantes <= 5:
                print("/||           ")
            if tentatives_restantes <= 6:
                print("==============\n")

        # Mise à jour de l'affichage du mot en fonction des lettres trouvées
        affichage_mot = " ".join([lettre + " " if lettre in lettres_trouvees else "_ " for lettre in mot_a_deviner])

        # Vérification si toutes les lettres ont été trouvées
        if "_" not in affichage_mot:
            print(f">>> Gagné! Le mot était : {mot_a_deviner} <<<")
            break

    print("\n    * Fin de la partie *    ")
    rejouer = input("Voulez-vous rejouer ? (O/N) ").lower()
    if rejouer != 'o':
        break