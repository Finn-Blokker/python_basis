run = True
while run == True:
    try:
        getal = int(input("getal: "))
        print(getal)
        run = False
    except ValueError:
        print("Ongeldige invoer, voer een geheel getal in")
    except ZeroDivisionError:
        print("Je kunt niet delen door 0")
