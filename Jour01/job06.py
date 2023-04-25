class Rectangle():
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
# créer un rectangle avec longueur 10 et largeur 5
mon_rectangle = Rectangle(10, 5)

# afficher la longueur et la largeur
print("Longueur d'origine :", mon_rectangle.get_longueur()) # affiche 10
print("Largeur d'origine :", mon_rectangle.get_largeur()) # affiche 5

# modifier la longueur et la largeur
mon_rectangle.set_longueur(20)
mon_rectangle.set_largeur(10)

# afficher la longueur et la largeur après modification
print("Longueur après modification :", mon_rectangle.get_longueur()) # affiche 20
print("Largeur après modification :", mon_rectangle.get_largeur()) # affiche 8