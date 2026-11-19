def main():
   for i in range(10):
      i += 1
      print(f"tafel van {i}")
      for j in range(10):
         j +=1
         print(F"{i} x {j} = {i * j}")
      print("\n")

if __name__ == '__main__':
   main()