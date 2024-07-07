noms=[]

def demander_nom():
    global noms
    while True:
        nom = input(" Veuillez entrer le nom : ")
        if nom == "":
            break
        noms.append(nom)

def afficher_nom(noms):
    noms.sort() #trier la liste (ordre alphabetique)
    print("Nom des personnes :")
    for i in noms:
        print(i)
 
print(""" ------ Bienvenue ------
      Vous devez remplir une liste de noms 
      veuillez entrer un nom vide pour finir 

""")
demander_nom()
afficher_nom(noms)