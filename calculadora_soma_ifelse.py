print("\nSOMA!\n")
y= float(input("insira Numero: "))
x= float(input("insira Numero: "))
yx= y+x

print ("\nSoma {} + {} = {}\n".format( x, y, yx))

if yx > 10:
    b = yx
    b += 10
    print("Como eh mais que dez \ncolocarei mais 10, logo,\n\n{} + 10.0 = {} \n".format(yx, b))
elif yx == 10:
    print("Igual a Dez\n")
else:
    print("Menos que Dez\n")
