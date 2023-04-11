print('\nSveiki atvykę į "Kryžiukų - Nuliukų" žaidimą!\n'
      'Šį žaidimą pradeda X žaidėjas, todėl nuspręskite, kas bus pirmasis.\n')


def spausdinimas(lenta):
    print(" ___________ ")
    print("|" + lenta[0] + "|" + lenta[1] + "|" + lenta[2] + "|")
    print("|___|___|___|")
    print("|" + lenta[3] + "|" + lenta[4] + "|" + lenta[5] + "|")
    print("|___|___|___|")
    print("|" + lenta[6] + "|" + lenta[7] + "|" + lenta[8] + "|")
    print("|___|___|___|")


def laimetojo_tikrinimas(lenta, zaidejas):
    if (lenta[0] == lenta[1] == lenta[2] == zaidejas) or \
       (lenta[3] == lenta[4] == lenta[5] == zaidejas) or \
       (lenta[6] == lenta[7] == lenta[8] == zaidejas) or \
       (lenta[0] == lenta[3] == lenta[6] == zaidejas) or \
       (lenta[1] == lenta[4] == lenta[7] == zaidejas) or \
       (lenta[2] == lenta[5] == lenta[8] == zaidejas) or \
       (lenta[0] == lenta[4] == lenta[8] == zaidejas) or \
       (lenta[2] == lenta[4] == lenta[6] == zaidejas):
        return True
    else:
        return False


def lygiuju_tikrinimas(lenta):
    for skaiciai_lentoje in range(9):
        if lenta[skaiciai_lentoje] in [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]:
            return False
    return True


def zaidimas():
    lenta = [" 1 ", " 2 ", " 3 ",
             " 4 ", " 5 ", " 6 ",
             " 7 ", " 8 ", " 9 "]
    zaidejas = " X "
    zaidimo_pabaiga = False

    while not zaidimo_pabaiga:
        spausdinimas(lenta)
        try:
            pozicija = int(input(f"Žaidėjau,{zaidejas}, įvesk savo ėjimo poziciją nuo 1 iki 9: "))
        except ValueError:
            print("Netinkama reikšmė. Bandyk dar kartą.")
            continue

        try:
            if lenta[pozicija - 1] in [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]:
                lenta[pozicija - 1] = zaidejas
            else:
                print("Ši pozicija jau užimta. Bandyk dar kartą.")
                continue
        except IndexError:
            print("Nėra tokios pozicijos. Bandyk dar kartą.")
            continue

        if laimetojo_tikrinimas(lenta, zaidejas):
            spausdinimas(lenta)
            print(f"Sveikiname, žaidejas{zaidejas}laimėjo žaidimą!!!")
            zaidimo_pabaiga = True
        elif lygiuju_tikrinimas(lenta):
            spausdinimas(lenta)
            print("Žaidimas baigtas lygiosiomis.")
            zaidimo_pabaiga = True
        else:
            if zaidejas == " X ":
                zaidejas = " O "
            else:
                zaidejas = " X "


zaidimas()
