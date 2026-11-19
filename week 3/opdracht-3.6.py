def main():
    lid = input("bent U lid? (ja of nee) ")
    prijs = 10.00

    if lid == "nee":
        print(f"Totaal: {prijs}€")
    elif lid == "ja":
        print(f"{prijs}€\n - 10% ledenkorting \nTotaal: {prijs * 0.9}€")
    else:
        print("voer ja of nee in")
        main()

if __name__ == '__main__':
   main()