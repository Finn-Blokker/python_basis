from klantenlijst import Klant

def main():
   klant1 = Klant(1, "F1nn", 3811223344)
   klant2 = Klant(2, "F2nn", 3822334455)
   klant3 = Klant(3, "F3nn", 3833445566)
   klant4 = Klant(4, "F4nn", 384455677)
   klant5 = Klant(5, "F5nn", 3855667788)

   klant1.check_telnr()
   klant2.check_telnr()
   klant3.check_telnr()
   klant4.check_telnr()
   klant5.check_telnr()
   print("zo weet je zeker dat de main als eerste/enigste wordt uitgevoerd en dat er niet een andere functie eerder wordt aangeroepen")

if __name__ == "__main__":
    main()