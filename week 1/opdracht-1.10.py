def main():
    prijs = 10
    aantal = 5
    btw_percentage = 21

    total_excl = prijs * aantal
    total_incl = prijs * aantal * (btw_percentage / 100 + 1)

    print(f"De prijs exclusief btw is €{total_excl}")
    print(f"De prijs inclusief btw is €{total_incl}")

if __name__ == '__main__':
   main()

