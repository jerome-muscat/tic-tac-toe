import random
from ia import board
from ia import ia

test = 0

def Tableau():
    tableau = [" ", " ", " ",
               " ", " ", " ",
               " ", " ", " "]
    return tableau

def impression_tableau(tableau):
    print("Voici le tableau:")
    print(tableau[0], "|", tableau[1], "|", tableau[2])
    print("---------")
    print(tableau[3], "|", tableau[4], "|", tableau[5])
    print("---------") 
    print(tableau[6], "|", tableau[7], "|", tableau[8])

def debut_partie():
    joueurs = []
    joueur = []
    i=0
    while i < 2 :
        #demande de prenom
        i += 1
        x = str(i)
        nom=(input("Quel est ton prénom joueur " + x + " ? "))
        print('Bonjour ' + nom)
        joueur+=[nom]
        
    
    #determine qui débute la partie
    commence = str((random.choice(joueur)))
    print(commence + " débutera la partie" )

    joueurs += [commence]

    for i in joueur:
        if i not in joueurs:
            joueurs += [i]

    return joueurs

def signe(joueur):
    signe = []
    signe_joueur1=""
    while "X" != signe_joueur1.upper() and "O" != signe_joueur1.upper():
        signe_joueur1 = input(joueur + ", tu veux jouer avec X ou O ? ").upper()
    
    signe += [signe_joueur1]
    if "X" not in signe:
        signe_joueur2 = "X"
    else:
        signe_joueur2 = "O"
        
    signe += [signe_joueur2]

    return signe

def ou_jouer(symbole, tableau, joueur):
    print("\nA", joueur, "de jouer")
    je_veux_jouer = int(input("Choisis un endroit de 1 à 9: "))
    while (je_veux_jouer <= 0 or je_veux_jouer >= 10 or tableau[je_veux_jouer - 1] != " "):
        print("Case déjà joueur")
        je_veux_jouer = int(input("Choisis un endroit de 1 à 9: "))
    tableau[je_veux_jouer-1] = symbole
    return tableau

gagne = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        #|     verification lignes     |  |    verification colonnes    ||verification diagonalle|

def detectGagne(tableau, joueur):
    global gagne
    for i in range(0, len(gagne)):
        if (tableau[gagne[i][0]] == tableau[gagne[i][1]] and tableau[gagne[i][1]] == tableau[gagne[i][2]] and tableau[gagne[i][0]] != ' '):
            impression_tableau(tableau)
            print('\n', joueur, 'gagne la partie !')
            return True
    return False

def score(joueur, signes, manches):
    Score = [[joueur[0], " ", test], 
             [joueur[1], " ", test]]
    i = 1
    while i != len(joueur[0]):
        i+=1
    
    Score[0][1] = signes[0]

    x = 1
    while x != len(joueur[1]):
        x+=1

    while len(Score[0][0]) != len(Score[1][0]) :
        if x < i:
            y = i - x
            Score[0][0] = joueur[0]
            Score[1][0] = joueur[1] + (" " * y)
        if x > i:
            y = x - i
            Score[0][0] = joueur[0] + (" " * y)
            Score[1][0] = joueur[1]

    Score[1][1] = signes[1]

    if manches % 2 == 0:
        Score[0][2] += 1
    else: 
        Score[1][2] += 1

    print("__________________")
    print( "|", Score[0][0], "|", Score[0][1], "|", Score[0][2], "|") 
    print("|" + "________________" + "|")
    print( "|", Score[1][0], "|", Score[1][1], "|", Score[1][2], "|")
    print("|" + "________________" + "|")

def jeu():
    tableau = Tableau()
    global joueur
    joueur = debut_partie()
    joueur1 = joueur[0]
    joueur2 = joueur[1]

    global signes
    signes = signe(joueur1)
    signe1 = signes[0]
    signe2 = signes[1]

    manches = 0
    while True:
        impression_tableau(tableau)
        if manches % 2 == 0:
            ou_jouer(signe1, tableau, joueur1)
        else:
            ou_jouer(signe2, tableau, joueur2)
        if detectGagne(tableau,None):
            if manches % 2 == 0:
                detectGagne(tableau, joueur1)
            else:
                detectGagne(tableau, joueur2)
            scores = score(joueur, signes, manches)
            break

        manches += 1
        if manches == 9:
            impression_tableau(tableau)
            print('\nMatch nul !!!')
            break
    

def continue_jeu():
    tableau = Tableau()
    joueur1 = joueur[0]
    joueur2 = joueur[1]

    signe1 = signes[0]
    signe2 = signes[1]
    
    manches = 0
    while True:
        impression_tableau(tableau)
        if manches % 2 == 0:
            ou_jouer(signe1, tableau, joueur1)
        else:
            ou_jouer(signe2, tableau, joueur2)
        if detectGagne(tableau,None):
            if manches % 2 == 0:
                detectGagne(tableau, joueur1)
            else:
                detectGagne(tableau, joueur2)
            scores = score(joueur, signes, manches)
            break

        manches += 1
        if manches == 9:
            impression_tableau(tableau)
            print('\nMatch nul !!!')
            break

def recommence():
    reponse = str(input("\nVoulez vous recommencer ? "))
    while (reponse.lower() == "oui"):
        reset = str(input("\nVoulez vous changer les joeurs ? "))
        print('\n\n\n\n\n--- NOUVELLE PARTIE --- \n')  # saut de lignes
        if (reset.lower() == "oui"):
            jeu()
        elif (reset.lower() == "non"):
            continue_jeu()
        else:
            break
        recommence()

jeu()
recommence()