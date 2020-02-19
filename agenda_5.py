import AgendaPaq.ContactLib
agenda=AgendaPaq.ContactLib.Agenda()
while True:
    agenda.afficher_titre()
    agenda.afficher_menu()
    saissie = input("Saissie: ")
    if saissie == "1":
        try:
            agenda.ajouer_contact()
        except AgendaPaq.ContactLib.SaisieInvalide as ex:
            print(ex)
        except Exception:
            print("Autre erreur")

    if saissie == "2" :
        agenda.voir_contact()
    if saissie =="3" :
        agenda.fermer_agenda()
        break
