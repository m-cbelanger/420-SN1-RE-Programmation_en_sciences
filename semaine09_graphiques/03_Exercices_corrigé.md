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
# a)

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