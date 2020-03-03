from fractions import *

def somme():
    S = 1
    for i in range (1,20):
        S = S + pow(Fraction(1,3),i)
        
    # Converts fraction to float
    # and returns the result
    return float(S);
    
print "Somme = " + str(somme())

def compte_espaces(phrase):
    nbre = 0
    for caractere in phrase:
        if caractere==" ":
            nbre=nbre+1
    
    return nbre
    
la_phrase = "Voici une phrase pour le programmeur Badie"
print "Il y a " + str(compte_espaces(la_phrase)) + " espaces dans la phrase - " + la_phrase + "-"

def Syracuse(n):
    resultat = n
    while (resultat!=1):
        if (resultat % 2) == 0:
            resultat = resultat // 2
        else:
            resultat = (3 * resultat) + 1
            
    return resultat
    
def Syracuse2(n):
    resultat = n
    compteur = 0
    while (resultat!=1):
        compteur = compteur + 1
        if (resultat % 2) == 0:
            resultat = resultat // 2
        else:
            resultat = (3 * resultat) + 1
            
    return compteur

n=10000000000
print "Syracuse(" + str(n) + ") = " + str(Syracuse(n)) + " avec un temps de vol de " + str(Syracuse2(n))