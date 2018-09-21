horast = float(input("Horas de trabajo: \n"))
tarifash = float(input("Tarifa por hora: \n"))
descuento = float(input("Descuentos: \n"))

if horast <= 40:
    pago = horast*tarifash - descuento
else:
    pago = horast*tarifash + ((horast*tarifash)*50)/100 - descuento
print(f'el pago es: {pago}\n')