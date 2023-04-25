class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Je suis {self.nom} {self.prenom}"

personne1 = Personne("Dupuis", "Clément")
personne2 = Personne("Martin", "Marie")
personne3 = Personne("Gates", "Bill")

print(personne1.se_presenter())
print(personne2.se_presenter())
print(personne3.se_presenter())