import numpy

print("Question 1")
#Question 1
temps_minutes = ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00']
vitesse = [0, 51.2, 79.2, 100.5, 105.3, 104.2, 110.3, 105.6, 102.6, 103, 105.6, 110.5, 111, 118.9, 110.2, 110.2, 108.9, 108, 70.6, 49.6, 0]

#a) Quelle était la vitesse à 5:30?
# avec index:
print("a)")
mon_index = temps_minutes.index('05:30')
print(f"La vitesse à 5:30 était {vitesse[mon_index]} km/h")
# avec boucle:
for i in range(len(temps_minutes)):
    if temps_minutes[i] == '05:30':
        print(f"La vitesse à 5:30 était {vitesse[i]} km/h")

#b) À combien de reprises la vitesse détectée a été au-dessus de 110 km/h?
print("b)")
# boucle for i in range:
nb_vitesse_plus_de_110 = 0
for i in range(len(vitesse)):
    if vitesse[i] > 110:
        nb_vitesse_plus_de_110 = nb_vitesse_plus_de_110 + 1
print(f"Il y eu {nb_vitesse_plus_de_110} prises de mesures au-dessus de 110 km/h")

# boucle for element in liste
nb_vitesse_plus_de_110 = 0
for element in vitesse:
    if element > 110:
        nb_vitesse_plus_de_110 = nb_vitesse_plus_de_110 + 1
print(f"Il y eu {nb_vitesse_plus_de_110} prises de mesures au-dessus de 110 km/h")

#c) Quel est le pourcentage des données récoltées qui sont au-dessus de 110 km/h?
print("c)")
pourcentage = round(nb_vitesse_plus_de_110/len(vitesse) *100, 1)
print(f"Il y a eu {pourcentage}% vitesses au-dessus de 110 km/h")

#d) Quelle a été la vitesse récoltée la plus élevée?
print("d)")
#méthode facile:
maximum = max(vitesse)

#méthode pour pratiquer les boucles:
maximum = 0 #Choisir une petite valeur pour qu'elle soit surclassée
for i in range(len(vitesse)):
    if vitesse[i] > maximum:
        maximum = vitesse[i]

print(f"La vitesse max est {maximum} km/h")

#e) Quelle a été la moyenne de vitesse? 
print("e)")
# méthode simple
moyenne = round(numpy.mean(vitesse),1)
print(f"La moyenne est {moyenne} km/h")

# méthode pour pratiquer les boucles
somme = 0
for i in range(len(vitesse)):
    somme = somme + vitesse[i]
moyenne = somme / len(vitesse)
print(f"La moyenne est {moyenne} km/h")

#f) Faire une liste des vitesses en m/s. La conversion pour passer de km/h à m/s est de diviser les km/h par 3.6.
print("f)")
vitesse_ms = []

for i in range(len(vitesse)):
    vitesse_ms.append(vitesse[i] /3.6)
        
print(f"vitesse = {vitesse}")

#g) Quel a été le taux de variation moyen entre chaque duo de temps. Garder la liste en km/h et mettre les résultats dans la liste TVM.
print("g)")
TVM = []
for i in range(len(vitesse)):
    if i < len(vitesse)-1: # pour ne pas passer tout droit à la fin du tableau
        taux_moyen = (vitesse[i] + vitesse[i+1]) / 2
        TVM.append(taux_moyen)

print(f"TVM = {TVM}")

print()
print()
#Question 2
print("Question 2")
janvier_min = [-10,-8,-4,-15,-17,-17,-12,-15,-16,-10,-11,-19,-13,-15,-16,-16,-20,-19,-25,-19,-20,-20,-17,-17,-9,-2,-2,-2,-9,-15,-11]
janvier_max = [-6,-1,0,0,-8,-10,-8,-3,-5,2,0,-7,-1,-1,-6,-8,-11,-7,-13,-9,-10,-2,-3,-7,1,0,0,2,-1,-9,-3]

#a)
print("a)")
print(len(janvier_max))
print(len(janvier_min))


#Quelles étaient les températures min et max le 15 janvier 2024?
print("b)")
print(janvier_min[14], "degrés min")
print(janvier_max[14], "degrés max")


#c) Combien y a-t-il eu de journées où il y a eu des températures au dessus de 0?
print("c)")

nb_jours_plus_de_zero = 0 #initialiser la variable à 0 une fois, avant la boucle
#range
for i in range(len(janvier_min)):
    if janvier_max[i] > 0:
        nb_jours_plus_de_zero = nb_jours_plus_de_zero+1
       
print(f"nb_jours_plus_de_zero = {nb_jours_plus_de_zero}")

#Calculer l'écart de température entre le max et le min. Mettre les résultats dans une nouvelle liste nommée janvier_ecarts
print("d)")
janvier_ecart = [] #initialiser la liste vide une fois, avant la boucle
for i in range(len(janvier_max)):
    ecart = janvier_max[i] - janvier_min[i]
    janvier_ecart.append(ecart)

print(f"janvier_ecart : {janvier_ecart}")

#Maintenant, faire une liste janvier_milieu qui se rempli avec le milieu entre la plus haute et la plus basse température.
#Le milieu entre 2 valeur est la somme des valeurs divisé par 2
print("e)")
janvier_milieu = [] #initialiser la liste vide une fois, avant la boucle
for i in range(len(janvier_max)):
    janvier_milieu.append((janvier_min[i] + janvier_max[i]) / 2)

print(f"janvier_milieu: {janvier_milieu}")

print()
print()
print("Question 3")
#Question 3
chimie1 = "Équation chimique de la combustion du méthane: CH4 + 2O2 -> CO2 + 2H2O"
chimie2 = "Équation chimique de la synthèse de l'eau: 2H2 + O2 -> 2H2O"
chimie3 = "Équation chimique de la combustion du propane: Na + Cl2 -> 2NaCl"
chimie4 = "Équation chimique de la neutralisation: HCl + NaOH -> NaCl + H2O"
chimie5 = "Équation chimique de la précipitation: NaCl + AgNO3 -> AgCl + NaNO3"

print("a)")
liste_chimie =[chimie1,chimie2,chimie3,chimie4,chimie5]
compteur = 0
for element in liste_chimie:
    if "H2O" in element:
        compteur = compteur + 1
print(f"compteur = {compteur}")


#Question 3b)
print("b)")
# façon raccourcie
mon_index = chimie1.index(":")
equation = chimie1[mon_index + 1:]
print(equation)
# avec boucles
equation1  = ""
drapeau = False
for i in range(len(chimie1)):
    if chimie1[i] == ":":
        drapeau = True
    if drapeau == True:
        equation1 = equation1 + chimie1[i]
print(equation)

#Question 3c)
print("c)")
liste_equations =[]
for i in range(len(liste_chimie)):
    mon_index = liste_chimie[i].index(":")  #remarquer qu'on remplace chimie1 par liste_chimie[i]
    equation = liste_chimie[i][mon_index + 1:] #idem
    liste_equations.append(equation)
    
print(f"liste_equations = {liste_equations}")

#Question 3d)
print("d)")
nb_caracteres = 0
nb_voyelles = 0
nb_H = 0
voyelles = ["a","A","e","E","i","I","o","O","u","U","y","Y"]
for element in chimie1:
    if element != " ":
        nb_caracteres = nb_caracteres + 1
    if element in voyelles:
        nb_voyelles = nb_voyelles + 1
    if element == "H":
        nb_H = nb_H + 1
    
print(f"nb_caracteres : {nb_caracteres}, nb_voyelles : {nb_voyelles}, nb_H : {nb_H} ")        
        
    
