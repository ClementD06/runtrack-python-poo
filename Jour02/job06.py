class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Année :", self.annee)
        print("Prix :", self.prix)

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4

    def demarrer(self):
        print("Vroum vroum, je démarre ma voiture")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roue)

    def demarrer(self):
        print("Vroum, je démarre ma moto")

ma_voiture = Voiture("Toyota", 2019, 25000)
ma_voiture.demarrer()

ma_moto = Moto("Harley Davidson", 2022, 30000)
ma_moto.demarrer()
ma_moto.informationsVehicule()


