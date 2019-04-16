#!/usr/bin/python

class JatekosLovese:
    lovesek = 0

    def __repr__(self):
        return ";".join([str(self.loves), self.nev, str(self.x), str(self.y)])

    def __init__(self, jatekosnev, xkoordinata, ykoordinata):
        JatekosLovese.lovesek = JatekosLovese.lovesek + 1
        self.loves = JatekosLovese.lovesek
        self.nev = jatekosnev
        self.x = xkoordinata
        self.y = ykoordinata

    def tavolsag(self, celx, cely):
        dx = celx - self.x
        dy = cely - self.y
        return ( dx ** 2 + dy ** 2 ) ** 0.5
    
    def pontszam(self, celx, cely):
        pont = round(10 - self.tavolsag(celx,cely),2)
        if pont < 0:
            return 0
        return pont 

# ferishot = JatekosLovese("feri", 20.01, 21.04)
# mari = JatekosLovese("mari", 21.88, 21.04)
# jani = JatekosLovese("jani", 21.73, 21.04)
# print(JatekosLovese.lovesek)
