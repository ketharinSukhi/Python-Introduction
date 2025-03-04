from calculator import square

def main():
   
   test_square()
   
def test_square():
    if square(2) !=4:
       print(" 2 sqared was not 4")
    if square(3) !=9:
       print(" 3 sqared was not 9")


if __name__ == "__main__":
   main()



       #if square(n) != n*n: # type: ignore
       #print("")