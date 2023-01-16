

import csv
raison = []
adresse1 = []
adresse2 = []
categorie = []
produit = []
quantite = []
prixUnitaire = []
date = []

nom = []
nomProduit = []

idClient = []
idProduit =[]

countCli = 0
countProd = 0
countComm = 0

def egalite(ch2, test):
    count = 0
    for ch1 in test:
        count = count + 1
        if ch1 == ch2:
            return True
    return False

def readColCSV(fichier, countCli, countProd, countComm):
    file = open( fichier , "r")
    reader = csv.reader(file)
    test = ""
    for row in reader:
        if egalite(row[0],raison) == False:
            countCli = countCli + 1
            raison.append(row[0])
            adresse1.append(row[1])
            adresse2.append(row[2])
        if egalite(row[4], produit) == False :
            countProd = countProd + 1
            categorie.append(row[3])
            produit.append(row[4])
            prixUnitaire.append(row[6])
        test1 = str(row[0]) + str(row[4])
        if (egalite(row[7],date) == False) | (test != test1) :
            countComm = countComm + 1
            nom.append(row[0])
            nomProduit.append(row[4])
            quantite.append(row[5])
            date.append(row[7])
        test = str(row[0]) + str(row[4])
    file.close()
    return [countCli, countProd, countComm]

def taille(objet):
    taille = 0
    for val in objet :
        taille = taille +1
    return taille
def writeCSVclient():
    idClient = 0
    t = taille(raison)
    f = open('client.csv', 'w')

    while idClient < t:
        f.write(str(idClient) + ",")
        f.write(str(raison[idClient]) + ",")
        f.write(str(adresse1[idClient] + ","))
        f.write(str(adresse2[idClient]))
        f.write("\n")
        idClient = idClient + 1
    f.close()

def writeCSVproduit():
    idProduit =0
    t = taille(produit)
    f = open('produit.csv', 'w')

    while idProduit < t:
        f.write(str(idProduit)+ ",")
        f.write(str(produit[idProduit])+",")
        f.write(str(categorie[idProduit]+","))
        f.write(str(prixUnitaire[idProduit]))
        f.write("\n")
        idProduit= idProduit +1

    f.close()
def pos(idCommandes, liste, liste2) :
    compteur = 0
    for i in liste :
        if i == liste2[idCommandes] :
            return compteur
        compteur = compteur + 1

def writeCSVcommandes():
    idCommandes = 0
    t = taille(quantite)
    test = False
    f = open('commandes.csv', 'w')

    while idCommandes < t:
        f.write(str(idCommandes)+ ",")
        f.write(str(pos(idCommandes, raison, nom))+",")
        idClient.append(pos(idCommandes, raison, nom))
        f.write(str(pos(idCommandes, produit, nomProduit))+",")
        idProduit.append(str(pos(idCommandes, produit, nomProduit)))
        f.write(str(quantite[idCommandes])+",")
        f.write(date[idCommandes])
        f.write("\n")
        idCommandes= idCommandes +1

    f.close()

def menu() :
    print("bonjour et bienvenu sur le menu de l'application de statistique de l'entreprise ! \n Que souhaitez vous faire ?\n")
    print("1 : Afficher le nombre de clients, nombre de produit, nombre de commandes\n")
    print("2 : Afficher le nombre moyen de commandes par client\n")
    print("3 : Afficher le nombre max de commandes\n")
    print("4 : Afficher la moyenne du nombre de produit commandés par catégorie\n")
    print("5 : Afficher le maximum de produit commandés par catégories\n")
    print("6 : Quitter l'application")
    valeur = input("tapez un nombre : \n")
    if( valeur == "1") :
        print("Clients : " + str(countCli) + "\n Produits : " + str(countProd) + "\nCommandes :" + str(countComm))

    elif valeur == "2" :
        moy = moyenne()
        print("La moyenne du nombre de commandes par personne est : " + str(moy))

    elif valeur == "3" :
        concat = maximum()
        var = concat.split(",")
        print("Le client numéro " + var[0] + " est celui ayant réalisé le plus de commandes avec " + var[1] +" commandes.")

    elif valeur == "4":
        moy = moyenne2()
        print("La moyenne du nombre de produit commandé par catégorie est : " + str(moy))

    elif valeur == "5" :
        concat = maximum()
        var = concat.split(",")
        print("La catégorie numéro " + var[0] + " est celle avec le plus de produits commandés avec " + var[
            1] + " produits.")

    elif valeur == "6":
        print("A bientôt !")
        return True
    else :
        print("la valeur que vous avez rentré ne correspond à aucune fonctionalité veuillez réessayer !")
    return False

#les fonctions suivantes sont les fonctionnalitées du menu :

def isIn(index, client):
    compteur = 0
    if(taille(index) > 1) :
        for i in index :
            if i == client :
                return compteur
            compteur = compteur +1
    elif(taille(index) >1) :
        if index[0] == client:
            return compteur
    return -1
def commandesParClients():
    index = []
    nombre = []
    compteur = [ index,nombre]
    count = 0
    for i in idClient :
        state = isIn(compteur[0], i)
        if(state == -1) :
            compteur[0].append(i)
            compteur[1].append(1)
        else :
            chaine = compteur[1][state] + 1
            compteur[1][state] = chaine
    return compteur
def maximum() :
    compteur = commandesParClients()
    t = taille(compteur[0])
    i=0
    maximum = -1
    idMax = -1
    while(i<t):
        if compteur[1][i] > maximum :
            maximum = compteur[1][i]
            idMax = i
        i=i+1
    concat = str(idMax)+ "," + str(maximum)

    return concat
def rassemblerCat():
    cat = []
    for i in categorie :
        if i not in cat :
            cat.append(i)
    return cat
def commandesParProduit() :

    quantiteParCat = []
    listeCategorie = rassemblerCat()
    for y in listeCategorie :
        count = 0
        quantiteParCat.append(0)
        for i in produit :
            if categorie[count] == y :
                if quantite[count] != "quantité" :
                    quantiteParCat[-1] = quantiteParCat[-1] + int(quantite[count])

            count = count +1
    return quantiteParCat

def moyenne():
    compteur = commandesParClients()
    moy =0
    count =0
    for i in compteur[1] :
        moy = moy + i
        count = count +1
    return moy/count

def moyenne2() :
    compteur = commandesParProduit()
    moy = 0
    count =0
    for i in compteur :
        moy = moy + i
        count = count + 1
    return moy / count
def max2() :
    compteur = commandesParProduit()
    t = taille(compteur)
    i = 0
    maximum = -1
    idMax = -1
    while (i < t):
        if compteur[i] > maximum:
            maximum = compteur[i]
            idMax = i
        i = i + 1
    concat = str(idMax) + "," + str(maximum)

    return concat

#Correspond au main :
tab = readColCSV("transactions.csv", countCli, countProd, countComm)
countCli = tab[0]
countProd = tab[1]
countComm = tab[2]
writeCSVclient()
writeCSVproduit()
writeCSVcommandes()
state = False
while state == False :
    state = menu()




writeCSVcommandes()


