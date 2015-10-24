class Kontakt(): #ustvarimo razred kontakt in mu najprej dolocimo lastnosti
    ime = ""
    priimek = ""
    naslov = ""
    email = ""
    phone = 123456789

    def __init__(self, ime, priimek, naslov, email, phone): #vse lastnosti inicializiramo - dolocimo jim neko osnovno vrednost
        self.ime = ime
        self.priimek = priimek
        self.naslov = naslov
        self.email = email
        self.phone = phone

    def izpisi(self): #metoda za izpis kontakta
        print "%s %s, %s, %s, %s" % (self.ime, self.priimek, self.naslov, self.email, self.phone)

    def izpisi_ime(self, ime, priimek): #metoda za izpis imena in priimka kontakta - naloga nikjer ne zahteva uporabe?
        self.ime = ime
        self.priimek = priimek

        print "%s %s" % (self.ime, self.priimek)

odgovor = "da" #pogoj za zanko
kontakti = [] #seznam kontaktov
while odgovor == "da":
    kontakt = Kontakt("","","","","") #lastnostim objekta pri kreiranju nastavimo prazen string, ker nam drugace tezi prevajalnik
    kontakt.ime = raw_input("vnesi ime osebe: ")
    kontakt.priimek = raw_input("vnesi priimek osebe: ")
    kontakt.naslov = raw_input("vnesi naslov osebe: ")
    kontakt.email = raw_input("vnesi email osebe: ")
    kontakt.phone = raw_input("vnesi telefonsko osebe: ")

    kontakti.append(kontakt) #kontakt dodamo na seznam

    odgovor = raw_input("zelis vnesti novo osebo? [da/ne] ") #preverimo ali gremo v nov krog zanke ali ne

for kontakt in kontakti: #izpis vseh kontaktov
    kontakt.izpisi()