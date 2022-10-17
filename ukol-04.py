class Recept:
    def __init__(self, nazev, narocnost, url_adresa, vyzkouseno=False):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = vyzkouseno

    def __str__(self):
        if self.vyzkouseno:
            return f'Recept na {self.nazev}, náročnost {self.narocnost}, odkaz: {self.url_adresa}, vyzkoušené.'
        return f'Recept na {self.nazev}, náročnost {self.narocnost}, odkaz: {self.url_adresa}, zatím nevyzkoušené.'
    
    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota
    
    def zkusit(self):
        self.vyzkouseno = True

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
    
    def __str__(self):
        return f'Kucharka {self.nazev} od autor {self.autor}, {len(self.recepty)} receptu.'
    
    def pocet_receptu(self):
        return len(self.recepty)
    
    def pridej_recept(self, recept):
        self.recepty.append(recept)

moje_kucharka = Kucharka('Peceni', 'Andy')
pernik = Recept('Pernik', 2, 'url-adresa')
tiramisu = Recept('Tiramisu', 4, 'adresa')
muffiny = Recept('Muffiny', 1, 'web-link')
moje_kucharka.pridej_recept(pernik)
moje_kucharka.pridej_recept(tiramisu)
moje_kucharka.pridej_recept(muffiny)




