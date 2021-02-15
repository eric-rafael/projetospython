y= float(input("insira y: "))
x= float(input("insira x: "))
yx= y+x
print ("soma {} + {} = {}".format( x, y, yx))

if yx > 10:
    b = yx
    b += 10
    print("\ncomo é mais que dez \ncolocarei mais 10, logo,\n{} + 10.0 = {} \n".format(yx, b))
elif yx == 10:
    print("igual a dez")
else:
    print("menos que dez")
