import math
import random
import time

class Carte:
    def __init__(self, valeur, symbole):
        self._valeur = valeur
        self._symbole = symbole
        self._visible = False
        self._dos = "#####"
        ##La variable enJeu permet de savoir si la carte est toujours active dans le jeu du memory
        self._enJeu = True
        
    def __get_valeur(self):
        return self._valeur
        
    def __set_valeur(self, valeur):
        self._valeur = valeur
        
    valeur = property(__get_valeur, __set_valeur)
    
    def __get_symbole(self):
        return self._symbole
        
    def __set_symbole(self, symbole):
        self._symbole = symbole
        
    symbole = property(__get_symbole, __set_symbole)
    
    def __get_visible(self):
        return self._visible
        
    def __set_visible(self, visible):
        self._visible = visible
        
    visible = property(__get_visible, __set_visible)
    
    def __get_enJeu(self):
        return self._visible
        
    def __set_enJeu(self, enJeu):
        self._enJeu = enJeu
        
    enJeu = property(__get_enJeu, __set_enJeu)
    
    def __str__(self):
        if self._visible == True:
            return "["+str(self._valeur)+"/"+self._symbole+"]"
        else:
            return str(self._dos)
    
    def retourner(self):
        self._visible = not self._visible

class CarteMemory(Carte):
    def __init__(self, valeur, symbole):
        Carte.__init__(self, valeur, symbole)

    def correspond(self, carte2):
        return self._symbole==carte2._symbole and self._valeur==carte2._valeur

class Carte32(Carte):
    def __init__(self, valeur, symbole):
        Carte.__init__(self, valeur, symbole)

    ##Permet de vérifier si les suites correspondent ainsi que les valeurs
    def correspond(self, carte2):
        return ((self._symbole in ["C", "S"] and carte2._symbole in ["C", "S"]) or (self._symbole in ["H", "D"] and carte2._symbole in ["H", "D"])) and (self._valeur==carte2._valeur)

    ##Transformation des lettres en leur valeur chiffrée respective pour pouvoir les comparer
    def comparer(self, carte2):
        valeurTmp1=self._valeur
        valeurTmp2=carte2._valeur
        
        if valeurTmp1=="V":
            valeurTmp1=11
        if valeurTmp1=="D":
            valeurTmp1=12
        if valeurTmp1=="K":
            valeurTmp1=13
        if valeurTmp1=="A":
            valeurTmp1=14

        if valeurTmp2=="V":
            valeurTmp2=11
        if valeurTmp2=="D":
            valeurTmp2=12
        if valeurTmp2=="K":
            valeurTmp2=13
        if valeurTmp2=="A":
            valeurTmp2=14

        return valeurTmp1>valeurTmp2       
    
class Plateau:
    def __init__(self, nbPaires, typePaquet):
        self._paquet = []
        self._nbPaires = nbPaires

        ##typePaquet==0 >> paquet de memory classique
        if typePaquet==0:          
            if self._nbPaires>13 : 
                print(str(self._nbPaires)+" est trop grand, le nombre de paires est rabaissé à 10.")
                self._nbPaires=10
            if self._nbPaires<0 :
                print(str(self._nbPaires)+" est trop petit, le nombre de paires est augmenté à 10.")
                self._nbPaires=10
            
            for i in range (0, self._nbPaires):
                carteTmp1=CarteMemory(i, chr(i+65))
                carteTmp2=CarteMemory(i, chr(i+65))
                self._paquet.append(carteTmp1)
                self._paquet.append(carteTmp2)
        ##Sinon utilisation du paquet de 32 cartes
        else:
            for i in ["S", "H", "C", "D"]:
                for j in [7, 8, 9, 10, 'V', 'D', 'K', 'A']:
                    carteTmp1=Carte32(j, i)
                    self._paquet.append(carteTmp1)

        self._nbPairesRestantes = self._nbPaires
        self._nbCartes = len(self._paquet)
        self._nbCartesRestantes = len(self._paquet)-1
        
        ##Permet de connaitre la dimension du carré pour la présentation du memory sur le plateau
        self._dimension = math.sqrt(self._nbPaires*2)
        if self._dimension%1!=0:
            self._dimension = int(self._dimension)+1

        random.shuffle(self._paquet)

    def __get_nbPaires(self):
        return self._visible
        
    def __set_nbPaires(self, nbPaires):
        self._nbPaires = nbPaires
        
    nbPaires = property(__get_nbPaires, __set_nbPaires)

    def __get_nbPairesRestantes(self):
        return self._nbPairesRestantes
        
    def __set_nbPairesRestantes(self, nbPairesRestantes):
        self._nbPairesRestantes = nbPairesRestantes
        
    nbPairesRestantes = property(__get_nbPairesRestantes, __set_nbPairesRestantes)    

    ##Affichage du jeu de Memory avec son ration carré
    def strMemory(self):
        ligne = ""
        for carte in range (0, len(self._paquet)):
            if carte!=0 and carte%self._dimension == 0:
               ligne+='\n'
            ligne+="["+str(carte+1).zfill(2)+"]"+str(self._paquet[carte])+" "          
        return ligne

    ##Affichage du jeu +/-, on voit seulement la dernière carte retournée à droite, et le reste du deck face cachée à gauche
    def strCarte32(self, indice):
        ligne = ""
        self._paquet[indice].retourner()
        if indice<31:
            ligne+= str(self._paquet[indice+1]) +" "+str(self._paquet[indice])
        else:
            ligne+= str(self._paquet[indice])
        self._paquet[indice].retourner()         
        return ligne
    
