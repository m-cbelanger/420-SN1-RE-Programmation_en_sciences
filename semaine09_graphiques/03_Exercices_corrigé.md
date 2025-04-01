# Solutions exercices graphiques

## Question 1
a)

```py
def f(x):
    return 3*x**2-19

liste_x = np.linspace(-5,5,100)
liste_y = f(liste_x)

plt.figure()
plt.title("Une superbe fonction")

plt.plot(liste_x,liste_y,color = "magenta", linestyle = "dashdot", lw = 2, label = "$f(x)=3x^2-19$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0,color="blue",lw=3)
plt.axvline(0,color="blue",lw=3)

plt.legend(loc="upper center")
plt.show()
```

b)
```py
def h(x):
    return np.sin(3*x)*np.exp(1/x)

liste_x2 = np.linspace(1,50,50)
liste_y2 = h(liste_x2)

plt.figure()
plt.title("Une aute superbe fonction")
plt.plot(liste_x2, liste_y2, color = "orange", label = "$sin(3x)e^{1/x}$")
plt.xlabel("x")
plt.ylabel("y")

plt.legend(loc="upper center")
plt.show()
```

# Question 2

```py
# Question 2

jours = np.linspace(1,31,31)
mes_pas = [8755,12001,5200,18233,10225,9665,7889,8852,8665,9004,10899,11323,14324,12008,13120,9663,9451,10478,15988,16632,10479,10552,11223,11299,4563,11787,12332,10545, 12018,13554,5009]

plt.figure()
plt.plot(jours, mes_pas,color = "magenta", marker = "s")
plt.title("Nombre de pas effectués en mars")

plt.xlabel("journée")
plt.ylabel("pas")

plt.show()
```

# Question 3
### a)

```py
notes_cegep = [70,80,62,74,87,95,90,77,66,85,75,89,88,62,75,73,89,61,69,92]
notes_uni = [2.3,3.2,1.8,2.1,3.5,3.9,3.6,2.5,2.7,3.0,2.5,3.2,3.0,1.5,1.9,2.1,3.2,2.2,1.9,3.9]

plt.figure()
plt.scatter(notes_cegep,notes_uni, c=notes_uni,cmap="autumn", marker = "D")

plt.title("Notes à l'université en fonction des notes au cégep")
plt.xlabel("notes au cégep")
plt.ylabel("notes à l'université")

plt.show()
```

### b)
```py
# Question 3b)

puissance_moteur = [201,252,241,304,304,153,184,292,175,185,132,330,340,145,268,240,155,329,148,300,268,132,150,240]
consommation_essence = [6.6,7.4,5.9,8.6,8.6,6.4,6.4,7.7,7.0,7.2,6.3,9.6,6.7,6.3,7.5,7.0,5.8,8.5,7.0,7.8,8.4,6.4,5.9,6.7]

plt.figure()
plt.scatter(puissance_moteur, consommation_essence, c= consommation_essence, cmap='jet', marker='D')
plt.xlabel('puissance moteur (chevaux vapeur)')
plt.ylabel("consommation d'essence (L/100km)")
plt.title("Consommation d'essence en fonction \n de la puissance moteur")
plt.grid(True)
plt.colorbar()
plt.show()
```

### c)
```py
# Question 3c)

moyenne = np.mean(consommation_essence)
print(moyenne)

maxi = np.max(consommation_essence)
print(maxi)

etendue = np.max(consommation_essence) - np.min(consommation_essence)
print(etendue)

consommation_essence.append(6.7)
puissance_moteur.append(148)
```

### d)

```py
consommation_essence_2 = np.array(consommation_essence)
puissance_moteur_2 = np.array(puissance_moteur)

print(consommation_essence_2*10)

consommations_legeres = consommation_essence_2[consommation_essence_2 < 7.5]
print(consommations_legeres)

moyenne_moteurs_puissants = np.mean(puissance_moteur_2[puissance_moteur_2 > 300])
print(moyenne_moteurs_puissants)
```