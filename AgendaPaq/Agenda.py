import shelve
import re
from AgendaPaq.Contact import Contact
from AgendaPaq.SaisieInvalide import SaisieInvalide
from AgendaPaq.ContactMySqlDA import ContactMysqlDA


# Class Agenda
"""
Documentation Agenda
"""
class Agenda():
    """Agenda class agenda"""
    instance = None
    agendaDB = ContactMysqlDA()

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

    def is_valid_name_expr(self, name):
        regex = "^[A-Za-z\s\-]+$"
        return re.match(regex, name) != None

    def is_valid_phone_number(self, phone_number):
        return re.match("^[+]?[0-9]{,15}$", phone_number) != None

    def is_valid_email(self, email):
        return re.match("^[a-z0-9\-\_\.]+@[a-z0-9\.\-]+\.[a-z]{2,}$", email) != None

    def ajouer_contact(self):
        nom = input("taper le nom: ")
        if not self.is_valid_name_expr(nom):
            raise SaisieInvalide("Le nom : " + nom + " n'est pas valide")

        prenom = input("taper le prenom: ")
        if not self.is_valid_name_expr(prenom):
            raise SaisieInvalide("Le nom : " + prenom + " n'est pas valide")

        tel = input("taper le tel: ")
        if not self.is_valid_phone_number(tel):
            raise SaisieInvalide("Le numero de tel  : " + tel + " n'est pas valide")

        email = input("taper le email: ")
        if not self.is_valid_email(email):
            raise SaisieInvalide("L'email  : " + email + " n'est pas valide")
        self.agendaDB.insert(Contact(nom, prenom, tel, email))
        # self.agenda[tel] = Contact(nom, prenom, tel, email)

    def voir_contact(self):
        print("====" * 20)
        print('{0[0]:<20} {0[1]:<20} {0[2]:<20} {0[3]:<20}'.format(('Nom', 'Prenom', 'Tel', 'Email')))
        print("====" * 20)
        contacts = self.agendaDB.get_all();
        for cle, contact in contacts.items():
            print(contact)
        print("====" * 20)

    def fermer_agenda(self):
        self.agendaDB.close()
