import time
 
def menu():
    """
    menu affiche les différents choix de l’utilisateur
    Entrée : saisi de l’utilisateur (choix de la fonctionnalité)
    Résultat : retourne le choix de l’utilisateur
    """
    choix = int(input("Saisissez 0 pour quitter l'annuaire\nSaisissez 1 pour enregistrer\nSaisissez 2 pour rechercher dans le repertoire\n\nVotre choix ?"))
 
    if choix == 0:
        choix0()
 
    elif choix == 1:
        saisie_tab()
 
    elif choix == 2:
        rechercher()
 
    elif choix == 3:
        afficher()
 
    else:
        print("Réessayez, saissisez 0, 1 ou 2\n")
        menu()
 
def choix0():
    """
    choix0 affiche le message de sortie
    Entrée : utilisé si menu renvoie 0
    Résultat : fin de programme
    """
    print("Vous quittez l'annuaire...")
    time.sleep(2)
    quit()

  
def saisie_tab():
    """
    choix1 envoie l’utilisateur au menu d'enregistrement
    Entrée : saisi de l’utilisateur (choix de la fonctionnalité)
    Résultat : retourne le choix de l’utilisateur
    """
  
nom=input("Entrez ci-dessous le nom de la personne que vous enregistrez dans l'annuaire\n")
prenom =input("Entrez ci-dessous le prenom de la personne que vous enregistrez dans l'annuaire\n")
numero =int(input("Veuillez saisir votre numero :"))
telephone = input("Entrez le numéro de téléphone de la personne")
nomdelarue=input("veuillez donner le nomde la rue:")
ville=input("veuillez donner la ville:")
codepostal =int(input("Veuillez saisir votre code postal:"))
with open("file.txt", "a") as fichier:
   fichier.write(nom+" "+prenom+" "+numero+" "+telephone+" "+nomdelarue+" "+ville+" "+codepostal+"\n")

menu()
def rechercher():
    """
    choix2 envoie l’utilisateur au menu de recherche
    Entrée : saisi de l’utilisateur (choix de la fonctionnalité)
    Résultat : retourne le choix de l’utilisateur
    """
    choix2 = input("Entrez ci-dessous le nom de la personne que vous voulez rechercher\n")
    annuaire = []
    with open("file.txt", "r") as fichier:
        for ligne in fichier:
            ligne=ligne.replace("\n","")
            ligne=ligne.split()
            annuaire.append(ligne)
        for elem in annuaire:
            if choix2 == elem[0]:
                print("Le numéro associé est : ", elem[1],"\n")
    menu()
     
menu()
