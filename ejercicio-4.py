"""
    La lista mostrada en el ejemplo contiene los URLs de diferentes sitios Web que han sido visitados.
    Los URLs normalmente se repiten y corresponden algunas veces a universidades de Ecuador y otros países.
    Note que los URLs no diferencian entre mayúsculas y minúsculas.

    lista = [
        "www.espol.edu.ec", “www.google.com”, “www.sri.gob.ec”, "www.fiec.espol.edu.ec", "www.uess.edu.ec",
        "www.FIEC.espol.edu.ec", "www.fict.espol.edu.ec", "www.fcnm.Espol.edu.ec", "www.ucsg.edu.ec",
        "www.Stanford.edu", "www.harvard.edu", "www.stanford.edu", "www.UCSG.edu.ec", ....
        "www.google.com.ec", "www.facebook.com", “www.opensource.org”, “www.educacionbc.edu.mx”
    ]

    Por ejemplo:
        www.espol.edu.ec y  www.ESPOL.edu.EC
    corresponden al mismo sitio.

    Escriba un programa en python que realice lo siguiente:

    a)  Muestre los nombres o siglas de las universidades que aparecen en la lista (sin repetir).
        Del el ejemplo mostrado, la salida sería:

        En la lista aparecen 6 universidades:
            1.) ESPOL
            2.) UESS
            3.) UCSG
            4.) STANFORD
            5.) HARVARD
            6.) EDUCACIONBC

    b) Muestre la cantidad y los nombres/siglas de universidades de Ecuador que aparecen en la lista.
       Del ejemplo mostrado, la salida sería:

       En la lista aparecen 3 universidades de Ecuador
            1.) ESPOL
            2.) UESS
            3.) UCSG

    c)  Dado un usuario y el nombre o sigla de la universidad, imprima el correo electrónico asignado.
        Por ejemplo:

        Ingrese el usuario: ricardobonilla
        Ingrese el nombre/sigla de la universidad: U CSG El correo electrónico del usuario es:
        ricardo.bonilla@ucsg.edu.ec
"""

lista = [
    "www.espol.edu.ec", "www.google.com", "www.sri.gob.ec", "www.fiec.espol.edu.ec", "www.uess.edu.ec",
    "www.FIEC.espol.edu.ec", "www.fict.espol.edu.ec", "www.fcnm.Espol.edu.ec", "www.ucsg.edu.ec",
    "www.Stanford.edu", "www.harvard.edu", "www.stanford.edu", "www.UCSG.edu.ec", "www.google.com.ec",
    "www.facebook.com", "www.opensource.org", "www.educacionbc.edu.mx", "www.elnoticiero.com.ec"
]


item_a = []
item_b = []
for item in lista:
    item = item.upper()
    l_site = item.split(".")
    if 'EDU' in item:
        index = l_site.index('EDU')  # get index where found 'EDU'
        name_u = l_site[index-1]     # assign element list
        if name_u not in item_a:
            item_a.append(name_u)

print("Respuesta literal a:")
print("En la lista aparecen %d universidades: " % len(item_a))
for i in range(len(item_a)):
    print("\t%d.) %s" % (i+1, item_a[i]))


for item in lista:
    item = item.upper()
    l_site = item.split(".")
    if 'EDU.EC' in item:
        index = l_site.index('EDU')  # get index where found 'EDU'
        name_u = l_site[index-1]     # assign element list
        if name_u not in item_b:
            item_b.append(name_u)

print("\nRespuesta literal b:")
print("En la lista aparecen %d de universidades en Ecuador: " % len(item_b))
for j in range(len(item_b)):
    print("\t%d.) %s" % (j+1, item_b[j]))

print("\nRespuesta literal c:")
usuario = input("Ingrese el usuario: ")
universidad = input("Ingrese el nombre/sigla de la universidad: ")
print("\nEl correo electrónico del usuario es: ", )
email = usuario+'@'+universidad+'.edu.ec'
print(email)
