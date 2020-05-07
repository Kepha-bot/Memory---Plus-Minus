##print("coucou")
##
##print("coucou1")
##print("coucou2")
##
##nom="toto"
##note2=45
##print( "bonjour "+ nom+ ", ta moyenne est de "+ \
##str(note2))

def calculSommeIter(n):
    if n>=0:
        som=0
        ##boucle sur [1,n]
        for i in range(1,n+1):
            som += i
        return som
    ##else : pas de return -> donc return None implicite

##print(calculSommeIter(10)==10+9+8+7+6+5+4+3+2+1)
##print(calculSommeIter(0)==0)
##print(calculSommeIter(-10)==None)

def calculSommeRec0(n):
    if n>=0:
        if (n==0):
            som=0
        else:
            som=n+calculSommeRec0(n-1)
        return som

##print(calculSommeRec0(10)==10+9+8+7+6+5+4+3+2+1)
##print(calculSommeRec0(0)==0)
##print(calculSommeRec0(-10)==None)

def calculSommeRec(n):
    def aux(n): ## les conditions d'erreur ont été écartées
        if (n==0):
            som=0
        else:
            som=n+aux(n-1)
        return som

    if n>=0:
        return aux(n)

##print(calculSommeRec(10)==10+9+8+7+6+5+4+3+2+1)
##print(calculSommeRec(0)==0)
##print(calculSommeRec(-10)==None)

def calculSommePairs(n):
    if n>=0:
        som=0
        for i in range(2,n+1,2): ##première façon de faire...
            som+=i
        return som

##print(calculSommePairs(10)==10+8+6+4+2)
##print(calculSommePairs(11)==10+8+6+4+2)
##print(calculSommePairs(0)==0)
##print(calculSommePairs(-10)==None)

## variantes calculSommePairs, y compris en récursif
def calculSommePairs2(n):
    if n>=0:
        som=0
        for i in range(n+1): ##première façon de faire...
            if (i%2==0):
                som+=i
        return som

##print(calculSommePairs2(10)==10+8+6+4+2)
##print(calculSommePairs2(11)==10+8+6+4+2)
##print(calculSommePairs2(0)==0)
##print(calculSommePairs2(-10)==None)

def calculSommePairs3(n):
    def aux(n):
        som=0
        if n!=0:
            if (n%2==0):
                som+= n
            som+= aux(n-1)
        return som
    
    if n>=0:
        return aux(n)

##print(calculSommePairs3(10)==10+8+6+4+2)
##print(calculSommePairs3(11)==10+8+6+4+2)
##print(calculSommePairs3(0)==0)
##print(calculSommePairs3(-10)==None)

def calculSommePairs4(n):
    def aux(n): ## ici on sait que n est pair
        som=0
        if n!=0:
            som+= n+aux(n-2)
        return som
    
    ### exploiter la propriété des nombres pairs (un sur deux)
    if n>=0:
        if (n%2==1):
            n-=1
        return aux(n)

##print(calculSommePairs4(10)==10+8+6+4+2)
##print(calculSommePairs4(11)==10+8+6+4+2)
##print(calculSommePairs4(0)==0)
##print(calculSommePairs4(-10)==None)

## fonction puissance (itératif et récursif)
def puissance(n, p):
    if (p>=0):
        rep=1
        for i in range(p):
            rep*=n
        return rep
    ##else traiter le cas des puissances négatives    

##print(puissance(0,0)==1)
##print(puissance(0,1)==0)
##print(puissance(5,8)==5**8)
##print(puissance(5,0)==1)
##print(puissance(5,1)==5)
##print(puissance(-10,10)==(-10)**10)
##print(puissance(-10,9)==(-10)**9)
##print(puissance(10,-10)==None)

def puissance0(n, p): ## return n**p
    if (p>=0):
        rep=1
        if (p>0):
            rep = n * puissance0(n, p-1) # 5**5 == 5 x (5**4)
        return rep
## rep *= n     ->    rep = rep * n
##print(puissance0(0,0)==1)
##print(puissance0(0,1)==0)
##print(puissance0(5,8)==5**8)
##print(puissance0(5,0)==1)
##print(puissance0(5,1)==5)
##print(puissance0(-10,10)==(-10)**10)
##print(puissance0(-10,9)==(-10)**9)
##print(puissance0(10,-10)==None)

## fonction de passage d'une base 10 à base 2 et inversement.
def de10En2(n):
    if n>=0:
        rep=""
        if n==0:
            rep="0"
        while n>0:
            reste = str(n%2)
            rep = reste + rep
            n = int(n/2)
        return rep

##print(de10En2(0)=="0")
##print(de10En2(1)=="1")
##print(de10En2(-256)==None)
##print(de10En2(256)=="100000000")
##print(de10En2(23)=="10111")

def de2En10(chaineBinaire):
    som=0
    for car in chaineBinaire:
        som = som*2 + int(car)  ## 1254 = 1000+ 200 + 50 + 4
    return som

##print(de2En10("0")==0)
##print(de2En10("1")==1)
##print(de2En10("100000000")==256)
##print(de2En10("10111")==23) # (((1*2 + 0)*2 + 1)*2 + 1)*2 + 1)

def de2En10Bis(chaineBinaire):
    som=0
    puissance=1
    taille=len(chaineBinaire)
    for i  in range(taille-1, -1, -1):
        car = chaineBinaire[i]
        som += puissance*int(car)
        puissance *= 2
    return som

##print(de2En10Bis("0")==0)
##print(de2En10Bis("1")==1)
##print(de2En10Bis("100000000")==256)
##print(de2En10Bis("10111")==23) # (((1*2 + 0)*2 + 1)*2 + 1)*2 + 1)
    
