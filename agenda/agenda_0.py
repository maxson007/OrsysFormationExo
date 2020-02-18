listeContact=[]


while True:
    print("Taper 1: Pour ajouter un nouveau contact:")
    print("Taper 2: Pour afficher la liste:")
    print("Taper 3: Pour quitter:")
    saissie=input("Saissie: ")
    if saissie == "1":
        nom=input("taper le nom: ")
        prenom=input("taper le prenom: ")
        tel=input("taper le tel: ")
        email=input("taper le email: ")
        listeContact.append(tuple((nom, prenom,tel,email)))

    if saissie == "2" :
        print("===" * 30)
        print('{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[3]:<20}'.format(('Nom', 'Prenom', 'Tel', 'Email')))
        print("==="*30)
        for contact in listeContact:
           #print( (contact))
           print('{0[0]:<20} {0[1]:<20} {0[2]:<10} {0[2]:<20}'.format(contact))
        print("===" * 30)
    if saissie =="3" : break
