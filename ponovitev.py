#glavno mesto
__author__ = "Janko"
import random

prestolnice = {
    "Nizozemska": "Amsterdam",
    "Slovenija": "Ljubljana",
    "Srbija": "Beograd",
    "Nemcija": "Berlin",
    "Svica": "Bern",
    "Francija": "Pariz",
}

def prestolnica(drzava):
    if drzava in prestolnice:
        return prestolnice[drzava]
    else:
        return False

def preveriPrestolnico(gl_mesto, drzava):
    if gl_mesto == prestolnica(drzava):
        return True
    else:
        return False

random = random.sample(prestolnice, 1)[0]
print random

tocke = 0

while True:
    drzava = random.sample(prestolnice, 1)[0]
    mesto = raw_input("vnesi glavno mesto drzave ali prekini s stop" + drzava + ": ")

    if mesto == "stop":
        break

    uganil = preveriPrestolnico(mesto, drzava)

    if uganil:
        tocke += 1
    else:
        tocke -= 1
print "Bravo uganil si %d krat" % tocke