import shelve
agenda = shelve.open("agenda.dat")

class Contact():
    """ Class contact pour creer des objet de type contact"""
    def __init__(self,nom, prenom, tel, email):
        self.nom=nom
        self.prenom=prenom
        self.tel=tel
        self.email=email
    def __str__(self):
        return '{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[2]:<20}'.format((self.nom, self.prenom, self.tel, self.email))

def ajouer_contact():
    nom = input("taper le nom: ")
    prenom = input("taper le prenom: ")
    tel = input("taper le tel: ")
    email = input("taper le email: ")
    agenda[tel]=Contact(nom, prenom, tel, email)

def voir_contact():
    print("====" * 20)
    print('{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[3]:<20}'.format(('Nom', 'Prenom', 'Tel', 'Email')))
    print("====" * 20)
    for cle, contact in agenda.items():
        # print( (contact))
        print(contact)
    print("====" * 20)

def fermer_agenda():
    agenda.close()