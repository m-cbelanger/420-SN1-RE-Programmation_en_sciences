# Blocs conditionnels imbriqués

Il est possible de faire un bloc conditionnel dans un autre bloc conditionnel. Voici un exemple:

```py
age = int(input("Quel âge avez-vous?"))

if age >= 16:
    print("Vous pouvez avoir un permis de conduire. ")
    if age >= 18:
        print("Vous êtes majeur. ")
        if age >= 22:
            print("Vous n'avez plus à respecter la condition de tolérance zéro pour conduire.")
else:
    print("Vous êtes trop jeune pour avoir un permis de conduire pour voiture.")
```


## Exemple:
Voici un exemple qui vérifie si l'air est respirable en haute altitude selon la pression et la température.

Dans cet exemple, on fait une fonction qui prend les valeurs d'altitude et de température et qui retourne le degré de dangerosité de s'aventurer dans la région, de 1 à 3. Ensuite, on utilise le retour de cette fonction pour déterminer le coût minimal de l'équipement des scientifiques qui doivent se rendre sur place.


```py
def verifier_air_respirable(altitude, temperature):
    # Calcul de la pression atmosphérique en fonction de l'altitude (approximation barométrique)
    pression = 101.3 * (1 - 0.0000226 * altitude) ** 5.256  # Pression en kPa

    # Vérification des conditions atmosphériques
    if pression < 80:  # Seuil de pression basse pour la respiration
        print("L'air est trop raréfié ! Vérification de la température...")
        
        # If imbriqué pour vérifier la température
        if temperature < 0:
            print("Il fait trop froid et la pression est trop basse. Prévoyez une bouteille d'oxygène et des vêtements thermiques.")
            return 3
        else:
            print("La pression est basse, mais la température est acceptable. L'oxygène est nécessaire.")
            return 2
    else:
        print("Les conditions atmosphériques sont normales. L'air est respirable.")
        return 1
                     
def cout_minimal(degre_risque):
    prix_bouteille = 185.50
    prix_manteau_thermique = 261.33
    prix_pantalon_thermique = 189.22
    if degre_risque == 3:
        cout = 2*prix_bouteille + prix_manteau_thermique + prix_pantalon_thermique
    elif degre_risque == 2 :
        cout = 1*prix_bouteille + prix_manteau_thermique
    else:
        cout = 0
    return cout
        

# Condition d'expédition
altitude = float(input("Entrez l'altitude en mètres: ")) 
temperature = float(input("Quelle est la température? "))

risque = verifier_air_respirable(altitude, temperature)
prix = cout_minimal(risque)

print(f"Avec une température de {temperature} degrés à une altitude de {altitude} mètres, on aura un coût minimal à défrayer de {prix} $")

```


# Exercices


### Question 1
Dans le code ci-dessous, la fonction donne une cote (A,B, C...) à un étudiant selon la note obtenue.

```py
def cote_selon_note(note):
    if note >= 90:
        cote = "A"
    elif note >= 80:
        cote = "B"
    elif note >= 70:
        cote = "C"
    elif note >= 60:
        cote = "D"
    else:
        cote = "E"
    return cote

#tests
print(cote_selon_note(78))
print(cote_selon_note(56))
print(cote_selon_note(99))
```        

a) Pourquoi le test, quand on appelle cote_selon_note(78) donne bel et bien "C", malgré que 78 soit plus grand que 60 et que 70? Pourquoi on n'a pas une ambiguïté entre la cote "C" et "D"?

b) Modifier ce code pour que les notes en haut de 100 et les notes en bas de 0 reçoivent une cote "tiret" ("-").

c) Pourquoi le code suivant, semblable au premier, ne donne pas les résultats escomptés? On prend pour acquis que chaque note entrée sera entre 0 et 100.
```py
def cote_selon_note2(note):
    if note < 60:
        cote = "E"
    elif note >= 60:
        cote = "D"
    elif note >= 70:
        cote = "C"
    elif note >= 80:
        cote = "B"
    else:
        cote = "A"
    return cote

#tests
print(cote_selon_note2(78))
print(cote_selon_note2(56))
print(cote_selon_note2(99))
```



### Question 2

Une année bissextile est une année multiple de 4, mais pas de 100, à l'exception des années multiples de 400. Ainsi, 2000, 2020, 2024, 2400 sont bissextiles, mais pas 1900, 2100, 2200 ni 2300. Faire la fonction qui prend une année et qui retourne si oui ou non (True ou False), on est dans une année bissextile.

