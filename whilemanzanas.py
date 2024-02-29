Cantidad = 4
descuento = 0

while Cantidad != 0:
    #pedir datos
    Cantidad = float(input("ingresa cantidad: "))
    if Cantidad == 0:
        break
    
    Precio = float(input("ingresa precio: "))

    if Cantidad == 18 :
        descuento = (Cantidad * Precio) *.15
        print(f"el descuento secreto es de {descuento}")
        
    elif Cantidad >= 10 :
        descuento = (Cantidad * Precio) *.10
        print(f"el descuento es de {descuento}")
    
    else:
        print("gracias por comprar")
    
    Totalapagar = (Cantidad * Precio) - descuento
    print(f"total a pagar {Totalapagar} " )
    
    #CONTROLF PARA BUSCAR Y CAMBIAR