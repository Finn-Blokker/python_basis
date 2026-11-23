while True:
    try:
        getal = input("getal 1: ")
        print(int(getal))
    except ValueError:
        print("Ongeldige invoer")
    except ZeroDivisionError:
        print("Je kunt niet delen door 0")

    print("het print 'ongeldige invoer' bij tekst en cijfers")