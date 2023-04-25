class Rectangle():
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimètre(self):
        print("Perimetre du rectangle :" ,self.__longueur + self.__largeur * 2,"cm")

    def surface(self):
        print("Surface du rectangle : ", self.__longueur * self.__largeur,"cm²")

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # mutateurs
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        print("Volume :",self.get_longueur() * self.get_largeur() * self.__hauteur,"cm3")



rec = Rectangle(5,8)
par = Parallélépipède(4,8,12)

rec.perimètre()
rec.surface()

print("Longueur d'entrée :",rec.get_longueur(),"cm")
print("Largeur d'entrée :", rec.get_largeur(),"cm")  

rec.set_longueur(10)
rec.set_largeur(20)

print("Longueur modifiée :", rec.get_longueur(), "cm")  
print("Largeur modifiée :", rec.get_largeur(), "cm")  
par.volume()