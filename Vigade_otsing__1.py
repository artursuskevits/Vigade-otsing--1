from math import *

print("Ruudu karakteristikud")
a=input('Sisesta ruudu külje pikkus => ')
S=float(a)**2
print("Ruudu pindala", S)
P=4*float(a)
print("Ruudu ümbermõõt " , P)
di=float(a)*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=input("Sisesta ristküliku 1. külje pikkus => ")
c=input("Sisesta ristküliku 2. külje pikkus => ")
S=float(b)*float(c)
print("Ristküliku pindala" , S)
P=2*(float(b)+float(c))
print("Ristküliku ümbermõõt", P)
di=sqrt(float(b)**2+float(c)**2)
print("Ristküliku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus =>'))
d=2*r
print("Ringi läbimõõt", (d))
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2))
