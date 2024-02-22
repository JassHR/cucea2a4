Cantidad = float(input("ingresa cantidad: "))
Precio = float(input("ingresa precio: "))
Totalapagar = Cantidad * Precio
print(Totalapagar)
    
descuento = 0
if Cantidad >= 10 :
        descuento = (Cantidad * Precio) *.10
        print(f"el descuento es de {descuento}")
else :
    print("gracias por comprar")
    
Totalapagar = (Cantidad * Precio) - descuento
print(f"total a pagar {Totalapagar} " )
    