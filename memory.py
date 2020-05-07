import math
import random

class Carte:
    def __init__(self, valeur, symbole):
        self._valeur = valeur
        self._symbole = symbole
        self._visible = False
        self._dos = "#####"
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

    def correspond(self, carte2):
        return (self._symbole==("T" or "P") and carte2._symbole==("T" or "P")) or self._symbole==("H" or "C") and carte2._symbole==("H" or "C")) and self._valeur==carte2._valeur 

class Plateau:
    def __init__(self, nbPaires):
        self._paquet = []
        self._nbPaires = nbPaires
        self._nbPairesRestantes = nbPaires
        
        if self._nbPaires>13 or self._nbPaires<0:
            self._nbPaires=10
        for i in range (0, self._nbPaires):
            carteTmp1=CarteMemory(i, chr(i+65))
            carteTmp2=CarteMemory(i, chr(i+65))
            self._paquet.append(carteTmp1)
            self._paquet.append(carteTmp2)
            
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

    def __str__(self):
        ligne = ""
        for carte in range (0, len(self._paquet)):
            if carte!=0 and carte%self._dimension == 0:
               ligne+='\n'
            ligne+="["+str(carte+1).zfill(2)+"]"+str(self._paquet[carte])+" "          
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
    def __init__(self, joueurs, nbPaires):
        self._listeJoueurs = joueurs
        random.shuffle(self._listeJoueurs)
        self._plateau = Plateau(nbPaires)

    def __str__(self):
        print("Nombre de paires : "+str(self._plateau._nbPaires)+", Nombre de paires restantes : "+str(self._plateau._nbPairesRestantes))
        chaine = str(self._plateau)+"\n"       
        for joueur in range (0, len(self._listeJoueurs)):
            chaine+=str(self._listeJoueurs[joueur])+"\n"          
        return chaine
    
    def play(self):
        nbCartes = len(self._plateau._paquet)
        numJoueur = -1
        perdu = True
        while(self._plateau._nbPairesRestantes!=0):
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
                if indiceChoix1>=0 and indiceChoix1<nbCartes:
                    if self._plateau._paquet[indiceChoix1]._enJeu==True:
                        choix=True
                    else:
                        print("Vous ne pouvez pas choisir une carte déjà gagnée.")
                else:
                    print("Merci de choisir une carte sur le plateau.")
            
            carteTmp1=self._plateau._paquet[indiceChoix1]
            carteTmp1.retourner()            
            print(self._plateau)

            choix=False
            while choix==False:
                indiceChoix2=int(input("Première carte à retourner : "))-1
                if indiceChoix2>=0 and indiceChoix2<nbCartes:
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
            print(self._plateau)

            if carteTmp1.correspond(carteTmp2):
                print("Bonne paire.")
                joueurTmp._cartesGagnees.append(str(carteTmp1))
                carteTmp1._enJeu=False
                joueurTmp._cartesGagnees.append(str(carteTmp2))
                carteTmp2._enJeu=False
                self._plateau._nbPairesRestantes-=1
                joueurTmp._score+=1
                joueurTmp._nbCoups+=1
            else:
                print("Mauvaise paire.")
                carteTmp1.retourner()
                carteTmp2.retourner()
                perdu = True
                joueurTmp._nbCoups+=1

        print("La partie est terminée ! Voici les scores : ")
        for joueur in range (0, len(self._listeJoueurs)):
            print(str(self._listeJoueurs[joueur]))

def main():
    j1 = Joueur("Paul")
    j2 = Joueur("François")
    j3 = Joueur("Carole")
    j4 = Joueur("Anais")
    
    nbPaires = int(input("Veuillez choisir un nompbre de paires : "))
    
    jeu = Memory([j1, j2, j3, j4], nbPaires)
    jeu.play()
        
main()
