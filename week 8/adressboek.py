class Adressenboek:
    def __init__(self, fnaam, lnaam, adress):  # method #maakt een nieuw adress aan
        self.fnaam = fnaam  # object
        self.lnaam = lnaam
        self.adress = adress

    def klantenlijst(self):
        lijst = []
        lijst.append(str(self.fnaam))
        lijst.append(str(self.lnaam))
        lijst.append(str(self.adress))

        def __str__():
            print(f"naam: {lijst[0]}\nachternaam: {lijst[1]}\nadress: {lijst[2]}")
        __str__()

