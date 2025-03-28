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