## Si vous êtes à l'aise avec l'algo et Python, vous pouvez attaquer
## directement Fibonacci et le triangle de Pascal, sinon les autres questions
## sur les tuples et les listes

### TUPLES avec deux éléments -> COUPLES
personne1 = ("Bernard", 60)
personne2 = ("Céline", 40)
personne3 = ("Kévin", 20)

##Créer une méthode qui permet de retourner le nom d'un individu
##getNom(individu)
def getNom1(individu):
    (nom, age) = individu
    return nom

##print(getNom1(personne1)=="Bernard")
##print(getNom1(personne2)=="Céline")
##print(getNom1(personne3)=="Kévin")

def getNom0(individu):
    (nom,_) = individu  #variable anonyme = caractère souligné (touche 8)
    return nom

##print(getNom0(personne1)=="Bernard")
##print(getNom0(personne2)=="Céline")
##print(getNom0(personne3)=="Kévin")

def getNom(individu):
    return individu[0]

##print(getNom(personne1)=="Bernard")
##print(getNom(personne2)=="Céline")
##print(getNom(personne3)=="Kévin")

##Créer une méthode qui permet de retourner l'age d'un individu
def getAge(individu):
    return individu[1]

##print(getAge(personne1)==60)
##print(getAge(personne2)==40)
##print(getAge(personne3)==20)

##Créer une méthode qui permet d'afficher un individu ex : Bernard, 60 ans.
def afficheIndividu(individu) :
    print(getNom(individu)+",",getAge(individu),"ans")

##afficheIndividu(personne1)
##afficheIndividu(personne2)
##afficheIndividu(personne3)

##Créer une méthode qui permet de comparer deux individus selon
##l'âge puis le nom pour indiquer si un individu est «plus petit» qu'un autre.
def inferieur(p1, p2):
    return getAge(p1)<getAge(p2) or \
           (getAge(p1)==getAge(p2) and getNom(p1)<getNom(p2))

##personne4=("Michel",60)
##print(not inferieur(personne1,personne1))
##print(not inferieur(personne1,personne2))
##print(inferieur(personne2,personne1))
##print(not inferieur(personne4,personne1))
##print(inferieur(personne1,personne4))

LISTE_INDIVIDUS=[("Bernard", 60),("Céline", 40),("Jade", 30),\
                 ("Olivia", 15),("Kevin", 20)]
LISTE_INDIVIDU_SEUL=[("Kevin", 20)]
LISTE_VIDE=[]

##Afficher une liste
def afficherListe(liste):
    for individu in liste:
        afficheIndividu(individu)

##afficherListe(LISTE_INDIVIDUS)
##afficherListe(LISTE_INDIVIDU_SEUL)
##afficherListe(LISTE_VIDE)

##Inverser une liste  (extend    liste.insert(1,"toto"))
def inverse(liste):
    rep=[]
    taille= len(liste)
    for i in range(taille-1, -1, -1):
        rep.append(liste[i])
    return rep        

##print(inverse(LISTE_VIDE)==[])
##print(inverse(LISTE_INDIVIDU_SEUL)==LISTE_INDIVIDU_SEUL)
##print(inverse(LISTE_INDIVIDUS)==[("Kevin", 20),("Olivia", 15),("Jade", 30),\
##                                ("Céline", 40),("Bernard", 60)])

##Inverser une liste  (extend    liste.insert(1,"toto"))
def inverse0(liste):
    rep=[]
    for element in liste:
        rep.insert(0,element)
    return rep        

##print(inverse0(LISTE_VIDE)==[])
##print(inverse0(LISTE_INDIVIDU_SEUL)==LISTE_INDIVIDU_SEUL)
##print(inverse0(LISTE_INDIVIDUS)==[("Kevin", 20),("Olivia", 15),("Jade", 30),\
##                                ("Céline", 40),("Bernard", 60)])


##Vérifier si un nom de personne apparaît au moins une fois dans la liste
##(bonus) Supprimer les personnes qui ont le même âge
##(bonus Trier une liste avec une ou plusieurs méthodes de tri




dico0 = {"Bernard":60, "Kevin":30, "Olivia":15}
dico0["Jade"]=30
dico0["Celine"]=40
dico0["Bernard"]=40

##print(dico0)
##print("les clés sans le dire, l'ordre n'est pas conservé")
##for elem in dico0:
##    print(elem)

##print("\nles items en brut---------")
##for (a,b) in dico0.items():
##    print((a,"->",b)
##print("\nles listes d'individus à partir d'items()---------")
##showList(dico0.items())
##print("\ncles avec keys--------")
##lesCles0=dico0.keys() ##structure particulière
##print(lesCles0)
##lesCles1=list(dico0.keys()) ##la structure est transformée en liste
##print(lesCles1)

##for cle in dico0.keys(): ## mais la structure peut être parcourue en l'état.
##    print(cle)
##print("\nvaleurs---------")
##for valeur in dico0.values():
##    print(valeur)

##Écrire une fonction qui retourne si deux noms ont le même âge dans le dictionnaire    
##Écrire une procédure qui affiche ceux qui ont le même âge, deux à deux.

##Écrire une fonction qui retourne le dictionnaire inverse : age -> personnes

##Copier-coller un texte quelconque sur le net et retourner un
##dictionnaire qui retourne la fréquence de chaque mot.
texte1 = "Dans le brouillard va le paysan cagneux et le boeuf\
          Dans le brouillard vont deux silhouettes grises";
