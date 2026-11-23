run = True
while run == True:
    try:
        getal = int(input("100 delen door: "))
        print(int(100 / getal))
        run = False
    except ValueError:
        print("Ongeldige invoer, voer een geheel getal in")
    except ZeroDivisionError:
        print("Je kunt niet delen door 0")
    finally:
        print("Klaar met rekenen")
