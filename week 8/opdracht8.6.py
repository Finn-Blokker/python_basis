def main():
    from adressboek import Adressenboek
    while True:
        keuze = input("1 om een nieuw persoon toe te voegen \n" #voornaam, achternaam, adres 
                      "2 om alle contacten te printen \n"
                      "3 om het programma af te sluiten \n")
        match keuze:
            case "1":
                Fnaam = input("Voornaam: ")
                Lnaam = input("Achternaam: ")
                Adress = input("adress: ")
                Adressenboek(fnaam=Fnaam, lnaam=Lnaam, adress=Adress)

            case "2":
                try:
                    persoon1 = Adressenboek(Fnaam, Lnaam, Adress)
                    persoon1.klantenlijst()
                except UnboundLocalError:
                    print("voer eerst een persoon toe")


            case "3":
                print("Programma sluit af")
                exit()
            case _:
                print("voer 1, 2 of 3 in")


if __name__ == "__main__":
    main()