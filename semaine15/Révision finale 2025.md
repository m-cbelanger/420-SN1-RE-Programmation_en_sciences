# Révision très importante pour l'examen final.

Élément à savoir pour l'examen:
- Seul le logiciel Thonny sera autorisé
- Les écrans devront être à une intensité lumineuse suffisante pour que les surveillants voient. N'oubliez pas votre prise
- Il y aura des sièges réservés à plusieurs surveillants le jour de l'examen, soyez attentifs. 
- Aucun accès à internet, aucun accès à vos anciens fichiers, une seule feuille de notes, la plus récente est autorisée.


# Question 1

Voici 4 listes qui donnent les prénom, l’âge de client dans une épicerie. On leur a demandé s’ils avaient la carte de fidélité du magasin et combien d’argent ils épargnaient par mois à l’épicerie avec leur carte de fidélité et autres moyens combinés (coupons, rabais, etc.)
```py
prenoms = ["Jean", "Marie", "Pierre", "Claire", "Antoine", "Sophie", "Luc", "Anne", "François", "Catherine", "Louis", "Élise", "Philippe", "Valérie", "Guillaume", "Sophie", "Marc", "Sébastien", "Jean", "Louis"] 
abonnement =[False, False, False, True, True, True, False, True, False, True, False, True, True, True, True, True, True, False, True, False]
ages = [23, 61, 54, 36, 63, 44, 25, 70, 55, 46, 30, 35, 59, 41, 17, 33, 42, 28, 61, 19]
argent_epargne = [15.15, 18.95, 4.07, 85.77, 51.52, 10.15, 4.51, 52.68, 8.92, 16.27, 28.98, 40.64, 53.84, 89.51, 71.70, 67.59, 5.77, 19.54, 74.14, 15.51]	
```

a) Combien d’argent total a été épargné par les participants qui sont abonnés? Prendre une boucle pour trouver la réponse.

b) Les participants qui sont abonnés et qui ont 55 ans et plus ainsi que les participants qui ont moins de 20 ans sont admissibles à un rabais lors de leur prochain achat. Faire une liste qui récupère le nom des personnes qui sont admissibles au rabais. Prendre une boucle pour y arriver et mettre les noms dans une nouvelle liste.

c) En moyenne, combien d’argent les participants ont-ils épargné?

d) Combien de participants sont au-dessus de la moyenne d'épargne?

e) On fait un tirage au sort et les personnes dont le prénom est Louis ou Claire gagnent 100$! Ajouter les 100$ au montant épargné pour les personnes qui ont gagné.

f) Quel est le pourcentage de personnes dont la dernière lettre du prénom est un "e"?

g) Combien de personnes faut-il parcourir dans la liste de gauche à droite avant de rencontrer la 2e personne qui a moins de 25 ans?

h) Jeu de devinette! Faites un petit jeu qui demande à l'utilisateur d'entrer un âge. Si l'âge se trouve dans la liste des âges, l'utilisateur gagne. À chaque joute, on doit lui demander s'il veut rejouer. On doit aussi lui laisser un maximum de 5 chances!

# Question 2

a)	Importer le fichier livres.csv dans votre fichier Python.

b)	Calculer combien de pages seraient lues si on lisait tous les livres de la liste qui sont des romans et dont l’auteur est décédé. 

c)	Faire une liste avec tous les noms des auteurs qui ont écrit 15 livres ou plus et dont le livre de la liste est un roman. (ne pas tenir compte des filtres des sous-questions précédentes)

d)	Lequel des livres a le plus de pages? (ne pas tenir compte des filtres des sous-questions précédentes).

e)	Combien de pages y a-t-il en moyenne dans la liste? (ne pas tenir compte des filtres des sous-questions précédentes).

f)	Imprimer qui est l’auteur de « La plus grosse poutine du monde » et son nombre de pages.

g)	Présenter le nuage de points du nombre de livre en fonction de l’âge des auteurs. Ne garder que les livres dont l'âge des auteurs est en dessous de la moyenne. Faire une présentation esthétique en mettant :
-	une couleur graduée de votre choix, allant de bas en haut
-	une forme de « marker » différente que celle par défaut
-	des titres aux 2 axes
-	un titre général
-	une fenêtre (figure) plus grande que celle par défaut
-	un quadrillage

h) De tous les auteurs, combien d'entre eux ont la lettre J ou la lettre G comme première lettre du prénom?

# Question 3

Dans les boucles suivantes, dire ce que la boucle fait et trouver la ou les erreurs qui font qu'elle ne fonctionne pas. Les erreurs ne sont pas dans les textes des print ni des input:

a)
```py
import random
compteur_petits = 0
compteur_grands = 0
while x < 10:
    saisie = input("Voulez-vous rejouer? Entrer oui pour continuer")
    pige = random.random()
    if pige <= 0.5:
        compteur_petits = compteur_petits + 1
    else:
        compteur_grands= compteur_grands + 1
print("Après 10 essais, on a obtenu {compteur_grands} nombres au-dessus de 0.5 et {compteur_petits} nombres en bas ou égal à 0.5")
```
b)
```py
import random
while saisie != 'stop':
    annee_aleatoire = random.randint(1920, 2025)
    annee_utilisateur = int(input("Entrez votre année de naissance (ou tapez 'stop' pour quitter) : "))
    
    ecart = abs(annee_utilisateur - annee_aleatoire)
    print(f"Année pigée : {annee_aleatoire}")
    print(f"Votre année : {annee_utilisateur}")
    print(f"Écart d’âge : {ecart} ans")

    if annee_utilisateur < annee_aleatoire:
        print("Vous êtes le plus vieux!")
    elif annee_utilisateur > annee_aleatoire:
        print("Vous êtes le plus jeune!")
    else:
        print("Vous avez le même âge!")
```
c) Le but est d'afficher les nombres de 1 à 5 au carré:
```py
for i in range(1, 5):
    print("Le carré de", i, "est", i * i)
```

d) 
```py
for i in range(1, 10):
    if i % 2 == 0:
        compteur += 1

print("Il y a", compteur, "nombres pairs entre 1 et 10.")
```