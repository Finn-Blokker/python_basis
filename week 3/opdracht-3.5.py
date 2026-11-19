def main():
    jaartal = int(input("jaar: "))
    deelbaar4 = jaartal % 4       #deelbaar door 4 als het 0 is
    deelbaar100 = jaartal % 100   #deelbaar door 100 als het 0 is
    deelbaar400 = jaartal % 400   #deelbaar door 100 als het 0 is

    if deelbaar400 == 0:
        print("dit is een schrikkeljaar")
    elif deelbaar100 == 0:
        print("dit is geen schrikkeljaar")
    elif deelbaar4 != 0:
        print("geen schrikkeljaar")
    elif deelbaar4 == 0:
        print("dit is een schrikkeljaar")
if __name__ == '__main__':
   main()