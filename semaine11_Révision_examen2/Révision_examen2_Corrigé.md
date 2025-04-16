# Corrigé

```py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Question 1
#1a)
def N(t):
    return 10*np.exp(0.02*t)
#b)

print(round(N(0)), "bactéries à t=0")
print(round(N(1)), "bactéries à t=1")
print(round(N(2)), "bactéries à t=2")

#Supplément:
print(N(1000), "bactéries à t=1000")

#c)
valeurs_t = np.linspace(0,1000,1001)

#d)
valeurs_N = N(valeurs_t)
#e)
plt.figure(figsize=(10,6))
plt.plot(valeurs_t, valeurs_N, color = "orange")
plt.title("Nombre de bactéries en fonction du temps")
plt.xlabel("temps")
plt.ylabel("nombre de bactéries")
plt.xlim(800)
plt.grid(True)
plt.show()

#Question 2

#a)
data = pd.read_csv("films.csv", encoding="utf-8")
#b)
liste_titre = data['Titre'].tolist()
liste_annee = data['Annee'].tolist()
liste_note = data['Note'].tolist()
liste_revenu = data['Revenu'].tolist()
#c)
somme = sum(liste_revenu)
moyenne = np.mean(liste_revenu)
plus_grand = max(liste_revenu)
plus_petit = min(liste_revenu)
ecart = plus_grand - plus_petit
print(f"somme: {somme}$, moyenne:{moyenne}$ et écart: {ecart}$")

#d)
index = liste_titre.index("Gladiator")
revenu = liste_revenu[index]
print(f"Gladiateur a généré un revenu de {revenu}$")

#e)
film_choisi = input("Entrez un titre de film:")
if film_choisi in liste_titre:
    index = liste_titre.index(film_choisi)
    revenu = liste_revenu[index]
    print(f"{film_choisi} a généré un revenu de {revenu}$")
else:
    print("Ce film n'est pas dans la liste")

#f)
plt.figure(figsize = (9,7))
plt.scatter(liste_note, liste_revenu, c=liste_revenu, cmap="cool", marker='D')
plt.title("Revenu en fonction de la note obtenue")
plt.xlabel("Note Rotten Tomatoes")
plt.ylabel("Revenus en dizaine de millions de $")
plt.grid(True)
plt.show()


#g)
plt.figure(figsize = (11,6))
plt.plot(liste_titre, liste_note,color="magenta",marker="s",lw=0.6, linestyle='--', label = "Note des films selon Rotten Tomatoes")
plt.title("Note des films selon Rotten tomatoes")
plt.xlabel("titre du film")
plt.ylabel("revenus")
plt.xticks(rotation=30, ha='right')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.4) # pas à savoir, c'est pour que les noms ne dépassent pas
plt.grid(True)
plt.legend()
plt.show()

# h) Combien de films avaient le mot clé "The" dans le titre?

data_filtree = data.query('Titre.str.contains("The",na=False)')
liste_titres = data_filtree['Titre'].tolist()
print(len(liste_titres))

# i) Si on ne garde que les films faits avant l'an 2000, quelle serait la moyenne de revenu?

data_filtree2 = data.query('Annee < 2000')

liste_revenus = data_filtree2['Revenu'].tolist()
print(round(np.mean(liste_revenus),2))


#Question 3

prenoms = ["Jean", "Marie", "Pierre", "Claire", "Antoine", "Sophie", "Luc", "Anne", "François", "Catherine", "Louis", "Élise", "Philippe", "Valérie", "Guillaume", "Sophie", "Marc", "Sébastien", "Jean", "Louis"] 
abonnement =[False, False, False, True, True, True, False, True, False, True, False, True, True, True, True, True, True, False, True, False]
ages = [23, 61, 54, 36, 63, 44, 25, 70, 55, 46, 30, 35, 59, 41, 17, 33, 42, 28, 61, 19]
argent_epargne = [15.15, 18.95, 4.07, 85.77, 51.52, 10.15, 4.51, 52.68, 8.92, 16.27, 28.98, 40.64, 53.84, 89.51, 71.70, 67.59, 5.77, 19.54, 74.14, 15.51]

# a) Combien d'argent les clients ont-il épargné en tout, ensemble?
total = sum(argent_epargne)
print(f"Ils ont épargné {total}$")

# b) Combien de participants ont 55 ans ou plus?
ages_array = np.array(ages) # sans mettre en array, on ne peut pas faire de comparaison > < >= ou <=
liste_55_plus = ages_array[ages_array >= 55]
nombre_55_plus = len(liste_55_plus) # Après avoir mis les personnes de 55 ans et plus dans un liste, on calcule la longueur de cette liste

print(f"Il y a {nombre_55_plus} personnes de 55 ans et plus")

# c) Combien de participants ont une carte de fidélité?

abonnements_array = np.array(abonnement)
liste_fidelite = abonnements_array[abonnements_array == True]
nombre_fidelite = len(liste_fidelite)

print(f"Il y a {nombre_fidelite} personnes qui ont une carte de fidélité")

# d) Y a-t-il un client qui se nomme Pierre? Samuel?

if "Pierre" in prenoms:
    print("Il y a un Pierre dans la liste")
else:
    print("Il n'y a pas de Pierre dans la liste")

if "Samuel" in prenoms:
    print("Il y a un Samuel dans la liste")
else:
    print("Il n'y a pas de Samuel dans la liste")

# e) Ajouter 5$ à l'épargne d'Antoine 

index = prenoms.index("Antoine") # obtenir l'index de Antoine pour accéder à ses éléments correspondants
print("avant ajout:", argent_epargne[index])
argent_epargne[index] = argent_epargne[index] + 5
print("après ajout:", argent_epargne[index])

# f) Marie a décidé de s'abonner! Assurez-vous que ça paraisse dans la liste.

index = prenoms.index("Marie")


# g) Combien d'argent Marie a-t-elle épargné à date?

argent_Marie = argent_epargne[index]
print(f"Marie a épargné {argent_Marie}$")

# h) Est-ce que Marie a plus que 45 ans?

if ages[index] > 45:
    print("Oui, Marie a plus de 45 ans")
else:
    print("Non, elle a 45 ans ou moins")

# i) Quel est l'âge moyen des participants?

moyenne = np.mean(ages)
print(f"l'age moyen des participants est {moyenne} ans")

# j) Combien de personnes ont épargné plus que 10$?

# On remplace la liste ordinaire argent_epargne en l'écrasant par un array du même nom
argent_epargne = np.array(argent_epargne)  
liste_plus_10 = argent_epargne[argent_epargne>10]
nombre_plus_10 = len(liste_plus_10)
print(f"Il y a {nombre_plus_10} personnes qui ont épargné plus de 10$")


# k) Ajouter 10% à l'épargne de tout le monde (faire x 1.10 sur tous les montants)
# Pour que l'opération réussisse, il faut que argent_epargne ait été transformé en array (question précédente)
print("La liste avant:",argent_epargne)
argent_epargne = 1.10*argent_epargne
print("La liste après:",argent_epargne)

# l) Faire une phrase avec toutes les informations de la personne # 5 dans la liste (#5 d'humain).
if abonnement[4] == True:
    message = "est abonné au programme de fidélité"
else:
    message = "n'est pas abonné au programme de fidélité"
print(f"{prenoms[4]} a {ages[4]} ans, {message} et a épargné {round(argent_epargne[4],2)}$")

```