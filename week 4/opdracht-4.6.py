def main():
   i = 0
   while i < 20:
      i += 1
      if i % 3 == 0:
         continue
      else:
         print(i)

if __name__ == '__main__':
   main()