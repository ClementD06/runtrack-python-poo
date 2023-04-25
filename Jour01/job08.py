class Livre():
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True   
    
    def get_titre(self):
        return self.titre
    
    def get_auteur(self):
        return self.auteur
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Le livre \"{self.titre}\" a été emprunté.")
        else:
            print(f"Le livre \"{self.titre}\" n'est pas disponible pour l'emprunt.")
    
    def rendre(self):
        if not self.disponible:
            self.disponible = True
            print(f"Le livre \"{self.titre}\" a été rendu.")
        else:
            print(f"Le livre \"{self.titre}\" a déjà été rendu.")
        

# Créer les objets Livre
livre1 = Livre("Mission Apollo 13", "Neil Armstrong")
livre2 = Livre("L'histoire de Tesla", "Nicolas Tesla")

# Stocker les objets Livre dans une liste
liste_livres = [livre1, livre2]

# Afficher les titres des livres disponibles
print("Listes des livres :")
for livre in liste_livres:
    print(livre.get_titre(),"écrit par" ,livre.get_auteur())

# Afficher les éléments de la liste
print("Les éléments disponibles sont :")
for i, livre in enumerate(liste_livres):
    print(f"{i+1}. {livre.titre} {'(disponible)' if livre.disponible else '(indisponible)'}")

# Demander à l'utilisateur de faire un choix
choix = input("Choisissez un élément (1 ou 2) : ")

# Vérifier si le choix est valide
if choix == '1':
    choix_livre = livre1
elif choix == '2':
    choix_livre = livre2
else:
    print("Choix invalide.")

# Afficher le choix de l'utilisateur
if choix_livre:
    print(f"Vous avez choisi : {choix_livre.titre}")
    
    # Demander à l'utilisateur s'il veut emprunter ou rendre le livre
    action = input("Voulez-vous emprunter (e) ou rendre (r) le livre ? ")
    
    # Vérifier si l'action est valide
    if action == 'e':
        choix_livre.emprunter()
    elif action == 'r':
        choix_livre.rendre()
    else:
        print("Action invalide.")