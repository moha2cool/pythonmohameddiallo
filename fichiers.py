def nbMotsAvecVoyelle(phrase):
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    nomf = phrase.lower().split()
    compte = 0
    
    for mot in nomf:
        if mot[0] in voyelles:
            compte += 1
    
    return compte

    
 

phrase = "Une phrase avec des mots commençant par une voyelle"
phrase = str(input("Saisir la phrase : "))
resultat = nbMotsAvecVoyelle(phrase)
print(resultat) 
