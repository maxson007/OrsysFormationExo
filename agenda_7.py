from AgendaPaq.Agenda import Agenda
from AgendaPaq.SaisieInvalide import SaisieInvalide
if __name__== "__main__":
    agenda= Agenda()
    agenda.afficher_titre()
    while True:
        agenda.afficher_menu()
        saissie = input("Saissie: ")
        if saissie == "1":
            try:
                agenda.ajouer_contact()
            except SaisieInvalide as ex:
                print(ex)
            except Exception as e:
                print(e)

        if saissie == "2" :
            agenda.voir_contact()
        if saissie =="3" :
            agenda.fermer_agenda()
            break
