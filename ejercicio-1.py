from datetime import date
print("Ingrese su fecha de nacimiento: \n")
anioNacimiento = int(input("Año de nacimiento: \n"))
mesNacimiento = int(input("Mes de nacimiento: \n"))
diaNacimiento = int(input("Día de nacimiento: \n"))
fecha_actual = date.today()  # aaaa-mm-dd
anioActual = fecha_actual.year
mesActual = fecha_actual.month
diaActual = fecha_actual.day

restaDia = diaActual - diaNacimiento
restaMes = mesActual - mesNacimiento
restaAnio = anioActual - anioNacimiento

if restaMes < 0:
    restaAnio -= 1
elif restaMes == 0:
    if restaDia > 0:
        restaAnio -= 1

if restaMes < 0:
    restaMes += 12

print(f"Los años vividos son: {restaAnio}")
print(f"Los meses vividos son: {restaMes}")
print(f"Los días vividos son: {restaDia}")



