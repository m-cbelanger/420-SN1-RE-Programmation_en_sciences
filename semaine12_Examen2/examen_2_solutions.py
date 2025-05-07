import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Question 2
nom = ["Jean Tremblay", "Sophie Gagnon", "Michel Bélanger", "Isabelle Lévesque", "Marc Martel", "Catherine Dion", 
        "Pierre Lapointe", "Louise Roy", "François Dubois", "Marie-Claude Morin", "Éric Bergeron", "Julie Beauchamp", 
        "Martin Giroux", "Sylvie Blanchet", "Patrick Caron", "Nathalie Fournier", "Robert Thibault", "Lucie Gauthier", 
        "Daniel Lemieux", "Caroline Poirier", "André Plamondon", "Chantal Gosselin", "Yves Gadbois", "Hélène Lavoie", 
        "Mathieu Beaulieu", "Suzanne Girard", "Richard Pelletier", "Annie Simard", "Philippe Rousseau", "Manon Lapierre", 
        "Denis Chénier", "Brigitte Fortin", "Jacques Lefebvre", "Geneviève Gagné", "Christian Dubé"]
probleme_sante = ["hypertension", "diabète de type 2", "asthme", "obésité", "maladie cardiaque", "arthrite", "dépression", 
              "aucune", "asthme", "hypertension", "aucune", "aucune", "dépression", "obésité", "aucune", "maladie cardiaque", 
              "aucune", "aucune", "asthme", "hypertension", "diabète de type 2", "aucune", "aucune", "obésité", "dépression",
              "aucune", "hypertension", "asthme", "aucune", "arthrite", "diabète de type 2", "aucune", "aucune", 
              "maladie cardiaque", "aucune"]
rythme_cardiaque = [72, 85, 90, 78, 95, 100, 68, 75, 80, 92, 88, 79, 82, 96, 70, 65, 88, 94, 76, 83, 
                      98, 71, 84, 77, 91, 86, 73, 87, 93, 69, 74, 81, 89, 97, 67]


#a)
print(len(nom))

#b)
index = nom.index("Denis Chénier")
print(probleme_sante[index])

#c)
nom.append("Jonathan Roberge")
probleme_sante.append("épilepsie")
rythme_cardiaque.append(98)

#d)
moyenne = np.mean(rythme_cardiaque)
print(moyenne)

#e)
rythme_cardiaque = np.array(rythme_cardiaque)
nombre = rythme_cardiaque[rythme_cardiaque>=75]
print(len(nombre))

#f)
print(f"personne rencontrée: {nom[15]}. Problème: {probleme_sante[15]}")


#g)
if "migraine" in probleme_sante:
    print("oui")
else:
    print("non")
    
#h)
print(max(rythme_cardiaque)-min(rythme_cardiaque))

#i)
nom.pop(8)



#Question 3

def h(t):
    return np.cos(5*t)*np.exp(-0.1*t)


print(round(h(2),3))

liste_t = np.linspace(0,40,400)
liste_h = h(liste_t)

plt.figure(figsize = (9,6))
plt.plot(liste_t,liste_h, color = "magenta", linestyle=":")
plt.xlabel("Temps")
plt.ylabel("Hauteur du ressort")
plt.title("Simulation du mouvement d'un ressort")
plt.grid(True)
plt.axhline(0, color = "black")
plt.show()



#Question 4

#pd.read_excel("voyages.xlsx").to_csv("voyages.csv", index=False, sep=',', encoding='utf-8-sig')
data = pd.read_csv("voyages.csv", encoding="utf-8")
#data.info()

#a)
data_filtree = data.query('moyen_transport.str.contains("avion", na=False)')
#b)
x = data_filtree["kilometres"].tolist()
y = data_filtree["minutes"].tolist()

plt.figure(figsize=(9,6))
plt.scatter(x,y, c=y, cmap = 'cubehelix', marker = 's')
plt.xlabel("Distance (km)")
plt.ylabel("Temps du voyage (minutes)")
plt.title("Temps du voyage selon la distance à parcourir")
plt.grid(True)
plt.show()

#c)
minutes = data['minutes'].tolist()

minutes = np.array(minutes)
heures = minutes/60
print(heures)

#d)
print(heures < 2)


