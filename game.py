secret = int(4)
guess = input("Pogodi sretan broj:")

if guess == secret:
    print("Cestitamo, osvojili ste dnevnu nagradu")
else:
    print("Više sreće drugi put, sretni broj bio je:" + str(secret))