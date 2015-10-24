from random import randint
stevilka = randint(1,50)
st_poskusov = 1

while st_poskusov <= 10:
    poskus = raw_input("Vnesi stevilko: ")
    if poskus.isdigit() == False:
        print("Nisi vnesel stevila!!!")
        break

    if int(poskus) < stevilka:
        print("Vnesi vecje stevilo.")
        st_poskusov += 1
    elif int(poskus) > stevilka:
        print("Vnesi manjse stevilo.")
        st_poskusov += 1
    else:
        print("Bravo, zadel si stevilo.")
        break

if st_poskusov >= 10:
    print("pravilna stevilka je: " + str(stevilka))