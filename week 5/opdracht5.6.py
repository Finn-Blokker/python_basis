def main():
   highest = 0
   i = 0
   lijst = [32, 11111, 99, 12]
   for nummers in lijst:
      if lijst[i] > highest:
         highest = lijst[i]
      i += 1
   print(highest)
if __name__ == '__main__':
   main()