import shelve


class Contact():
    """ Class contact pour creer des objet de type contact"""
    def __init__(self,nom, prenom, tel, email):
        self.nom=nom
        self.prenom=prenom
        self.tel=tel
        self.email=email
    def __str__(self):
        return '{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[2]:<20}'.format((self.nom, self.prenom, self.tel, self.email))

class Agenda():
    instance= None
    agenda = shelve.open("agenda.dat")

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=object.__new__(cls)
            return  cls.instance

    def afficher_titre(self):
         print("Mon Agenda")

    def afficher_menu(self):
        print("Taper 1: Pour ajouter un nouveau contact.")
        print("Taper 2: Pour afficher la liste.")
        print("Taper 3: Pour quitter.")

    def ajouer_contact(self):
        nom = input("taper le nom: ")
        prenom = input("taper le prenom: ")
        tel = input("taper le tel: ")
        email = input("taper le email: ")
        self.instance.agenda[tel]=Contact(nom, prenom, tel, email)

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