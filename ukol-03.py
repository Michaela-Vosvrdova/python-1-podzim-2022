# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné 
# nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel 
# zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. 
# Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. 
# Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce
# určí její cenu, kterou vypíše uživateli.

zadane_cislo = input('Zadej telefonní číslo příjemce: ')

def over_delku(cislo):
    str(cislo)
    predvolba = str(+420)
    if ((predvolba in cislo) and (len(cislo) == 13)) or (len(cislo) == 9):
        return True
    return False

over_delku(zadane_cislo)

if over_delku:
    text = input('Zadej zprávu: ')
else:
    print('Zadej číslo ve správném formátu!')

def spocitej_cenu(text):
    if len(text) <= 180:
        return 3
    radky = ((len(text) // 180) + 1) 
    return radky * 3

cena_zpravy = spocitej_cenu(text)

print(f'Cena zprávy je {cena_zpravy} Kč.')