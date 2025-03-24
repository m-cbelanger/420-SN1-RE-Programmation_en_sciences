import math
import random

def portee_projectile(vitesse, angle):
    if angle >=90 or angle <0:
        print("L'angle doit être entre 0 et 89.9")
        return 0
    else:
        g= 9.81
        portee = vitesse**2*math.sin(2*angle*math.pi/180)/g
        return portee

#a = float(input("Entrez l'angle initial en degrés: "))
#v = float(input("Entrez la vitesse initiale en m/s: "))
#print(f"La portée sera de {portee_projectile(v,a):.2f} mètres")

def medicament(type_animal,poids):
    if type_animal == "chien" and poids < 15:
        dose = 1
    elif type_animal == "chien" and poids <=45:
        dose = 2
    elif type_animal == "chat" and poids < 4:
        dose = 0.5
    elif type_animal == "chat" and poids <= 20:
        dose = 1
    else:
        dose = 0
    return dose

print(medicament("chien", 5))
print(medicament("chien", 20))
print(medicament("chat", 2))
print(medicament("chat", 15))
print(medicament("chien", 60))

def jeu_hasard():
    nombre1 = random.randint(1,10)
    nombre2 = int(input("Choissez un nombre entre 1 et 10: "))
    if nombre2 == nombre1:
        print(f"Vous avez gagné!")
    else:
        print(f"Vous avez perdu! Vous étiez à {nombre2-nombre1} du chiffre pigé!")
    
jeu_hasard()

  