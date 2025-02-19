# Appels de fonctions successifs

L'appel de fonction peut être multiple. On peut appeler une fonction à l'intérieur d'une autre et en utiliser le retour.

Mise en contexte: Les jeux Olympiques

Les jeux Olympiques, en temps normal, sont alternés entre les jeux d'été et les jeux d'hiver à chaque 2 ans. Si on est dans une année multiple de 4, il y aura des jeux d'été et sinon, ce sera des jeux d'hiver. On peut faire une fonction imbriquée pour fournir une année à la fonction jeux_olympiques(annee) et celle-ci me retournera "été" ou "hiver".  


Voici un exemple:

```py
def annee_multiple_4(annee):
    if annee % 4 == 0 :
        return True
    return False

def jeux_olympiques(annee):
    multiple = annee_multiple_4(annee)
    if multiple == True:
        return "été"
    elif annee % 2 == 0:
        return "hiver"

```

Voici un autre exemple avec un seul appel qui fait plusieurs sous-appels. Faisons la `TRACE` de cet algorithme. Le code de chaque fonction est simplifié pour l'exemple, les print() ne sont là que pour décrire où on est rendus.

```py
def analyser_echantillon():
    print("Début de l'analyse de l'échantillon")
    prelever_echantillon()
    effectuer_tests()
    interpreter_resultats()
    print("Fin de l'analyse de l'échantillon")

def prelever_echantillon():
    print("Début du prélèvement de l'échantillon")
    steriliser_materiel()
    print("Fin du prélèvement de l'échantillon")

def steriliser_materiel():
    print("Début de la stérilisation du matériel")
    print("Fin de la stérilisation du matériel")

def effectuer_tests():
    print("Début des tests en laboratoire")
    tester_pH()
    tester_conductivite()
    print("Fin des tests en laboratoire")

def tester_pH():
    print("Début du test de pH")
    print("Fin du test de pH")

def tester_conductivite():
    print("Début du test de conductivité")
    print("Fin du test de conductivité")

def interpreter_resultats():
    print("Début de l'interprétation des résultats")
    print("Fin de l'interprétation des résultats")

# Lancement de l'analyse
analyser_echantillon()
```

# Exercices



### Question 1

On souhaite faire un tirage au sort d'une date de fête.

a) faire une fonction qui ne prend rien, mais qui retourne un mois de fête selon les proportions suivantes. Les pourcentages sont dans l'ordre de janvier à décembre. Cela veut dire que, au Canada par exemple, 7.5% des personnes sont nées en janvier, 7% en février, 8% en mars, etc. (estimation de 2020)

```py
pourcentages_naissances = [7.5, 7.0, 8.5, 8.0, 8.3, 8.5, 8.7, 9.2, 9.0, 8.8, 8.0, 7.5]
``` 

b) faire une fonction qui prend un mois et qui retourne un jour pigé (entier) au hasard dans ce mois.

c) faire une fonction qui pige une date de fête complète et la retourne en chaine de caractères. Elle doit ABSOLUMENT utiliser les 2 autres fonctions pour y parvenir.

d) Dans l'environnement principal, appeler la fonction créée en 2 et écrire le résultat dans une phrase complète.


### Question 2

Pour calculer l'énergie mécanique en physique, il faut calculer l'énergie cinétique plus l'énergie potentielle gravitationnelle.

Énergie mécanique: $E_m = E_c + E_p$

Énergie cinétique: $E_c = 0.5 mv^2$

Énergie potentielle: $E_p = mgh$

avec $m$ qui est la masse en kg, $v$ qui est la vitesse en $m/s$, $h$ qui est la hauteur en mètres et g qui est l'accélération gravitationnelle de 9.81.

a) Faire 2 fonctions: une pour calculer et retourner l'énergie cinétique en prenant la masse et la vitesse et une pour calculer l'énergie potentielle en prenant la masse et la hauteur (g est constante) 

b) Faire une 3e fonction pour calculer l'énergie mécanique qui doit ABSOLUMENT appeler les 2 autres fonctions pour faire ses calculs. Elle doit prendre tous les paramètres nécessaires pour que les calculs s'effectuent. Quels seraient ces paramètres?

c) À l'extérieur des fonctions, dans l'environnement principal, créer 3 questions qui demandent la masse, la vitesse et la hauteur d'un objet pour ensuite utiliser les réponses et montrer le résultat de l'énergie mécanique (dans l'environnement principal). L'affichage final de la réponse doit avoir 2 décimales et on doit voir une phrase complète pour l'afficher.


<br>
<br>
<br>



# Solutions

## Question 1
```py
import random

#a)
def mois_de_fete():
    pourcentages_naissances = [7.5, 7.0, 8.5, 8.0, 8.3, 8.5, 8.7, 9.2, 9.0, 8.8, 8.0, 7.5]
    mois = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    
    mois_pige = random.choices(mois,weights=pourcentages_naissances,k=1)[0]
    return mois_pige

#test
print(mois_de_fete())

#b)
def jour_de_fete(mois):
    if mois == "janvier" or mois == "mars" or mois == "mai" or mois == "juillet" or mois == "août" or mois == "octobre" or mois == "décembre":
        jour_pige = random.randint(1,31)
    elif mois == "avril" or mois == "juin" or mois == "septembre" or mois == "novembre":
        jour_pige = random.randint(1,30)
    elif mois == "février":
        jour_pige = random.randint(1,29)
    return jour_pige

# test
print(jour_de_fete("janvier"))
print(jour_de_fete("février"))
print(jour_de_fete("avril"))

#c)
mon_mois = mois_de_fete()
mon_jour = jour_de_fete(mon_mois)
print(f"La date de fête pigée est le {mon_jour} {mon_mois}.")
```

## Question 2
```py
#a)
def energie_cinetique(masse, vitesse):
    return 0.5*masse*vitesse**2

#test
print(energie_cinetique(5, 100))

def energie_potentielle(masse, hauteur):
    g = 9.81
    return masse*g*hauteur

print(energie_potentielle(5, 10))

#b)
def energie_mecanique(masse, vitesse, hauteur):
    Ec = energie_cinetique(masse, vitesse)
    Ep = energie_potentielle(masse,hauteur)
    
    return Ec + Ep

#Test:  énergie mécanique approximative d'un véhicule de 1200kg qui est en haut d'une côte de 40 m et qui descend a 90  km/h
vitesse_m_s = 90 / 3.6
print(f"L'énergie mécanique d'un véhicule de 1200 kg qui descend une côte de 40 m à 90 km/h est {energie_mecanique(1200, vitesse_m_s, 40)} Joules")

#c)
h = float(input("Quelle est la hauteur de l'objet en m? "))
v = float(input("Quelle est la vitesse en m/s? "))
m = float(input("Quelle est la masse en kg? "))

print(f"L'énergie mécanique d'un objet de {m} kg qui est à une hauteur de {h} m à {v} m/s est {energie_mecanique(m, v, h)} Joules")
```