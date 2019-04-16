#!/usr/bin/python
from JatekosLovese import JatekosLovese

f = open("lovesek.txt","r")
sorok = [ sor.rstrip() for sor in f.readlines() ]

# split: szetvalasztas ; szeparator alapjan
cel = sorok.pop(0).split(';')
# replace fuggveny: tizedes vesszo pontra
celx = float(cel[0].replace(',','.'))
cely = float(cel[1].replace(',','.'))

lovesek = []

for sor in sorok:
    elemek = sor.split(';')
    nev = elemek[0]
    x = float(elemek[1].replace(',','.'))
    y = float(elemek[2].replace(',','.'))
    loves = JatekosLovese(nev, x, y)
    lovesek.append(loves)

print("\n5. feladat: jatekosok loveseinek szama")
jatekosok = [ jatekos.nev for jatekos in lovesek]
lovesszamok = { x: jatekosok.count(x) for x in jatekosok }
print(lovesszamok)

print("\n6. feladat: lovesek tavolsagai")
tavolsagok = { loves.loves: [loves.nev, loves.tavolsag(celx, cely)] for loves in lovesek }
print(tavolsagok)

print("\n7. feladat: legjobb loves")
print(min(tavolsagok.items(), key=lambda x: x[1][1]))

print("\n8. feladat: pontszamok")
pontszamok = { loves.loves: [loves.nev, loves.pontszam(celx, cely)] for loves in lovesek }
print(pontszamok)

print("\n9. feladat: 0 pontos lovesek")
nullasok = [ loves.pontszam(celx,cely) for loves in lovesek ].count(0)
print(nullasok)

print("\n10. feladat: jatekosok szama")
jatekosok = len(set(loves.nev for loves in lovesek))
print(jatekosok)

print("\n11. feladat: jatekosok loveseinek darabszama")

