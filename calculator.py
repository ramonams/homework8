a = float(input("unesi broj a:"))
b = float(input("unesi broj b:"))


operation = input("Unesi matematicku operaciju:")

if operation == "+":
    print("rezultat je:", a + b)
elif operation == "-":
    print("rezultat je:" + " " + str(a - b))
elif operation == "*":
    print("rezultat je:" + " " + str(a * b))
elif operation == "/":
    print("rezultat je:" + " " + str(a / b))
else:
    print("netočna operacija")
