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