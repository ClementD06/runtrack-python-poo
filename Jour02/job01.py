class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        if self.age == 14:
            print("J'ai 14 ans")
        else:
            print("L'âge de la personne modifié est", self.age, "ans")

    def bonjour(self):
        print('Hello')

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def __init__(self, age=14):
        super().__init__(age)

    def allerEnCours(self):
        print('Je vais en cours')

    def affichageAge(self):
        super().afficherAge()


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours de", self.__matiereEnseignee, "va commencer")


    


p1 = Personne()
p1.bonjour()
p1.afficherAge()
p1.modifierAge(30)
p1.afficherAge()

p2 = Eleve(age=14)
p2.allerEnCours()
p2.affichageAge()

p3 = Professeur("maths")
p3.enseigner()
