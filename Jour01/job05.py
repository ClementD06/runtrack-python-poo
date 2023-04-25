import string

class Animal():
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def nommer(self, nom):    
        self.prenom = nom

    def vieillir(self):
        self.age += 1
        if mon_animal.age >=2:
            print("Age de l'animal après vieillissement :" , mon_animal.age, "ans")
        elif mon_animal.age <=1:
            print("Age de l'animal après vieillissement :" , mon_animal.age, "an")
        
#Instanciation d'un objet animal      
mon_animal = Animal()

#Nommer l'animal
mon_animal.nommer("Médor")

#Affichage du nom complet de l'animal
print(f"L'animal se nomme : {mon_animal.prenom}")

#Affichage de l'attribut age
if mon_animal.age >=2:
            print("Age de l'animal :" , mon_animal.age, "ans")
elif mon_animal.age <=1:
            print("Age de l'animal :" , mon_animal.age, "an")
 
# print(f"Age de l'animal {mon_animal.age} an")

#Appel de la methode vieillir
mon_animal.vieillir()
            


