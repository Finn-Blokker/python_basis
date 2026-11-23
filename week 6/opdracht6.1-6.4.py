class Persoon:
   def __init__(self, naam, leeftijd): #method
      self.naam = naam                 #object
      self.leeftijd = leeftijd         #object

   def begroet(self):
      print(f"Hoi ik ben {self.naam}!")

Persoon1 = Persoon("Finn", 19)
Persoon2 = Persoon("Daniel", 21)
Persoon3 = Persoon("Geert", 44)
Persoon1.begroet()
Persoon2.begroet()
Persoon3.begroet()