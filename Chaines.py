chaine=input("Ecrivez une phraase: \n");
chaine=str(chaine)

# on crée la liste des voyelles
liste_voyelles = ["a", "e", "i", "o", "u", "y"]

# on initialise le compteur de voyelles
nb_voyelles = 0
nb_consone=0;
# la boucle de comptage
for lettre in chaine:
    if lettre in liste_voyelles:
        nb_voyelles += 1

for lettre in chaine.replace(" ", ""):
    if lettre not in liste_voyelles and lettre.isalpha():
        nb_consone += 1

print("taile totale: %d" % len(chaine))
print("Nombre de voyelle: %d" % (nb_voyelles))
print("Nombre de consonne: %d" % nb_consone)
print("Nombre de mot: %d" % len(chaine.split()))