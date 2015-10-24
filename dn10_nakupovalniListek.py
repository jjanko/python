# -*- coding: utf-8 -*-

nakupovalni_listek = [] #pripravimo si spremenljivko za nakupovalni listek

odgovor = raw_input("ali zelis vnesti izdelek? ") #uporabnika vprašamo ali želi vnesti izdelek

while odgovor == "da": #v zanko vstopimo, če želi vnesti izdelek
    izbira = raw_input("vnesi izdelek: ") #uporabnika pozovemo, da vnese izdelek
    nakupovalni_listek.append(izbira) #izbrani izdelek dodamo na seznam
    odgovor = raw_input("ali zelis vnesti izdelek? ") #uporabnika ponovno pozovemo, če želi vnesti izdelek

print(nakupovalni_listek) #nakupovalni izdelek po izstopu iz zanke izpišemo

#vsak izdelek izpišemo v svoji vrstici
i = 1
print "nakupovalni listek:"
for izdelek in nakupovalni_listek:
    print str(i) + ". " + izdelek + ","
    i += 1