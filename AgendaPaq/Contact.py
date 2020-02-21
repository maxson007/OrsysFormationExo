class Contact:
    """ Class contact pour creer des objet de type contact"""

    def __init__(self, nom, prenom, tel, email):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email

    def __str__(self):
        return '{0[0]:<20} {0[1]:<20} {0[2]:<20} {0[3]:<20}'.format((self.nom, self.prenom, self.tel, self.email))
