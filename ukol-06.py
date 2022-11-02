with open('muj_vykaz.txt', 'r', encoding='utf-8') as soubor:
    radky = soubor.readlines()

new_dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E'}
radky = [radek.replace('\t', ' ').replace('\n', '').replace(new_dict.keys(), new_dict.values()) for radek in radky]
print(radky)
