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

def Maximum(n):
    # We are looking for the value between 0 and n for which
    # Syracuse2(n) is the greatest.
    i = 1
    candidat = i
    temps_vol = 1
    while (i <= n):
        # Check if new flight length is greater than previous one !
        if (Syracuse2(i) > temps_vol):
            temps_vol = Syracuse2(i)
            candidat = i
        i = i + 1
    
    return candidat

n=10000000000
print "Syracuse(" + str(n) + ") = " + str(Syracuse(n)) + " avec un temps de vol de " + str(Syracuse2(n))

N=5000
print "Temps de vol le plus haut entre 1 et N = " + str(N) + " est pour n = " + str(Maximum(N))
print "Il vaut " + str(Syracuse2(Maximum(N)))
