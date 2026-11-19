def main():
    leeftijd = int(input("leeftijd: "))

    if leeftijd < 13:
        print("kind")
    elif 13 < leeftijd <= 17 :
        print("tiener")
    else:
        print("volwassene")

if __name__ == '__main__':
   main()