# Exercices sur les listes

Dans le livre: page 110 # 1-2-5
Théorie page 134 (chapitre 4.4)


Voici quelques exercices simples de manipulation de listes. À tout moment, n'hésitez pas à imprimer la liste en console (print()). Soyez attentifs aux termes utilisés dans les questions.

Le mot "index" signifie la position de l'élément, en commençant à 0. En tout temps, on crée la liste à la main dans le programme, mais ON NE LA RECHANGE PAS DIRECTEMENT DANS LA FENÊTRE. Ce sont les commandes Python qui vont les modifier.


### Question 1
a) reproduire les 2 listes suivantes dans Thonny:

```py
heure = ['8:00','8:07' , '8:12', '8:18', '8:25', '8:32', '8:45']
glycemie = [0.80, 1.00, 1.05, 1.10, 1.12, 1.12, 1.10]
```

b) Afficher les listes créées en a) dans la console

c) À quel est l'index de la glycémie prise à 8:25? Mettre la valeur dans une variable.

d) À partir de l'index de la question précédente, afficher la glycémie correspondante dans l'autre liste.

e) Ajouter une glycémie de 1.09 à 8:56 dans les listes respectives.

f) Une valeur avait été oubliée à 7:45. Ajouter la glycémie de 0.75 à 7:45 dans les listes respectives et assurez-vous que le résultat est en ordre.

g) À l'aide d'une commande python, dites si oui ou non, une des glycémie a été prise à 8:25. Et à 9:00?

h) Enlever la valeur à la position 4 dans les 2 listes 

i) Calculer la valeur maximale de glycémie et la mettre dans une variable. Faire la même chose pour le min.

j) Quelle est la différence entre le max et le min?

k) Utiliser la méthode `len` pour afficher le nombre d'éléments dans la liste de glycémie et mettre le résultat dans une variable.

l) Dans un print, afficher la 3 valeur de glycémie et l'heure à laquelle on l'a prise, dans une phrase.

m) Que se passe-t-il si on fait glycémie*10?

n) Une erreur s'est glissée dans la prise de la glycémie! Changer la mesure de 8:07 pour 1.04.



# Listes avec Numpy

Théorie dans le livre, page 134 (chapitre 4.4)
Dans le livre: page 151 # 1-3-5

### Question 2

a) Définir un array (liste spéciale de numpy) nommé temperature_celsius et qui contient les valeurs suivantes: -5.2,  -3.8,  2.3,  8.7,  15.4,  20.1,  23.3,  22.8,  17.5,  10.2,  3.6, -2.1. Ces valeurs sont les température moyenne fictives pour les 12 mois de l'année dans une région du Canada
b) Avec une commande associée aux arrays, vérifiez si oui ou non la taille de l'array est de 12 (pour 12 mois)

c) Quelle est la moyenne de températures pour cette année-là?

d) Quelle est la température la plus basse?

e) Afficher les températures de juin à septembre. Faites la moyenne de ces mois seulement et placer le résultat dans une variable.

f) Faire un nouveau array nommé temperature_fahrenheit qui prend l'ancien array et qui le convertit en fahrenheit. Il faut faire la température en Celsius * 9/5 +32 




### Question 3
a) Faire un array nommé mon_array avec les valeurs de -pi, -pi/2, 0, pi/2, pi

b) Faire une liste nommée ma_liste avec les valeurs de -pi, -pi/2, 0, pi/2, pi

c) Afficher le résultat de 2*mon_array et le résultat de 2*ma_liste. Que constatez-vous?

d) Faite le sinus de chaque valeur. Est-ce qu'on prend la liste ou l'array?

e) Avec des commandes Python, ajouter les valeurs manquantes de 3*pi/2 et 2*pi à l'array.

f) Avec les commandes Python, ajouter les valeurs manquantes de -3*pi/2 et de -2*pi à l'array.




### Question 4

a) Faire un array qui contient les valeurs entières de -20 à 20 en utilisant np.linspace. On l'appelle x.

b) Faire un autre array, appelé y_1, qui contient l'image (la valeur de y quand on met x dans l'expression) de $y = e^x -2$

c) Faire une fonction nommée f, qui prend x en paramètre et qui retourne $x^2-9x+6$. Prendre le retour et le mettre dans un autre array, nommé y_2.

d) Pour chaque valeur de la liste y_1, imprimer si oui ou non, la valeur est supérieure ou égale à 5000.

d) faire une liste y_2_modifiee qui ne garde que les valeurs de y_2 qui sont inférieures à 100.




