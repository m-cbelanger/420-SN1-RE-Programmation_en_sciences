import matplotlib.pyplot as plt
import numpy as np

x = np.array([-2,-1,0,1,2])
x = np.array([-2,-1.5,-1,-0.5,0,0.5,1,1.5,2])
x = np.linspace(-2,2,50)
y1 = x**2
y2 = np.atan(x)
y3 = np.sin(x)

plt.title("Graphique des courbes $x^2$, $sin(x)$ et $arctan(x)$")

plt.plot(x,y1,label="quadratique",color = "green",lw = 8,linestyle = "-.", alpha=0.4)
plt.plot(x,y2,label="arctan", color = "purple")
plt.plot(x,y3,label="sinus", color = "red")

plt.xlabel("abscisses")
plt.ylabel("ordonnées")

plt.axhline(0,color ="black")
plt.axvline(0,color ="black")



plt.legend(loc = "upper left")
plt.show()

