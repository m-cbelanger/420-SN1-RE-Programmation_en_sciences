# Exercices pour la structure conditionnelle

1. Faire une fonction qui prend le pH d'une solution et qui **retourne** une chaîne de caractères qui dit si la solution est acide, basique ou neutre. On considère qu'un pH est acide s'il est inférieur à 7, neutre s'il est égal à 7 et basique s'il est supérieur à 7. À l'extérieur de cette fonction, demander à un utilisateur d'entrer un pH et appelez votre fonction avec sa réponse.

2. Faire une fonction qui prend une température corporelle en degrés Celsius. Si la température est en haut de 37.5, **afficher** qu'il fait de la fièvre. Si la température est en bas de 35, afficher qu'il fait de l'hypothermie. Sinon, afficher que tout est normal. Testez la fonction avec au minimum 3 valeurs.

3. Faire une fonction qui prend un entier et qui retourne si oui ou non, cet entier est divisible par 3. Testez avec au minimum 2 valeurs qui renvoient des réponses différentes.

4. a) Faire une fonction qui prend le résultat de 2 dés à jouer et qui donne des points selon la loi suivante:
- Si la somme des 2 dés est de 1, 2 ou 3, retourner 10 points. 
- Si la somme des 2 dés est de 4,5,...,9, retourner 5 points.
- Si la somme des 2 dés est de 10 ou plus, retourner 12 points.

b) À la page 69 du manuel, on explique comment faire un tirage au sort. Piger le résultat des 2 dés et ensuite, envoyez les 2 résultats dans la fonction de calcul de points. Faire l'expérience 3 fois en cumulant les points.


5. Faire la fonction qui prend les 3 paramètres d'une fonction quadratique et qui retourne le ou les 0. retourner "aucun" s'il n'y en a pas.


6. À l'aide de plusieurs mesures, on a modélisé la marée à un port maritime de France. Le modèle suivi par les données est le suivant: $h(t)=5.9sin(\pi t/6 -1.97) +6.9$

a) Faites une fonction qui prend l'heure (entière) et qui retourne la hauteur de la marrée (en mètres).

b) Faire une fonction qui prend l'heure (entière) et qui retourne un message pour avertir les usager du port si la marrée est en train de monter ou descendre. Vous DEVEZ utiliser la fonction faite à l'étape précédente.


# Solutions

Les solutions ne sont pas uniques. Chaque code doit être accompagné de tests, minimalement autant de tests que de cas possibles.

1. calculer_ph
```py
def calculer_ph(pH):
    if pH < 7:
        return "acide"
    elif pH == 7:
        return "neutre"
    elif pH > 7:    # On aurait pu mettre seulement else ici
        return "basique"

#Tests
print(calculer_ph(2))
print(calculer_ph(7))
print(calculer_ph(9.3))
```

2. température
```py
def thermometre(temperature):
    if temperature > 37.5:
        print("Fait de la fièvre")
    elif temperature < 35:
        print("Fait de l'hypothermie")
    else:
        print("Tout est normal")

#Tests
thermometre(38)
thermometre(33)
thermometre(36.5)
```

3. Divisible_par_3

```py
def divisible_par_3(n):
    if n % 3 == 0:
        return True
    else:
        return False

#Tests
print(divisible_par_3(9))
print(divisible_par_3(10))
```

4. dés à jouer 
a)
```py
def pointage_des(de1, de2):
    somme = de1 + de2
    if somme <= 3:
        return 10
    elif somme >= 4 and somme <= 9:
        return 5
    else:
        return 12

#Tests
print(pointage_des(1,1))
print(pointage_des(3,5))
print(pointage_des(6,6))
```

b)
```py
import random

total_point = 0

de1 = random.randint(1,6)
de2 = random.randint(1,6)
total_point = total_point + pointage_des(de1,de2)

de1 = random.randint(1,6)
de2 = random.randint(1,6)
total_point = total_point + pointage_des(de1,de2)

de1 = random.randint(1,6)
de2 = random.randint(1,6)
total_point = total_point + pointage_des(de1,de2)
```

5. quadratique

```py
import math

def zero_quadratique(a,b,c):
    if b**2 - 4*a*c > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        return x1,x2
    elif b**2 - 4*a*c == 0:
        x = -b /(2*a)
        return x
    else:
        return "Aucune valeur"

#tests
print(zero_quadratique(4,1,1))
print(zero_quadratique(1,4,1))
print(zero_quadratique(1,2,1))
```