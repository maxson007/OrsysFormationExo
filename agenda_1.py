import AgendaPaq.ContactLib
while True:
    print("Taper 1: Pour ajouter un nouveau contact:")
    print("Taper 2: Pour afficher la liste:")
    print("Taper 3: Pour quitter:")
    saissie=input("Saissie: ")
    if saissie == "1":
        AgendaPaq.ContactLib.ajouer_contact()

    if saissie == "2" :
        AgendaPaq.ContactLib.voir_contact()
    if saissie =="3" : break
