# Révision finale

import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Question 1
def question1():
    prenoms = ["Jean", "Marie", "Pierre", "Claire", "Antoine", "Sophie", "Luc", "Anne", "François", "Catherine", "Louis", "Élise", "Philippe", "Valérie", "Guillaume", "Sophie", "Marc", "Sébastien", "Jean", "Louis"] 
    abonnement =[False, False, False, True, True, True, False, True, False, True, False, True, True, True, True, True, True, False, True, False]
    ages = [23, 61, 54, 36, 63, 44, 25, 70, 55, 46, 30, 35, 59, 41, 17, 33, 42, 28, 61, 19]
    argent_epargne = [15.15, 18.95, 4.07, 85.77, 51.52, 10.15, 4.51, 52.68, 8.92, 16.27, 28.98, 40.64, 53.84, 89.51, 71.70, 67.59, 5.77, 19.54, 74.14, 15.51]
    # a) Combien d’argent total a été épargné par les participants qui sont abonnés? Prendre une boucle pour trouver la réponse.
    argent_total = 0
    for i in range(len(argent_epargne)):
        if abonnement[i] == True:
            argent_total =  argent_total + argent_epargne[i]
    print(f"L'argent total épargné est {round(argent_total,2)}$")

    # b) Les participants qui sont abonnés et qui ont 55 ans et plus ainsi que les participants qui ont moins de 20 ans sont admissibles à un rabais lors de leur prochain achat. Faire une liste qui récupère le nom des personnes qui sont admissibles au rabais. Prendre une boucle pour y arriver et mettre les noms dans une nouvelle liste.
    noms_rabais = []
    for i in range(len(prenoms)):
        if (ages[i] >= 55 or ages[i] < 20) and abonnement[i] == True:
            noms_rabais.append(prenoms[i])
    print("Les noms des personnes concernées sont: ",noms_rabais)

    # c) En moyenne, combien d’argent les participants ont-ils épargné?
    # pour pratiquer les boucles:
    somme = 0
    for i in range(len(argent_epargne)):
        somme = somme + argent_epargne[i]

    moyenne = somme / len(argent_epargne)
    print(f"La moyenne est {round(moyenne,2)}$")

    # d) Combien de participants sont au-dessus de la moyenne d'épargne?
    compteur = 0
    for i in range(len(argent_epargne)):
        if argent_epargne[i] > moyenne:
            compteur += 1
    print(f"Il y a {compteur} épargnants au-dessus de la moyenne")

    # e) On fait un tirage au sort et les personnes dont le prénom est Louis ou Claire gagnent 100$! Ajouter les 100$ au montant épargné pour les personnes qui ont gagné.
    print("Avant: ", argent_epargne)
    for i in range(len(prenoms)):
        if prenoms[i] == 'Louis' or prenoms[i] == 'Claire':
            argent_epargne[i] += 100
    print("Après: ", argent_epargne)      


    # f) Quel est le pourcentage de personnes dont la dernière lettre du prénom est un "e"?
    nombre_fini_e = 0
    for i in range(len(prenoms)):
        chaine = prenoms[i]
        if chaine[-1] == 'e':
            nombre_fini_e += 1
            
    pourcentage = nombre_fini_e / len(prenoms) *100
    print(f"Il y a {pourcentage}% des prénoms de la liste qui finissent par e.")
    # g) Combien de personnes faut-il parcourir dans la liste de gauche à droite avant de rencontrer la 2e personne qui a moins de 25 ans?
    total = 0
    moins_25 = 0
    for i in range(len(ages)):
        total += 1
        if ages[i] < 25:
            moins_25 += 1
            if moins_25 == 2:
                break

    print(f"Il a fallu parcourir {total} personnes pour rencontrer la 2e qui a moins de 25 ans")

    # h) Jeu de devinette! Faites un petit jeu qui demande à l'utilisateur d'entrer un âge. Si l'âge se trouve dans la liste des âges, l'utilisateur gagne. À chaque joute, on doit lui demander s'il veut rejouer. On doit aussi lui laisser un maximum de 5 chances!
    max_chances = 5
    essais = 0
    trouve = False
    while trouve == False and essais < max_chances:
        devine = int(input("Entre un âge et je te dirai s'il est dans la liste: "))
        essais += 1
        if devine in ages:
            trouve = True
            print(f"Bravo, tu as trouvé! {devine} ans est bien dans la liste!")
        elif essais < max_chances:
            print(f"Il te reste {max_chances - essais} chances de deviner")
        else:
            print("Dommage, tu n'as pas trouvé! Aurevoir")


