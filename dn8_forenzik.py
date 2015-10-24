# -*- coding: utf-8 -*-

besedilo = open("dna.txt", "r").read() #prebere besedilo datoteke

#pripravimo si spremenljivke, v katere kasneje zapišemo vrednosti
lasje = ""
obraz = ""
oci = ""
spol = ""
rasa = ""

#znani kriteriji
crna = "CCAGCAATCGC"
rjava = "GCCAGTGCCG"
korencek = "TTAGCTATCGC"

kvadraten = "GCCACGG"
okrogel = "ACCACAA"
ovalen = "AGGCCTCA"

modra = "TTGTGGTGGC"
zelena = "GGGAGGTGGC"
rjava = "AAGTAGTGAC"

moski = "TGCAGGAACTTC"
zenska = "TGAAGGACCTTC"

belec = "AAAACCTCA"
crnec = "CGACTACAG"
azijec = "CGCGGGCCG"

#določanje vrednosti za posamezen kriterij
#lasje
if besedilo.find(crna) != -1:
    lasje = "crna"
elif besedilo.find(rjava) != -1:
    lasje = "rjava"
else:
    lasje = "korencek"

#obraz
if besedilo.find(kvadraten) != -1:
    obraz = "kvadraten"
elif besedilo.find(okrogel) != -1:
    obraz = "okrogel"
else:
    obraz = "ovalen"

#oci
if besedilo.find(modra) != -1:
    oci = "modra"
elif besedilo.find(zelena) != -1:
    oci = "zelena"
else:
    oci = "rjava"

#spol
if besedilo.find(moski) != -1:
    spol = "moski"
else:
    spol = "zenska"

#rasa
if besedilo.find(belec) != -1:
    rasa = "belec"
elif besedilo.find(crnec) != -1:
    rasa = "crnec"
else:
    rasa = "azijec"

osumljenec = "" #prazna spremenljivka za osumljenca
if spol == "moski" and rasa == "belec" and lasje == "korencek" and oci == "rjava" and obraz == "okrogel":
    osumljenec = "Žiga"
elif spol == "moski" and rasa == "belec" and lasje == "crna" and oci == "modra" and obraz == "ovalen":
    osumljenec = "Matej"
else:
    osumljenec = "Miha"

print "Nas osumljenec je: " + osumljenec #kot rezultat programa izpišemo našega osumljenca 



