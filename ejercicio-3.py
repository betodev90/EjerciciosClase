valor_pagar = float(input("El total de la cuenta es: \n"))

if valor_pagar < 50:
    print("Pago en efectivo")
else:
    if 50 <= valor_pagar <= 100:
        print("Pago con el celular( dinero electronico) ")
    else:
        if 100 <= valor_pagar <= 200:
            print("Pago con la tarjeta de débito")
        else:
            print("Pago con la tarjeta de crédito")
