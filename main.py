from math import *

def angle (a,b,c):
  k=(b**2+c**2-a**2)/(2*b*c)
  l=(b**2+a**2-c**2)/(2*a*b)
  m=(c**2+a**2-b**2)/(2*a*c)
  return [degrees(acos(k)), degrees(acos(l)), degrees(acos(m))]

print ("Exervice numéro 93")
print ("Résultat du calcul des angles")
print ("Angle = " + str(angle (5,4,3)) )