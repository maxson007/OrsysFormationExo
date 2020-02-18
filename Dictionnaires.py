dico={'r':3, 'a':0,'y':5, 'z':1, 't':4, 'e':2}


dicoKeys=dico.keys()
dicoValues=dico.values()

for key in sorted(dicoKeys):
    for value in sorted(dicoValues):
        if dico.get(key)==value:
            print("%s=>%s" %(key, dico.get(key)))