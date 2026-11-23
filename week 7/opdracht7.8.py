print("ongeldig getal wordt geprint, het is een string en geen int\n daarna komt er een error")
try:
    getal = int(input("Geef een getal: "))
except ValueError:
    print("Ongeldig getal")
print(getal)
