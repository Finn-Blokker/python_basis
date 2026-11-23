while True:
    try:
        getal1 = int(input("getal 1: "))
        getal2 = int(input("getal 2: "))
        print(getal1 / getal2)
    except ValueError:
        print("Voer een geheel getal in")
    except ZeroDivisionError:
        print("Je kunt niet delen door 0")