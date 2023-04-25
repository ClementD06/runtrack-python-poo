class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien."
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Identifiant : {self.__num_etudiant}")
        print(f"Niveau : {self.__level}")

# Exemple d'utilisation
john_doe = Student("Doe", "John", 85)
john_doe.add_credits(30)
john_doe.add_credits(40)
john_doe.add_credits(20)
john_doe.student_info()
