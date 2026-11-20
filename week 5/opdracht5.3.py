def main():
   namenlijst = []
   for i in range(5):
      i += 1
      naam = input(f"naam {i}: ")
      namenlijst.append(naam)
   print(namenlijst)


if __name__ == '__main__':
   main()