### Question 3

Faire une fonction qui prend les lettres du groupe sanguin de 2 personnes, un donneur et un receveur. La fonction retourne une chaine de caractère qui dit si le don de sang est possible sans risque. Pour garder ça simple, on ignore le Rhésus (+, -). Il faut aussi que la fonction rejette les lettres non-valides. Les lettre valides pour les groupes sanguins sont "A", "B", "AB" ou "O". Le groupe "O" peut donner à tous les autres, le groupe "A" peut donner aux "A" et "AB", le groupe "B" peut donne aux groupes "B" et "AB" et le groupe "AB" ne peut donner qu'à lui-même.

<br>
<br>
<br>



# Solutions

Il existe plusieurs bonnes réponses. N'hésitez pas à valider auprès du prof!

### Question 1

a) Dans la structure if et ses déclinaisons attachées, on commence toujours à vérifier si le if est vrai. S'il est vrai, on exécute les lignes de code immédiatement en dessous de celui-ci puis on sort de la structure if-elif-else (on ne fait aucune autre ligne). Si la condition du if est fausse, on passe au premier elif. On répète l'opération. La déclinaison des if-elif-else est comme un filet qui ne permet pas de descendre plus bas si on remplit une condition plus haute.

b) 
```py
def cote_selon_note(note):
    if note < 0 or note >100:
        cote = "-"
    else:
        if note >= 90:
            cote = "A"
        elif note >= 80 :
            cote = "B"
        elif note >= 70 :
            cote = "C"
        elif note >= 60:
            cote = "D"
        else:
            cote = "E"
    return cote

#test
print(cote_selon_note(110))
print(cote_selon_note(58))
print(cote_selon_note(-2))
```

c) Parce que si on entre une note de 98, celle-ci est plus grande que 60, qui est une condition placée AVANT celle qui vérifie que la note soit plus grande que 90. La condition du premier elif est donc vraie et on ne fait aucune autre branche de la structure.

### Question 2

```py
#Question 2

def est_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0)  or  annee % 400 == 0:
        return True
    else:
        return False
    
print(est_bissextile(2000))
print(est_bissextile(2100))
print(est_bissextile(2025))
print(est_bissextile(2024))
```

### Question 3

```py
#Question 3
def don_de_sang(donneur,receveur):
    possibilite_don = ""
    if donneur != "A" and donneur != "B" and donneur != "AB" and donneur != "O":
        possibilite_don = "Erreur sur l'entrée du groupe donneur"
    elif receveur != "A" and receveur != "B" and receveur != "AB" and receveur != "O":
        possibilite_don = "Erreur sur l'entrée du groupe receveur"
    else:
        
        if donneur == "O":
            possibilite_don = "Don possible"
        elif donneur == "A" and (receveur == "A" or receveur == "AB"):
            possibilite_don = "Don possible"
        elif donneur == "B" and (receveur == "B" or receveur == "AB"):
            possibilite_don = "Don possible"
        elif donneur == "AB" and receveur == "AB":
            possibilite_don = "Don possible"
        else:
            possibilite_don = "Danger, don impossible"
    
    return possibilite_don

print(don_de_sang("W","A"))   # Cas non-valide 1
print(don_de_sang("A","W"))   # Cas non-valide 2
print(don_de_sang("O", "O"))   # Cas 1 : o
print(don_de_sang("O", "A"))   # Cas 2
print(don_de_sang("O", "B"))   # Cas 3
print(don_de_sang("O", "AB"))  # Cas 4

print(don_de_sang("A", "O"))   # Cas 5
print(don_de_sang("A", "A"))   # Cas 6
print(don_de_sang("A", "B"))   # Cas 7
print(don_de_sang("A", "AB"))  # Cas 8

print(don_de_sang("B", "O"))   # Cas 9
print(don_de_sang("B", "A"))   # Cas 10
print(don_de_sang("B", "B"))   # Cas 11
print(don_de_sang("B", "AB"))  # Cas 12

print(don_de_sang("AB", "O"))  # Cas 13
print(don_de_sang("AB", "A"))  # Cas 14
print(don_de_sang("AB", "B"))  # Cas 15
print(don_de_sang("AB", "AB")) # Cas 16
```

                 










