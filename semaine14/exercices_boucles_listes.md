## Question 1

Voici une liste des vitesses enregistrées à chaque 30 secondes par un mécanisme posé sur une voiture à des fins de récolte de données pour programme d'assurance. Voici les vitesses aux temps respectifs:

```py
temps_minutes = ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00']
vitesse = [0, 51.2, 79.2, 100.5, 105.3, 104.2, 110.3, 105.6, 102.6, 103, 105.6, 110.5, 111, 118.9, 110.2, 110.2, 108.9, 108, 70.6, 49.6, 0]
```
**Il est demandé d'utiliser des boucles pour toutes les questions sauf la a)**

a) Quelle était la vitesse à 5:30?

b) À combien de reprises la vitesse détectée a été au-dessus de 110 km/h?

c) Quel est le pourcentage des données récoltées qui sont au-dessus de 110 km/h?

d) Quelle a été la vitesse récoltée la plus élevée?

e) Quelle a été la moyenne de vitesse? 

f) Faire une liste des vitesses en m/s. La conversion pour passer de km/h à m/s est de diviser les km/h par 3.6. 

g) Quel a été le taux de variation moyen entre chaque duo de temps. Garder la liste en km/h et mettre les résultats dans la liste TVM.

## Question 2

Voici 3 listes qui représentent les températures minimales et maximales enregistrées à Shawinigan en janvier 2024. Répondre à toutes les questions avec une commande Python et faites un print pour voir la réponse, si désiré.

```py
janvier_min = [-10,-8,-4,-15,-17,-17,-12,-15,-16,-10,-11,-19,-13,-15,-16,-16,-20,-19,-25,-19,-20,-20,-17,-17,-9,-2,-2,-2,-9,-15,-11]
janvier_max = [-6,-1,0,0,-8,-10,-8,-3,-5,2,0,-7,-1,-1,-6,-8,-11,-7,-13,-9,-10,-2,-3,-7,1,0,0,2,-1,-9,-3]
```

a) Vérifier que les listes sont de la bonne longueur, c'est-à-dire 31.

b) Quelles étaient les températures min et max le 15 janvier 2024 à Shawinigan?

c) Combien y a-t-il eu de journées où il y a eu des températures au dessus de 0?

d) Calculer l'écart de température entre le max et le min pour chaque jour. Mettre les résultats dans une nouvelle liste nommée janvier_ecarts

e) Maintenant, faire une liste janvier_milieu qui se rempli avec le milieu entre la plus haute et la plus basse température pour tous les jours. Le milieu entre 2 valeurs est la somme des valeurs divisée par 2.

## Question 3 

Voici des équations chimiques dans des chaînes de caractères affectées dans des variables chimie1 à chimie5:
```py
chimie1 = "Équation chimique de la combustion du méthane: CH4 + 2O2 -> CO2 + 2H2O"
chimie2 = "Équation chimique de la synthèse de l'eau: 2H2 + O2 -> 2H2O"
chimie3 = "Équation chimique de la combustion du propane: Na + Cl2 -> 2NaCl"
chimie4 = "Équation chimique de la neutralisation: HCl + NaOH -> NaCl + H2O"
chimie5 = "Équation chimique de la précipitation: NaCl + AgNO3 -> AgCl + NaNO3"
```
Mettre les 5 variables dans une liste nommée liste_chimie.

a) À l'aide d'une boucle, vérifier si l'élément chimique de l'eau (H2O) est présent dans les équations. Compter le nombre d'équations qui en contiennent au moins 1.

b) Pour chimie1, trouver l'index du caractère ":". Créer ensuite une variable equation1 qui ne contient que l'équation chimique, sans le texte (donc ce qui est après le symbole : ). Une chaîne de caractère se traite comme un tableau pour parcourir chaque élément.

c) (facultative, plus difficile) Maintenant, faire ces étapes dans une boucle pour les 5. Mettre les équations dans une liste appelée liste_equations au fur et à mesure.

d) Parcourir tous les caractères de la chaîne chimie1. Compter 3 choses: 
- le nombre de caractères (sans les espaces).
- le nombre de voyelles = ["a","A","e","E","i","I","o","O","u","U","y","Y"]. (note: il existe des outils comme chaine.upper() qui pourrait aider à comparer des majuscules entre elles).
- le nombre de "H".