from datetime import datetime

datum_vstup = input('Zadej datum: ')
datum = datetime.strptime("datum_vstup", "%d. %m. %Y")

otevreni_kina = datetime(2021, 7, 1)
uzavreni_kina = datetime(2021, 8, 31)
konec_drazsiho_obdobi = datetime(2021, 8, 10)

if (datum < otevreni_kina) & (datum > uzavreni_kina):
    print('Letní kino je v tuto dobu uzavřené.')

pocet_osob = input('Zadej počet osob: ')

if (datum >= otevreni_kina) & (datum < konec_drazsiho_obdobi):
    print(f'Částka k platbě je {pocet_osob * 250} Kč.')
else:
    print(f'Částka k platbě je {pocet_osob * 150} Kč.')