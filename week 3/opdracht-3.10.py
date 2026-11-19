def main():
    gewicht = float(input("gewicht in kg: "))
    lengte = float(input("lengte in meters: "))

    bmi = gewicht / (lengte ** 2)
    if bmi <= 18.5:
        print("ondergewicht")
    elif bmi >= 25:
        print("overgewicht")
    else:
        print("gezond gewicht")
if __name__ == '__main__':
   main()