# Démonstration en classe mercredi
# Comment faire pour imiter une boucle for avec une boucle while
n = 1
while n <= 4:
    print(f"le n vaut maintenant {n}")
    n = n + 1
    

mot_de_passe = ""
nombre_essais = 0
while mot_de_passe != "Password":
    mot_de_passe = input("Entrez votre mot de passe: ")
    nombre_essais = nombre_essais + 1

print(f"Il a fallu {nombre_essais} essais")

import random
# Faire 50 lancers d'un dé à 6 faces et compter combien de grand et de petit chiffres on a obtenu

n = 1
nombre_petits = 0
nombre_grands = 0
while n <= 50:
    lancer = random.randint(1,6)
    if lancer <= 3:
        nombre_petits = nombre_petits + 1
    else:
        nombre_grands = nombre_grands + 1

    n = n + 1

print(f"Après 50 lancers, on a eu {nombre_petits} petits chiffres et {nombre_grands} grands chiffres.")


# On lance le dé, mais on redemande après chaque lancer si on veut rejouer

def question_des():
    nombre_grands = 0
    nombre_petits = 0
    reponse = "oui"
    while reponse == "oui" or reponse == "Oui" or reponse == "o":
        lancer = random.randint(1,6)
        print(f"Le dé obtenu est {lancer}")
        if lancer <= 3:
            nombre_petits = nombre_petits + 1
        else:
            nombre_grands = nombre_grands + 1
        reponse = input("Entrez oui pour rejouer")
    
    
    print(f"On a eu {nombre_petits} petits chiffres et {nombre_grands} grands chiffres.")


question_des()
