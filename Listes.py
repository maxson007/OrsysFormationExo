
listeInitiale=[1,43,8,-23,12,-67,42,8,21,-12,-42,-8,21,-12,-42,-61,8,17,42]
nouvelleListe=[]
listeSansValeurNegatif=[]
#print(dir(listeInitiale))
for value in listeInitiale:
    listeSansValeurNegatif.append(abs(value))

for value in listeSansValeurNegatif:
    if value not in nouvelleListe:
        nouvelleListe.append(abs(value))

nouvelleListe.sort()
print(nouvelleListe)