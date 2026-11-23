class Klant:                                 #class
   def __init__(self, klant_id, naam, telnr): #method
      self.klant_id = klant_id               #object
      self.naam = naam
      self.telnr = telnr

   def check_telnr(self):
      telnr_string = str(self.telnr)
      if len(telnr_string) == 10:
         self.klantenlijst()
      else:
         print("dit is geen geldig telefoonnummer")

   def klantenlijst(self):
      lijst = [f"{self.klant_id}, {self.naam}, {self.telnr}"]
      def __str__():
         for i in lijst:
            print(lijst)
      __str__()

def maakklanten():
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

maakklanten()










