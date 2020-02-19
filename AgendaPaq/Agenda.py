import shelve
from AgendaPaq.Contact import Contact
from AgendaPaq.SaisieInvalide import SaisieInvalide
# Class Agenda
class Agenda():
    """Agenda class agenda"""
    instance = None
    agenda = shelve.open("agenda.dat")

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            return cls.instance

    def afficher_titre(self):
        print("Mon Agenda")

    def afficher_menu(self):
        print("Taper 1: Pour ajouter un nouveau contact.")
        print("Taper 2: Pour afficher la liste.")
        print("Taper 3: Pour quitter.")

    def is_valid_name(self, name):
        name = str(name)
        name = name.replace(" ", "").replace("-", "")
        if not name.isalpha():
            return False
        return True

    def ajouer_contact(self):
        nom = input("taper le nom: ")
        if not self.instance.is_valid_name(nom):
            raise SaisieInvalide("Le nom : " + nom + " n'est pas valide")
        prenom = input("taper le prenom: ")
        if not self.instance.is_valid_name(prenom):
            raise SaisieInvalide("Le nom : " + prenom + " n'est pas valide")
        tel = input("taper le tel: ")
        email = input("taper le email: ")
        self.instance.agenda[tel] = Contact(nom, prenom, tel, email)

    def voir_contact(self):
        print("====" * 20)
        print('{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[3]:<20}'.format(('Nom', 'Prenom', 'Tel', 'Email')))
        print("====" * 20)
        for cle, contact in self.instance.agenda.items():
            # print( (contact))
            print(contact)
        print("====" * 20)

    def fermer_agenda(self):
        self.instance.agenda.close()
