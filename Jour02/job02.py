class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        if self.age == 14:
            print("J'ai 14 ans")
        

    def bonjour(self):
        print("Bonjour")

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def __init__(self, age=15):
        super().__init__(age)
    
    def bonjour_2(self):
        print("Bonjour")

    def allerEnCours(self):
        print('Je vais en cours')

    def affichageAge(self):
        super().afficherAge()
        print("Je suis l'eleve, j'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print('Le cours va commencer')


p2 = Eleve(age=15)
p2.bonjour()
p2.affichageAge()
p2.allerEnCours()

prof = Professeur('maths', 40)
prof.bonjour()
prof.enseigner()