class Joueur:
    def __init__(self, nom = "Inconnu"):
        self._nom = nom
        self._nbCoups = 0
        self._cartesGagnees = []
        self._score = 0
        
    def __get_nom(self):
        return self._nom
        
    def __set_nom(self, nom):
        self._nom = nom
        
    nom = property(__get_nom, __set_nom)
    
    def __get_nbCoups(self):
        return self._nbCoups
        
    def __set_nbCoups(self, nbCoups):
        self._nbCoups = nbCoups
        
    nbCoups = property(__get_nbCoups, __set_nbCoups)
    
    def __get_cartesGagnees(self):
        return self._cartesGagnees
        
    def __set_cartesGagnees(self, liste):
        self._cartesGagnees = liste
        
    cartesGanees = property(__get_cartesGagnees, __set_cartesGagnees)
    
    def __get_score(self):
        return self._score
        
    def __set_score(self, score):
        self._score = score
        
    score = property(__get_score, __set_score)
    
    def __str__(self):
        return self._nom.rjust(12)+" / Nombre de coups : "+str(self._nbCoups).zfill(2)+" / Score : "+str(self._score).zfill(2)+" / "+str(self._cartesGagnees)        

class Memory:
    def __init__(self, joueurs, nbPaires, typePaquet):
        self._listeJoueurs = joueurs
        random.shuffle(self._listeJoueurs)
        self._plateau = Plateau(nbPaires, typePaquet)

    def __str__(self):
        print("Nombre de paires : "+str(self._plateau._nbPaires)+", Nombre de paires restantes : "+str(self._plateau._nbPairesRestantes))
        chaine = self._plateau.strMemory()+"\n"       
        for joueur in range (0, len(self._listeJoueurs)):
            chaine+=str(self._listeJoueurs[joueur])+"\n"          
        return chaine
    
    def play(self):
        numJoueur = 0
        perdu = False
        joueurTmp=self._listeJoueurs[numJoueur]
        
        while(self._plateau._nbPairesRestantes!=0):
            ##Si le précédent joueur a perdu alors on passe au joueur suivant
            ##Le modulo permet de boucler une fois tous les joueurs passés
            if perdu == True:
                numJoueur+=1
                numJoueur=numJoueur%(len(self._listeJoueurs))
                joueurTmp=self._listeJoueurs[numJoueur]
                perdu = False
                
            print(self)
            print("Au tour de "+str(joueurTmp._nom))

            choix=False
            while choix==False:
                indiceChoix1=int(input("Première carte à retourner : "))-1
                if indiceChoix1>=0 and indiceChoix1<self._plateau._nbCartes:
                    if self._plateau._paquet[indiceChoix1]._enJeu==True:
                        choix=True
                    else:
                        print("Vous ne pouvez pas choisir une carte déjà gagnée.")
                else:
                    print("Merci de choisir une carte sur le plateau.")
            
            carteTmp1=self._plateau._paquet[indiceChoix1]
            carteTmp1.retourner()            
            print(self._plateau.strMemory())

            choix=False
            while choix==False:
                indiceChoix2=int(input("Deuxième carte à retourner : "))-1
                if indiceChoix2>=0 and indiceChoix2<self._plateau._nbCartes:
                    if self._plateau._paquet[indiceChoix2]._enJeu==True:                        
                        if indiceChoix1!=indiceChoix2:
                            choix=True
                        else:
                            print("Vous ne pouvez pas retourner deux fois la même carte")
                    else:
                        print("Vous ne pouvez pas choisir une carte déjà gagnée.")
                else:
                    print("Merci de choisir une carte sur le plateau.")

            carteTmp2=self._plateau._paquet[indiceChoix2]
            carteTmp2.retourner()       
            print(self._plateau.strMemory())

            if carteTmp1.correspond(carteTmp2):
                print("Bonne paire.")
                ##On ajoute les cartes gagnées à la liste du joueur courrant
                joueurTmp._cartesGagnees.append(str(carteTmp1))
                ##On définit les cartes comme n'étant plus en jeu, elles ne passeront plus les vérifications pour le choix d'une carte
                carteTmp1._enJeu=False
                joueurTmp._cartesGagnees.append(str(carteTmp2))
                carteTmp2._enJeu=False
                self._plateau._nbPairesRestantes-=1
                joueurTmp._score+=1
                joueurTmp._nbCoups+=1
                ##J'ai choisi de laisser les cartes gagnées sur le plateau de jeu, face visible. Sinon il faudrait redimenssionner la grille d'affichage à chaque paire trouvée et les anciennes cartes se verraient déplacées, ce qui n'est pas le but du memory
            else:
                print("Mauvaise paire.")
                carteTmp1.retourner()
                carteTmp2.retourner()
                perdu = True
                joueurTmp._nbCoups+=1

        afficherGagnant(self._listeJoueurs)
        