# Question 2
def question2():
    # a) Importer le fichier livres.csv dans votre fichier Python.
    data = pd.read_csv("livres.csv",encoding='utf-8')
    data.info()
    print(data.head())
    
    # b) Calculer combien de pages seraient lues si on lisait tous les livres de la liste qui sont des romans et dont l’auteur est décédé. 
    # Plusieurs autres méthodes possibles
    data_filtree = data.query('style.str.contains("Roman") and decede == "oui"')
    print(data_filtree)
    pages_filtree = data_filtree['nombre_pages'].tolist()
    total_pages = sum(pages_filtree)
    print(f"Au total, {total_pages} pages de romans d'auteurs décédés")
    
    # c) Faire une liste avec tous les noms des auteurs qui ont écrit plus de 30 livres et dont le livre de la liste est un roman. (ne pas tenir compte des filtres des sous-questions précédentes)
    # Plusieurs méthodes possibles
    auteurs = data['auteur'].tolist()
    nombre_livres = data['nombre_livres'].tolist()
    type_livre = data['style'].tolist()
    
    auteurs_retenus = []
    for i in range(len(auteurs)):
        if nombre_livres[i] >= 15 and type_livre[i] == 'Roman':
            auteurs_retenus.append(auteurs[i])
    print("Voici les auteurs retenus: ", auteurs_retenus)
    
    # d) Lequel des livres a le plus de pages? (ne pas tenir compte des filtres des sous-questions précédentes).
    titres = data['titre'].tolist()
    nombre_pages = data['nombre_pages'].tolist()
    pages_max = max(nombre_pages)
    index = nombre_pages.index(pages_max)
    
    print(f"Le livre ayant le plus de pages est {titres[index]} de {auteurs[index]}")
    
    # e) Combien de pages y a-t-il en moyenne dans la liste? (ne pas tenir compte des filtres des sous-questions précédentes).
    # peut se faire avec une boucle aussi!
    moyenne = np.mean(nombre_pages)
    print(f"Il y a en moyenne {moyenne} pages par livre")
    
    # f) Imprimer qui est l’auteur de « La plus grosse poutine du monde » et son nombre de pages.
    for i in range(len(titres)):
        if titres[i] == 'La plus grosse poutine du monde':
            print(f"La plus grosse poutine du monde a été écrit par {auteurs[i]} et contient {nombre_pages[i]} pages")
            break
        
        
    '''
    g) Présenter le nuage de points du nombre de livre en fonction de l’âge des auteurs. Ne garder que les livres dont l'âge des auteurs est en dessous de la moyenne. Faire une présentation esthétique en mettant :
    -une couleur graduée de votre choix, allant de bas en haut
    -une forme de « marker » différente que celle par défaut
    -des titres aux 2 axes
    -un titre général
    -une fenêtre (figure) plus grande que celle par défaut
    -un quadrillage
    '''

    age_auteurs = data['age'].tolist()
    # nombre de livres déjà créée
    
    plt.figure(figsize = (9,6))
    plt.scatter(age_auteurs,nombre_livres,c=nombre_livres,cmap='ocean', marker = 'D')
    plt.title("Nombre de livres selon l'âge des auteurs")
    plt.xlabel("Âge")
    plt.ylabel("Nombre de livres")
    plt.grid(True)
    plt.colorbar()
    plt.show()
    
       
    # h) De tous les auteurs, combien d'entre eux ont la lettre J ou la lettre G comme première lettre du prénom?
    compteur = 0
    for i in range(len(auteurs)):
        chaine = auteurs[i]
        if chaine[0] == 'J' or chaine[0] == 'G':
            compteur += 1
    
    print(f"Il y a {compteur} noms qui débutent par J ou G")
    
    
def question3():
    '''
    a)
    - la variable x qui sert de compteur n'est pas initialisée
    - la variable x qui sert de compteur n'est jamais incrémentée (risque de boucle infinie)
    - on demande a l'utilisateur s'il veut rejouer, mais on ne fait rien
    avec le contenu de la variable. On l'ajoute dans les conditions pour continuer la boucle 
    - idéalement, afficher le nombre pigé et poser la question de rejoute après
    '''
    # voici le code corrigé:
    compteur_petits = 0
    compteur_grands = 0
    x=0
    saisie = 'oui' # Mettre saisie à oui pour entrer au moins une fois.
    while x < 10 and saisie == 'oui':
        x += 1
        pige = random.random()
        print(f"Nombre pigé: {pige}")
        if pige <= 0.5:
            compteur_petit = compteur_petits + 1
        else:
            compteur_grands= compteur_grands + 1
        saisie = input("Voulez-vous rejouer? Entrer oui pour continuer: ")
        
    print(f"Après 10 essais, on a obtenu {compteur_grands} nombres au-dessus de 0.5 et {compteur_petits} nombres en bas ou égal à 0.5")
    
    
    '''
    b)
    - Tant qu'on entre des nombre (des années), le code va fonctionner. Il arrêtera de fonctionner si on saisie "stop"
    '''
    while saisie != 'stop':
        annee_aleatoire = random.randint(1920, 2025)
        # on enlève le int devant input
        annee_utilisateur = input("Entrez votre année de naissance (ou tapez 'stop' pour quitter) : ")
        
        # On vérifie s'il y a stop, si oui on sort
        if annee_utilisateur == "stop":
            break
        
        # Si on est toujours là, c'est qu'on n'a pas entré stop. On met donc l'entrée en nombre
        # On pourrait ajouter des vérifications supplémentaires, mais ça n'est pas évalué
        annee_utilisateur = int(annee_utilisateur)
        
        ecart = abs(annee_utilisateur - annee_aleatoire)
        print(f"Année pigée : {annee_aleatoire}")
        print(f"Votre année : {annee_utilisateur}")
        print(f"Écart d’âge : {ecart} ans")

        if annee_utilisateur < annee_aleatoire:
            print("Vous êtes le plus vieux!")
        elif annee_utilisateur > annee_aleatoire:
            print("Vous êtes le plus jeune!")
        else:
            print("Vous avez le même âge!")
            
        '''
        c) Si on veut aller de 1 à 5, on doit écrire 1 à 6
        
        d) Même chose, on doit écrire 1 à 11 et non 1 à 10
        '''
        
        
question1()
question2()
question3()