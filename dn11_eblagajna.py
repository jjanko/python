seznam_izdelkov = {
    "mleko": 1.55,
    "jajca": 2.2,
    "kruh": 1.79,
    "jogurt": 0.29,
    "med": 5.99,
    "viki krema": 3.49
}

odgovor = ""
def eBlagajna(izdelek):
    if izdelek in seznam_izdelkov.keys():
        print "cena izdelka " + izdelek + " je: " + str(seznam_izdelkov[izdelek])
    else:
        print "izdelka ni na razpolago!"
    return

while odgovor != "izhod":
    odgovor = raw_input("vnesi izdelek ['izhod' za izstop iz zanke']: ")
    eBlagajna(odgovor)