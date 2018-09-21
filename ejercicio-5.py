tendencias = {
    '04-08-2018': {'#ClasicoBSCvsEMC', '#BSC', '#EC'},
    '04-09-2018': {'#BSC', '#GolTV', '#GYE'},
    '04-11-2018': {'#MadridvsJuve', '#Madrid', '#Mark'},
    '04-12-2018': {'#Madrid', '#GYE', '#PresidenciaEC'},
    '04-13-2018': {'#SemiChampios', '#EC'},
}

def cuentaEtiquetas(tendencias, listaFechas):
    # Retorna un nuevo diccionario con la etiqueta como clave y como valor # de días que esta etiqueta fue tendencia
    dicresult = {}
    lstag = []
    for fecha in listaFechas:
        if fecha in tendencias.keys():
            for index, item in enumerate(tendencias[fecha]):
                lstag.append(item)
    for tag in lstag:
        dicresult[tag] = lstag.count(tag)
    return dicresult

def reportaTendencias(tendencias, listaFechas):
    print("========================= REPORTE DE TENDENCIAS SEGÚN LAS FECHAS SOLICITADAS =============================")
    dicresult = cuentaEtiquetas(tendencias, listaFechas)
    print("Las etiquetas que fueron tendencia en todas las fechas solicitadas son: \n")
    for key, value in dicresult.items():
        if value > 1:
            print(f"\t\t{key}")
    print("---"*30)
    print("Las etiquetas que fueron tendencia en al menos una de las fechas solicitadas son: \n")
    for key, value in dicresult.items():
        if value == 1:
            print(f"\t\t{key}")

d = cuentaEtiquetas(tendencias, ['04-08-2018', '04-09-2018'])
print(d)
reportaTendencias(tendencias, ['04-08-2018', '04-09-2018'])