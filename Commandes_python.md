# 📊 Commandes principales pour les graphiques en Python (Matplotlib)

## Importation de Matplotlib
```python
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.plot(x, y, color='red')  # Changer la couleur
plt.plot(x, y, 'r')  # Autre façon de changer la couleur
plt.plot(x, y, linestyle='--')  # Modifier le style de ligne
plt.plot(x, y, marker='o')  # Ajouter un marqueur
plt.plot(x, y, linewidth=2)  # Modifier l’épaisseur de ligne
plt.plot(x, y, marker='s', markersize=8)  # Modifier la taille des marqueurs
plt.plot(x, y, marker='D', markerfacecolor='yellow', markeredgecolor='black')  # Modifier l’apparence des marqueurs

plt.scatter(x, y)
plt.scatter(x, y, color='blue')  # Changer la couleur des points
plt.scatter(x, y, s=50)  # Modifier la taille des points
plt.scatter(x, y, alpha=0.5)  # Modifier la transparence
plt.scatter(x, y, c='red', edgecolors='black')  # Ajouter un contour aux points
plt.scatter(x, y, c=z, cmap='viridis')  # Définir une couleur en fonction d'une variable

plt.xlabel("Axe X")  # Ajouter un label à l'axe X
plt.ylabel("Axe Y")  # Ajouter un label à l'axe Y
plt.title("Titre du graphique")  # Ajouter un titre
plt.xlim(0, 10)  # Définir les limites de l'axe X
plt.ylim(0, 20)  # Définir les limites de l'axe Y
plt.xticks([0, 2, 4, 6, 8, 10])  # Modifier les graduations de l'axe X
plt.yticks([0, 5, 10, 15, 20])  # Modifier les graduations de l'axe Y


plt.plot(x, y, label="Courbe 1")
plt.plot(x2, y2, label="Courbe 2")
plt.legend()  # Afficher la légende
plt.legend(loc="upper right")  # Définir la position de la légende

plt.grid(True)  # Activer la grille
plt.grid(linestyle='--', linewidth=0.5)  # Personnaliser la grille

plt.show()

