# Corrigé exercices de liste

## Question 1
```py
heure = ['8:00','8:07' , '8:12', '8:18', '8:25', '8:32', '8:45']
glycemie = [0.80, 1.00, 1.05, 1.10, 1.12, 1.12, 1.10]

#b)
print(heure)
print(glycemie)

#c)
glycemie_825 = heure.index("8:25")
print(glycemie_825)

#d)
print(glycemie[glycemie_825])

#e)
glycemie.append(1.09)
heure.append("8:56")
print(heure)
print(glycemie)

#f)
glycemie.insert(0,0.75)
heure.insert(0,"7:45")
print(heure)
print(glycemie)

#g)
print("8:25" in heure)
print("9:00" in heure)

#h)
heure.pop(3)
glycemie.pop(3)
print(heure)
print(glycemie)

#i)
maximum = max(glycemie)
minimum = min(glycemie)
print("Le maximum de glycémie est", maximum, "et le minimum est", minimum)

#j)
difference = maximum - minimum
print("il y a", round(difference,2), "de différence entre le max et le min")

#k)
print(len(glycemie))

#l)
print("La 3e valeur est", glycemie[2], "prise à", heure[2])

#m)
print(glycemie *10)

#n)
i = heure.index("8:07")
glycemie[i] = 1.04
print(glycemie)
```

## Question 2

```py
#a)
temperature_celsius = np.array([-5.2,  -3.8,  2.3,  8.7,  15.4,  20.1,  23.3,  22.8,  17.5,  10.2,  3.6, -2.1])

#b)
print(len(temperature_celsius) == 12)

#c)
moyenne = temperature_celsius.mean()
print("La moyenne de l'année est",moyenne, "degrés Celsius")

#d)
minimum = min(temperature_celsius)
print("La température la plus basse par mois est",minimum, "degrés Celsius")

#e)
temperature_ete = temperature_celsius[5:9]
print(temperature_ete)
moyenne = temperature_ete.mean()
print("La moyenne de l'été est",round(moyenne,1), "degrés Celsius")

#f)
temperature_fahrenheit = temperature_celsius*9/5+32
print(temperature_fahrenheit)

```

## Question 3

```py
#a) Faire un array nommé mon_array avec les valeurs de -pi, -pi/2, 0, pi/2, pi
mon_array = np.array([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

#b) Faire une liste nommée ma_liste avec les valeurs de -pi, -pi/2, 0, pi/2, pi
ma_liste = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]

#c) Afficher le résultat de 2mon_array et le résultat de 2ma_liste. Que constatez-vous?
print(2*mon_array)
print(2*ma_liste)

#d) Faite le sinus de chaque valeur. Est-ce qu'on prend la liste ou l'array?
print(np.sin(mon_array))

#e) Avec des commandes Python, ajouter les valeurs manquantes de 3pi/2 et 2pi à l'array.
mon_array = np.append(mon_array, 3*np.pi/2)
mon_array = np.append(mon_array, 2*np.pi)
print(mon_array)

#f) Avec les commandes Python, ajouter les valeurs manquantes de -3pi/2 et de -2pi à l'array.
mon_array = np.insert(mon_array, 0, -3*np.pi/2)
mon_array = np.insert(mon_array, 0, -2*np.pi)
print(mon_array)
```

## Question 4
```py
#a) Faire un array qui contient les valeurs entières de -20 à 20 en utilisant np.linspace. On l'appelle x.
x = np.linspace(-20,20,41) # il y a 40 valeurs entre -20 et 20, plus 1, donc 41 valeurs
print(x)

#b) Faire un autre array, appelé y_1, qui contient l'image (la valeur de y quand on met x dans l'expression) de $y = e^x -2$
y_1 = np.exp(x)-2
print(y_1)
#c) Faire une fonction nommée f, qui prend x en paramètre et qui retourne $x^2-9x+6$. Prendre le retour et le mettre dans un autre array, nommé y_2.
def f(x):
    return x**2-9*x+6

y_2 = f(x)
print(y_2)
#d) Pour chaque valeur de la liste y_1, imprimer si oui ou non, la valeur est supérieure ou égale à 5000.
print(y_1>=5000)

#e) faire une liste y_2_modifiee qui ne garde que les valeurs de y_2 qui sont inférieures à 100.
y_2_modifie = y_2[y_2<100]
print(y_2_modifie)
```