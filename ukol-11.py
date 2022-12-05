import re

# Soubor si načti do proměnné tak, aby se celý jeho obsah nacházel jako jeden řetězec v proměnné.
with open("posta.html", encoding='utf-8') as vstup:
    radky = vstup.read()

# Nahraď znaky odřádkování (zapisuje se jako '\n') jednoduchou mezerou pomocí metody replace().
radky_s_mezerami = [radek.replace("\n"," ") for radek in radky]

# Nahraď po sobě jdoucích víc mezer jedinou mezerou: Sestav regulární výraz, který označuje jednu nebo více mezer. 
# Pak pomocí re.sub() nahraď takové sekvence jedinou mezerou.
regex_mezery = re.compile("\s{1,2}")
radky_s_jednou_mezerou = re.sub(regex_mezery, " ", radky_s_mezerami)

# Najdi v datech všechna česká a slovenská města a jejich PSČ, která se nacházejí v ukázkových adresách. 
# Mají format PSČ MĚSTO, kde PSČ se skládá ze tří číslic, mezery a dvou číslic, a MĚSTO se skládá z jednoho, 
# dvou nebo tří slov oddělených mezerou, za kterými může ještě následovat číslo pošty.

regex_psc_mesto = re.compile("\d{3} \d{2} (\w|[À-ž]| )* ?\d{0,3}")
psc_mesto = regex_psc_mesto.search(radky_s_jednou_mezerou)