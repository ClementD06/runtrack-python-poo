class Livre():
    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages       

    def get_titre(self):
        return self.titre
    
    def set_titre(self, titre):
        self.titre = titre
        
    def get_auteur(self):
        return self.auteur
    
    def set_auteur(self, auteur):
        self.auteur = auteur

    def get_nb_pages(self):
        return self.nb_pages
    
    def set_nb_pages(self, nb_pages):
        if nb_pages is None:
            print("Le nombre de pages ne peut pas être nul.")
        elif isinstance(nb_pages, int):
            self.nb_pages = nb_pages
            print("Ce Livre contient", nb_pages, "pages.")
        else:
            print("Le nombre de pages doit être un entier.")
        


mon_livre = Livre("J'apprends à développer","Clément Dupuis", None)

mon_livre.set_nb_pages(50)

nb_pages = mon_livre.get_nb_pages()


print("Le titre du livre est :", mon_livre.get_titre())
print("L'auteur du livre est :", mon_livre.get_auteur())


