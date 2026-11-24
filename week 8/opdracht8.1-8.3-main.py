from persoon import Persoon     #naam en leeftijd
from klant import Klant         #id, naam en telnr

persoon1 = Persoon("Finn", 19)    #object
print(persoon1.naam)


klant1 = Klant(1, "Finn", 612345678)
print(f"klant_id:\t {klant1.klant_id} \nnaam:\t\t {klant1.naam} \ntelnr:\t\t {klant1.telnr}")


