##Instructions de base

##Calculer la somme des n premiers nombres
def calculSommeIter(n):
    if(n>=0):
        somme=0
        for i in range(0, n+1):
            somme+=i
        return somme
    else:
        return None
	
print(calculSommeIter(10)==10+9+8+7+6+5+4+3+2+1)
print(calculSommeIter(0)==0)
print(calculSommeIter(-10)==None)

def calculSommeRecu(n):
    if(n>=0):
        if(n==0):
            somme=0
        else:
            somme=n+calculSommeRecu(n-1)
        return somme
    else:
        return None
        
print(calculSommeRecu(10)==10+9+8+7+6+5+4+3+2+1)
print(calculSommeRecu(0)==0)
print(calculSommeRecu(-10)==None)

##Calculer la somme des nombres pairs inférieurs ou égaux à N
def calculSommePairsIter(n):
    if(n>=0):
        somme=0
        for i in range(2, n+1, 2):
            somme+=i
        return somme
    else:
        return None

print(calculSommePairsIter(10)==10+8+6+4+2)
print(calculSommePairsIter(0)==0)
print(calculSommePairsIter(-10)==None)

def calculSommePairsRecu(n):
    if(n>=0):
        if(n==0):
            somme=0
        elif(n%2==0):
            somme=n+calculSommePairsRecu(n-1)
        else:
            somme=calculSommePairsRecu(n-1)
        return somme
    else:
        return None

print(calculSommePairsRecu(10)==10+8+6+4+2)
print(calculSommePairsRecu(0)==0)
print(calculSommePairsRecu(-10)==None)

##Algorithmique itérative mathématiques

##Déterminer le plus grand n tel que la somme des n premiers nombres est inférieure à 15000
def somme15000():
    somme=0
    n=0
    while((somme+n)<15000):
        somme+=n
        n+=1
    return n-1
    
##Faire une fonction qui calcule la puissance.
def puissance(n, p):
    if(p>=0):
        puissance=1
        for i in range(1, p+1):
            puissance=puissance*n
        return puissance
    else :
        return None

print(puissance(2, 2)==4)
print(puissance(3, 3)==27)
print(puissance(3, 0)==1)
print(puissance(4, -5)==None)

##Passer d'un nombre en base 10 à base 2 et inversement.
def deciToBin(n):
    return bin(n).replace("0b","") 

print(deciToBin(4)==str(100))
print(deciToBin(5)==str(101))
print(deciToBin(4)==str(101))

def binToDeci(n):
    decimal, i= 0, 0
    while(n != 0): 
        dec = n % 10
        decimal = decimal + dec * pow(2, i) 
        n = n//10
        i += 1
    return decimal

print(binToDeci(100)==4)
print(binToDeci(101)==5)
print(binToDeci(100)==5)

##Suite de Fibonacci
def Fibonacci(n): 
    if n<0: 
        return None
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
    
Fibonacci(10)

##Triangle de pascal
def trianglePascal(n):
    T = [[0] * (n+1) for p in range(n+1)]
    for n in range(n+1):
        if n == 0:
            T[n][0] = 1
        else:
            for k in range(n+1):
                if k == 0:
                    T[n][0] = 1
                else:
                    T[n][k] = T[n-1][k-1] + T[n-1][k]
    return T
    
print(trianglePascal(9))

##Tuple
personne=("Bernard", 40)

def getNom(individu):
    (nom, age)=individu
    ##(nom, _)=individu >> variable anonyme _
    ##nom=individu[0]
    return nom

print(getNom(personne)=="Bernard")