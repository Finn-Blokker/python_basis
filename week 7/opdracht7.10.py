run = True
while run == True:
    try:
        getal = int(input("getal: "))
        if 1 <= getal and getal <= 10:
            print(getal)
        else:
            print("voer een getal tussen de 1 en 10 in")
    except ValueError:
        print("Ongeldige invoer, voer een geheel getal in")
    except ZeroDivisionError:
        print("Je kunt niet delen door 0")