class PlusMoins:
    def __init__(self, joueurs, nbPaires=16, typePaquet=1):
        self._listeJoueurs = joueurs
        random.shuffle(self._listeJoueurs)
        self._plateau = Plateau(nbPaires, typePaquet)
        ##La variable self._indice permet de savoir à quelle carte nous sommes dans le paquet
        self._indice = 0

    def __str__(self):
        print("Nombre de cartes : "+str(self._plateau._nbCartes)+", Nombre de cartes restantes : "+str(self._plateau._nbCartesRestantes))
        chaine = self._plateau.strCarte32(self._indice)+"\n"       
        for joueur in range (0, len(self._listeJoueurs)):
            chaine+=str(self._listeJoueurs[joueur])+"\n"          
        return chaine

    def play(self):
        numJoueur = 0
        perdu = False
        scoreCourrant = 0
        joueurTmp=self._listeJoueurs[numJoueur]
        
        while(self._plateau._nbCartesRestantes!=0):
            ##Si le précédent joueur a perdu alors on passe au joueur suivant
            ##Le modulo permet de boucler une fois tous les joueurs passés
            if perdu == True:
                numJoueur+=1
                numJoueur=numJoueur%(len(self._listeJoueurs))
                joueurTmp=self._listeJoueurs[numJoueur]
                scoreCourrant = 0
                perdu = False
                
            print(self)
            print("Au tour de "+str(joueurTmp._nom))

            choix=False
            while choix==False:
                valeurChoix=input("La valeur de la prochaine carte sera [+] ou [-] élevée ? : ")
                if valeurChoix in ["+", "-"]:
                    choix=True
                else:
                    print("Merci de répondre [+] ou [-].")
            
            carteTmp1=self._plateau._paquet[self._indice]
            print("On retourne la carte d'après.")
            self._indice+=1
            print(self)
            carteTmp2=self._plateau._paquet[self._indice]

            ##La fonction comparer renvoie True si la valeur de la carte 1 est plus grande que la valeur de la carte 2
            if (carteTmp1.comparer(carteTmp2) and valeurChoix=="-") or (not(carteTmp1.comparer(carteTmp2)) and valeurChoix=="+"):
                print("Bonne supposition.")
                scoreCourrant+=1
                carteTmp1.retourner()
                joueurTmp._cartesGagnees.append(str(carteTmp1))
                ##Le joueur augmente son score total uniquement si le score courrant est plus élevé que son score enregistré
                ##Le score courant est réinitialisé si le joueur perd
                if (joueurTmp._score<scoreCourrant):
                    joueurTmp._score=scoreCourrant
            else:
                print("Mauvaise supposition.")
                perdu = True
            
            joueurTmp._nbCoups+=1   
            self._plateau._nbCartesRestantes-=1
        
        afficherGagnant(self._listeJoueurs)        

def afficherGagnant(listeJoueurs):
    print("La partie est terminée ! Voici les scores : ")
    scoreTmp=0
    for joueur in range (0, len(listeJoueurs)):
        if scoreTmp <= listeJoueurs[joueur]._score:
            scoreTmp=listeJoueurs[joueur]._score
            gagnant=listeJoueurs[joueur]          
        print(str(listeJoueurs[joueur]))
    print(gagnant._nom+" gagne la partie !")
         
def main():
    nbJoueur = int(input("Veuillez renseigner le nombre de joueurs : "))
    listeJoueurs = []
    for i in range(0, nbJoueur):
        nomTmp = input("Veuillez renseigner le nom du joueur "+str(i+1)+" : ")
        joueurTmp = Joueur(nomTmp)
        listeJoueurs.append(joueurTmp)

    typeJeu = int(input("Veuillez choisir un type de jeu >> [0] Memory // [1] Plus / Moins : "))
    if typeJeu == 0:
        typePaquet = int(input("Veuillez choisir un type de paquet >> [0] Memory // [1] 32 Cartes : "))
        if typePaquet==0:
            nbPaires = int(input("Veuillez choisir un nompbre de paires : "))
        else:
            ##Si l'on prend le paquet de 32 cartes pour le memory alors on ne peut pas choisir le nombre de paires à trouver, il faudra trouver toutes les paires du paquet, soit 16 paires
            nbPaires=16
        jeu = Memory(listeJoueurs, nbPaires, typePaquet)
    else:
        jeu = PlusMoins(listeJoueurs)
    jeu.play()
    ##On laisse le temps aux joueurs de lire le tableau des scores
    time.sleep(5)
        
main()
