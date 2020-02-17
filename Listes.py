
listeInitiale=[1,43,8,-23,12,-67,42,8,21,-12,-42,-8,21,-12,-42,-61,8,17,42]
nouvelleListe=[]

#print(dir(listeInitiale))
for value in listeInitiale:
    index=listeInitiale.index(value)
    listeInitiale[index]= abs(value)

for value in listeInitiale:
    if value not in nouvelleListe:
        nouvelleListe.append(abs(value))

nouvelleListe.sort()
print(nouvelleListe)