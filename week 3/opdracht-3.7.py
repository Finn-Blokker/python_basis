def main():
    leeftijd = int(input("leeftijd: "))
    geldig_id = input("geldig id: (ja of nee) ")

    if leeftijd >= 18 and geldig_id == "ja":
        print("jij mag leeftijdsgebonden producten kopen")
    else:
        print("jij mag geen leeftijdsgebonden producten kopen")

if __name__ == '__main__':
   main()