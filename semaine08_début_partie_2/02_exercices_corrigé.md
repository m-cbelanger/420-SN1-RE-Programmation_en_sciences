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

