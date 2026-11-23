while True:
    try:
        getal = int(input("getal 1: "))
        print(getal)
    except ValueError:
        print("Voer een geheel getal in")