baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

predan = input("Zadejte kód balíku: ")

if baliky[predan]:
    print("Balík byl předán kurýrovi.")
else:
    print("Balík zatím nebyl předán kurýrovi.")