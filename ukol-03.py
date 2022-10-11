zadane_cislo = input('Zadej telefonní číslo příjemce: ')

def over_delku(cislo):
    predvolba = str('+420')
    if ((predvolba in cislo) and (len(cislo) == 13)) or (len(cislo) == 9):
        return True
    return False

def spocitej_cenu(text):
    if len(text) <= 180:
        return 3
    radky = ((len(text) // 180) + 1) 
    return radky * 3

if over_delku(zadane_cislo):
    zadany_text = input('Zadej zprávu: ')
    cena_zpravy = spocitej_cenu(zadany_text)
    print(f'Cena zprávy je {cena_zpravy} Kč.')
else:
    print('Zadej číslo ve správném formátu! Číslo musí být devítimístné nebo třináctimistné s českou předvolbou +420.')
