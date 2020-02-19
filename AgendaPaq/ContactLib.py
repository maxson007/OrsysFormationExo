import shelve


class Contact():
    """ Class contact pour creer des objet de type contact"""

    def __init__(self, nom, prenom, tel, email):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email

    def __str__(self):
        return '{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[2]:<20}'.format((self.nom, self.prenom, self.tel, self.email))

#Exception de saissie invalide
class SaisieInvalide(Exception):
    def __init__(self, valeur):
        self.valeur=valeur

    def __str__(self):
        return repr(self.valeur)

#Class Agenda
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
        name=str(name)
        name=name.replace(" ","").replace("-","")
        if not name.isalpha():
            return False
        return True

    def ajouer_contact(self):
        nom = input("taper le nom: ")
        if not self.instance.is_valid_name(nom):
            raise SaisieInvalide("Le nom : "+nom+" n'est pas valide")
        prenom = input("taper le prenom: ")
        if not self.instance.is_valid_name(prenom):
            raise SaisieInvalide("Le nom : "+prenom+" n'est pas valide")
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
