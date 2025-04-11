# Exercices de révision examen 2

Important pour l'examen 2:
- il faut toujours que les réponses soient présentées à l’aide de lignes de code (ne pas écrire ce que vous déduisez en regardant la liste avec vos yeux, par exemple)
- l'examen sera composé à environ 90%-95% de code, 5%-10% de questions théoriques.

## Section théorique

Je ne mettrai pas de questions directement, mais voici des exemples de sujets qui devraient être compris:

- La différence et les diverses actions qu'on fait avec une liste ordinaire versus un array
- La position d'un élément dans une liste, numérotée par un index qui commence à 0. 
- L'utilisation des listes pour faire des graphiques (obligé d'être numérique ou non?)

## Section de code

### Question 1
Supposons qu’une population de bactéries suit une croissance exponentielle dans le temps donnée par l’équation :

$N(t)=10⋅e^{0.02t}$

a) Écrire la fonction N qui prend le temps t en paramètres et qui retourne le nombre de bactéries.

b) Afficher le nombre de bactéries pour un temps de 0, un temps de 1 et un temps de 2. 

c) Faire une liste de valeurs_t allant de 0 à 1000.

d) Générer une liste valeurs_N qui sont l’image des valeurs_t.

e) Afficher le tracé de cette courbe. Faire une présentation esthétique en mettant :

- une couleur différente de la couleur par défaut
- un style différent du style par défaut
- des titres aux 2 axes
- un titre général
- une fenêtre (figure) plus grande que celle par défaut
- un quadrillage
- Tout autre ajustement visuel pertinent (aucun mot ne se chevauche, les graduations sont esthétiques et logiques)
- Faire commencer les graduations de l’axe des valeurs_t à 800.


# Question 2

Vous avez le fichier films.csv qui contient le titre de films populaires, leur année de parution, la longueur du film en minute, la note fictive sur le site "rotten tomatoes" et le revenu en dollars de la première semaine de parution du film au box office. 

a)	Importer le fichier films.csv dans Python avec la fonction de la librairie Pandas. Préalablement, télécharger le fichier csv et le placer dans le même dossier que le fichier Python (cette étape préalable ne sera pas précisée à l'examen. Si vous devez recourir à de l'aide, les points attribués à cette section seront perdus.)

b)	Faire des listes avec les colonnes Titre, Année, Note et Revenu.

c)	Calculer la somme des revenus, la moyenne des revenus et l’écart entre le revenu le plus grand et le revenu le plus petit.

d)	Quel est le revenu du film Gladiator? Afficher la réponse. (ne pas oublier d'utiliser le code)

e)	Demander un titre de film à un utilisateur. Si le film est dans la liste, afficher son revenu (une version bonifiée de la question d).

f)	Présenter le nuage de point du revenu en fonction de la note obtenue. Faire une présentation esthétique en mettant :

-	une couleur différente de la couleur par défaut (je peux aussi demander une gradation de couleur, soyez prêts aux 2 éventualités)
-	une forme de « marker » différente que celle par défaut
-	des titres aux 2 axes
-	un titre général
-	une fenêtre (figure) plus grande que celle par défaut
-	un quadrillage
-	Tout autre ajustement visuel pertinent (aucun mot ne se chevauche, les graduations sont esthétiques et logiques)

g)	Faire un graphique (tracé avec lien entre les points) de la variable Revenu en fonction de la variable Titre. Faire une présentation esthétique en mettant :
-	une couleur différente de la couleur par défaut
-	des titres aux 2 axes
-	un titre général
-	une fenêtre (figure) plus grande que celle par défaut
-	un quadrillage
-	une légende avec le libellé « revenu des divers films en 100 000 000$».
-	Tout autre ajustement visuel pertinent (aucun mot ne se chevauche, les graduations sont esthétiques et logiques)


### Question 3

Voici des listes qui donnent les prénom, l’âge de client dans une épicerie. On leur a demandé s’ils avaient la carte de fidélité du magasin et combien d’argent ils épargnaient par mois à l’épicerie avec leur carte de fidélité et autres moyens combinés (coupons, rabais, etc.).

Vous pouvez copier-coller ces listes dans un fichier Python.

```py
prenoms = ["Jean", "Marie", "Pierre", "Claire", "Antoine", "Sophie", "Luc", "Anne", "François", "Catherine", "Louis", "Élise", "Philippe", "Valérie", "Guillaume", "Sophie", "Marc", "Sébastien", "Jean", "Louis"] 

abonnement =[False, False, False, True, True, True, False, True, False, True, False, True, True, True, True, True, True, False, True, False]

ages = [23, 61, 54, 36, 63, 44, 25, 70, 55, 46, 30, 35, 59, 41, 17, 33, 42, 28, 61, 19]

argent_epargne = [15.15, 18.95, 4.07, 85.77, 51.52, 10.15, 4.51, 52.68, 8.92, 16.27, 28.98, 40.64, 53.84, 89.51, 71.70, 67.59, 5.77, 19.54, 74.14, 15.51]
```

Pour toutes les questions ci-dessous, faites comme si vous NE VOYEZ PAS les données ci-haut, comme si elle provenaient d'un fichier externe

a) Combien d'argent les clients ont-il épargné en tout, ensemble?

b) Combien de participants ont 55 ans ou plus?

c) Combien de participants ont une carte de fidélité?

d) Y a-t-il un client qui se nomme Pierre? Samuel?

e) Ajouter 5$ à l'épargne d'Antoine 

f) Marie a décidé de s'abonner! Assurez-vous que ça paraisse dans la liste.

g) Combien d'argent Marie a-t-elle épargné à date?

h) Est-ce que Marie a plus que 45 ans?

i) Quel est l'âge moyen des participants?

j) Combien de personnes ont épargné plus que 10$?

k) Ajouter 10% à l'épargne de tout le monde (faire x 1.10 sur tous les montants)

l) Faire une phrase avec toutes les informations de la personne # 5 dans la liste (#5 d'humain).

