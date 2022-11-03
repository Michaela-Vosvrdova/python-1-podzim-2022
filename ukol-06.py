with open('vykaz.txt', 'r', encoding='utf-8') as vstup:
    radky = vstup.readlines()

prvni_radek = radky[0]
prevod_znamek = {ord('1'): 'A', ord('2'): 'B', ord('3'): 'C', ord('4'): 'D', ord('5'): 'E'}
radky = [radek.replace('\n', '').translate(prevod_znamek) for radek in radky[1:]]

with open('novy_vykaz.txt', 'w', encoding='utf-8') as vystup:
    vystup.write(prvni_radek)
    for radek in radky:
        vystup.write(radek + '\n')
