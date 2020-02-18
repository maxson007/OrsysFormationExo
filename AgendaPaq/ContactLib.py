
listeContact=[]
def ajouer_contact():
    nom = input("taper le nom: ")
    prenom = input("taper le prenom: ")
    tel = input("taper le tel: ")
    email = input("taper le email: ")
    listeContact.append(tuple((nom, prenom, tel, email)))

def voir_contact():
    print("====" * 20)
    print('{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[3]:<20}'.format(('Nom', 'Prenom', 'Tel', 'Email')))
    print("====" * 20)
    for contact in listeContact:
        # print( (contact))
        print('{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[2]:<20}'.format(contact))
    print("====" * 20)