class Persoon:
   def __init__(self, naam, leeftijd): #method
      self.naam = naam                 #object
      self.leeftijd = leeftijd         #object

   def begroet(self):
      print(f"Hoi ik ben {self.naam}!")
