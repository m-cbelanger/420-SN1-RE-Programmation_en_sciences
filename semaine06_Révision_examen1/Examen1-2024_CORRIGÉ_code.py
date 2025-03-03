#Corrigé examen 2024

import math
#question 6
def classement_rats(poids, longueur):
    if (poids < 300 or longueur < 22):
        return "petit"
    elif (poids >= 600 and longueur >27):
        return "grand"
    else:
        return "moyen"
print(classement_rats(350, 21))
print(classement_rats(450, 25))

#Question 8
def quad(a,b,c):
    reponse1 = -b/(2*a)
    reponse2 = (4*a*c-b**2)/(4*a)
    print(f"Le x du sommest est {reponse1} et le y du sommet est {reponse2}")

print(quad(1,8,3))

#Question 10
nom = "Léonard de Vinci"
annee_naissance = 1452
annee_deces = 1519
profession = "peintre"
vie = annee_deces-annee_naissance

print("Le scientifique", nom, "est un", profession, "qui a vécu", vie, "ans.")