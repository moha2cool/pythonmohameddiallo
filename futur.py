def saisie():
    noms = []
    while True:
        nom = input("Saisissez un nom: ")
        if nom == 'q':
            break
            noms.append(nom)
    return noms

  
personnes = saisie()
print(personnes)



import random

def saisie_voyage(noms):
    for personne in noms:
        periode = random.randint(-10000, 10000)
        print(periode)

personnes = noms
saisie_voyage(personnes)
