# Syntaxe

Voici quelques bouts de code dans lesquels il y a des erreurs de SYNTAXE (pas de logique). Trouvez ces erreurs et corrigez-les

a)
```py
def ma_description(nom, prénom)
    nom_complet = prenom + nom
    return nom_complet

print(ma_description("Bélanger", "Marie"))
```

b)
```py
def compare(a,b):
    if a = b:
        print("les nombres sont identiques")
    else:
        print("les nombres sont différents")

compare(3,4)
```

c)
```py
def hypotenuse(a,b):
    hyp**2 = a**2 + b**2
    return hyp

print(hypotenuse(3,4))
```

```py
def mon_calcul(nombre1, nombre2):
    calcul = nombre1**5 - 5e4 * 3/8 + 15nombre2
    return calcul

x1 = 12
x2 = 5
mon_calcul(x1,x2)
```

## Variables locales et portée

Comme on a vu au chapitre 2, les variables ont une **portée**. Par exemple, si on fait une fonction dont le paramètre se nomme x, ce n'est pas le même x que dans une autre fonction et ce n'est pas le même x que dans le code principal (celui collé sur le mur). On dira donc que la variable parite est LOCALE à fonction1. Elle n'existe pas à l'extérieur. On pourrait faire plusieurs fonctions avec des variables nommées x sans qu'elles n'interfèrent les unes avec les autres.

```py
def fonction1(x):
    if x % 2 == 0:
        parite = True
    else:
        parite = False
    return parite


# Ce x n'est pas le même que celui dans fonction1
x = 67


# parite n'est pas accessible a l'extérieur de la fonction1. Donc ceci provoque une erreur:
# Cette ligne provoque une erreur (commentez-là pour passer par-dessus)
print(parite)

# Pour avoir la valeur de parité, il faut appeler la fonction1 avec une valeur.
# Puisque la valeur de x dans l'environnement global (hors fonction) est de 67, on peut appeler fonction1(x)
print(fonction1(x))

a = 108

# La valeur de la variable à passer à la fonction doit simplement exister dans l'environnement où l'appel de la fonction se trouve.
# ici, on a le choix entre a et x pour appeler la fonction1.
print(fonction1(a))
```

## Variables globales

Si on veut avoir accès à une variable qui est utilisée partout, on peut la déclarer au début, en majuscule, et l'utiliser partout. On peut aussi la modifier dans une fonction, DANS CERTAINES SITUATIONS précises.

### Variable globale constante

Présentement (février 2025), la taxes sur les produits et services au Québec est de 9,975% au provincial et de 5% au fédéral. Mettre ces valeurs dans des variables globales constantes et les utiliser dans une fonction qui calcule et retourne la valeur finale de vente d'un article. Dans cette fonction, ajouter aussi la possibilité de mettre un rabais (optionnel). (Réfléchir à un nom significatif pour la fonction, aux paramètres à passer lors de l'appel)


# Exercice

## Question 1

copier le code ci-dessous dans Thonny sans le modifier au départ. Ensuite, corriger chaque erreur une à la fois en déchiffrant le message d'erreur à chaque fois. Écrire chaque nom d'erreur obtenue et essayer de vous en inspirer pour réparer chaque erreur une à la fois.

```py
def carres(x):
    if x % math.sqrt(x) = 0:
        return True
     else
        return false

print carre(x)
```