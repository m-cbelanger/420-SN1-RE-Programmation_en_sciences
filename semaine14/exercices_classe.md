# Exemples de boucles for dans un tableau

**Numéro 1**: 

a) Faire une variable appelée `cumul` qui contient initialement 5.

b) Mettre la liste [1,6,5,1,2,3,8] dans une variable nommée liste1.

c) Faire une boucle qui parcoure la liste1 et qui regarde si l'élément de la liste est pair ou impair. S'il est pair, on l'additionne à `cumul`, s'il est impair, on le soustrait à `cumul`.

d) À la toute fin, on imprime `cumul`.

**Numéro 2**: 
a) Mettre la liste [1,6,5,1,2,3,8,9,0,1,4,4,7,12,10,11] dans une variable nommée liste2.

b) Faire une boucle qui parcoure la liste2 et qui, dans le corps de la boucle, vérifie si l'élément de la liste est un nombre pair ou non et qui imprime la réponse à mesure.

c) Calculer combien de nombres il faut croiser avant de rencontrer le 2e multiple de 3.

d) Remplacer tous les multiples de 4 par 0. 

**Numéro 3**
```py
materiaux = ['Aluminium', 'Fer', 'Cuivre', 'Plomb', 'Or', 'Argent', 'Titane', 'Zinc', 'Nickel', 'Étain']
fusion_celsius = [660.3, 1538, 1084.6, 327.5, 1064.2, 961.8, 1668, 419.5, 1455, 231.9]
```
a) Quelle est la température de fusion du cuivre?

b) Quel est le pourcentage des matériaux ayant une température de fusion inférieure à 500 °C?

c) Combien de matériaux ont une température de fusion inférieure à la moyenne?

d) Combien de matériau faut-il parcourir pour rencontrer le premier qui a une température de fusion supérieure à la moyenne?

e) Créez une liste fusion_kelvin contenant les températures converties en kelvins.
Formule : K = °C + 273.15

f) Créez une liste commentaires contenant des chaînes du type :
"Le <matériau> fond à <température> °C", pour chaque matériau.



**Numéro 4**: 

Les chaînes de caractères peuvent aussi être parcourues comme des listes dans une boucle. Voici une liste:
elements_chimiques = ["Hg", "Pb", "As", "Cd", "H2S"]
Voici des équations chimiques. Faire détecter algorithmiquement si les équations contiennent des éléments chimiques de la liste elements_chimiques.
```py
chaine1 = "HgO + 2HCl -> HgCl2 + H2O"
```



**Numéro défi**: 

Faisons une boucle qui dessine un triangle d'étoiles comme ceci:

![triangle.PNG](img/triangle.PNG)