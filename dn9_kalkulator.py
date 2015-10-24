#od uporabnika zahtevamo vnos 2 števil in operacije
x = raw_input("vnesi stevilko1: ")
y = raw_input("vnesi stevilko2: ")
op = raw_input("vnesi operacijo (+, -, *, /, %: ")

#preverimo ali je vnesel številos
if x.isdigit() and y.isdigit():
    stevilka1 = int(x)
    stevilka2 = int(y)

    #izvedemo izbrano operacijo in izpišemo rezultat
    if(op == "+"):
        print("vrednost: " + str(stevilka1+stevilka2))
    elif(op == "-"):
        print("vrednost: " + str(stevilka1-stevilka2))
    elif(op == "*"):
        print("vrednost: " + str(stevilka1*stevilka2))
    elif(op == "/"):
        if(stevilka2 == 0):
            print("deljenje z 0!")
        else:
            print("vrednost: " + str(stevilka1/stevilka2))
    elif(op == "%"):
        print("vrednost: " + str(stevilka1%stevilka2))
    else:
        print("napacna operacija")

#èe uporabnik ne vnese števila
else:
    print("obvezno vnesi stevilko!!!")