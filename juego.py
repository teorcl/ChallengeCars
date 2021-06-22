# Archivo principal

from random import randint, sample

#import jugador

dicc = {}

file = open("DDBB.txt", encoding="UTF-8")

#Extrae las características del archivo
for linea in file:
    index = linea.index(":")
    num = linea[:index]
    a = linea[index + 1:-1] # numero de veces ganadas
    b = a.split(",") #juagador
    dicc[int(num)] = {1: int(b[0]), 2: int(b[1]), 3: int(b[2])}

file.close()

while True:
    num_players = int(input("Ingrese # jugadores"))
    if num_players < 3:
        print('Debe ingresar como mínimo 3 jugadores')
    elif num_players > 20:
        print('Deben de ser menos de 20 jugadores')
    else:
        break
tamano_pista = 30

#Diccionario general del juego
game = {"jug":[],"num_players": num_players,"ganadores":{1:"",2:"",3:"","orden":1},"jugadas":dicc}

#Crear a cada jugador y le asigna un carril
#Jugador puede verse como una clase que herada de:
#Carril y Conductor
#Carril a su vez heredaría de pista


for i in range(num_players):
    num = str(i+1) #numero que identifica a cada jugador
    tama = len(num) #Largo del numero para usarse al dibujar la pista
    pista = " "+ num + " " * (tamano_pista - tama) #carril del jugador con su respectivo identificador
    game["jug"].append({"carril":{"pista":pista,"tama":tama,"num":num},"conductor":{"pos":2}})

y = [] #Arreglo para guardar los carriles
for k in game["jug"]:
    y.append(k["carril"]["pista"])

x = [] #Arreglo que guarda los carriles de forma vertical
for l in zip(*y):
    x.append(l)

# Se dibuja la pista
for i in range(len(x)):  # se itera para el largo de la pista
    for j in range(game["num_players"]):  # Se itera por la cantidad de jugadores
        print("|", end="")  # se dibuja un extremo de la pista

        # Con la condición se garantiza que se dibuje el identificador en una sola línea
        if x[i][j].isnumeric() and x[i - 1][j] == " ":
            num = game["jug"][j]["carril"]["num"]
            print("J" + num, end="")
            # De lo contrario se debe imprimir un tamaño lo suficientemente grande para incluir el identificador
        else:
            tama = game["jug"][j]["carril"]["tama"]
            print(" " * (tama + 1), end="")
    print("|")

######################
for j in range(len(game["jug"])):
    num = game["jug"][j]["carril"]["num"]
    index = game["jug"][j]["conductor"]["pos"]
    tama = game["jug"][j]["carril"]["tama"]
    pista = " " + num + " " * (tamano_pista - tama)
    game["jug"][j]["carril"]["pista"] = pista

y = []
for k in game["jug"]:
    y.append(k["carril"]["pista"])

x = []
for l in zip(*y):
    x.append(l)

for i in range(len(x)):
    for j in range(game["num_players"]):
        print("|", end="")
        if x[i][j].isnumeric() and x[i - 1][j] == " ":
            if x[i - 1][j] == " ":
                num = game["jug"][j]["carril"]["num"]
                print("J" + num, end="")
        else:
            tama = game["jug"][j]["carril"]["tama"]
            print(" " * (tama + 1), end="")
    print("|")
#######################################

while True:
    opcion = int(input('''
Elija una opción:
    1: Carrera
    2: Mirar Veces ganadas
    3: Salir
Opción: '''))

    if opcion == 1:
        continuar = 1
        # Lista usada para idenfitificar los ganadores
        lista = list(range(game["num_players"]))

        while continuar:
            input("\nIngrese una tecla para continuar: \n")

            # Se actualiza la posición de los jugadores que no han llegado a la meta
            for j in lista:
                ran = randint(1, 6)  # avance de 1 a 6
                game["jug"][j]["conductor"]["pos"] += ran

                # Se limita el avance al tamaño de la meta
                if game["jug"][j]["conductor"]["pos"] > tamano_pista:
                    game["jug"][j]["conductor"]["pos"] = tamano_pista

                # Se actualiza el carril
                num = game["jug"][j]["carril"]["num"]
                index = game["jug"][j]["conductor"]["pos"]
                # Se agrega un " " al principio siempre para facilitar el trabajo
                # al momento de dibujar la pista
                pista = " " * (index - 1) + num
                pista += " " * (tamano_pista - len(pista))
                game["jug"][j]["carril"]["pista"] = pista

            y = []  # Arreglo para guardar los carriles
            for k in game["jug"]:
                y.append(k["carril"]["pista"])

            x = []  # Arreglo que guarda los carriles de forma vertical
            for l in zip(*y):
                x.append(l)

            # Se dibuja la pista
            for i in range(len(x)):  # se itera para el largo de la pista
                for j in range(game["num_players"]):  # Se itera por la cantidad de jugadores
                    print("|", end="")  # se dibuja un extremo de la pista

                    # Con la condición se garantiza que se dibuje el identificador en una sola línea
                    if x[i][j].isnumeric() and x[i - 1][j] == " ":
                        num = game["jug"][j]["carril"]["num"]
                        print("J" + num, end="")
                        # De lo contrario se debe imprimir un tamaño lo suficientemente grande para incluir el identificador
                    else:
                        tama = game["jug"][j]["carril"]["tama"]
                        print(" " * (tama + 1), end="")
                print("|")

            # Se genera una lista aleatoria para poder evaluar el orden
            # de llegada de forma aleatoria, justamente.
            # Si no se hiciese así, en el caso que al actualizar las
            # posiciones J1, J2 y J3 llegaran a la meta, siempre ganaría J1 el primer
            # lugar, J2 el segundo y J3 el tercero.
            ran_list = []
            itera = len(lista)
            copia = lista[:]
            for i in range(itera):
                # Se toma un elemento aleatorio de la lista de los que no han ganado aún
                ran_num = sample(copia, 1)[0]
                index = copia.index(ran_num)
                ran_list.append(copia[index])
                copia.remove(ran_num)

            # se verifica si hay ganadores
            for i in ran_list:
                if game["jug"][i]["conductor"]["pos"] == tamano_pista:
                    # Se toma la posición de ganador
                    orden = game["ganadores"]["orden"]
                    game["ganadores"][orden] = i + 1
                    # Se actualiza las veces ganadas por ese jugador
                    game["jugadas"][i + 1][orden] += 1
                    # Se actualiza el orden para el siguiente ganador
                    game["ganadores"]["orden"] += 1
                    # Se remueve el jugador de la lista ya que llegó a la meta
                    lista.remove(i)

                # Si llegaron 3 jugadores se acaba el juego
                if game["ganadores"]["orden"] == 4:
                    continuar = 0
                    break

        # se muestran los ganadores
        print("\nPODIO:")
        print("Primer lugar:", "J" + str(game["ganadores"][1]))
        print("segundo lugar:", "J" + str(game["ganadores"][2]))
        print("tercer lugar:", "J" + str(game["ganadores"][3]))

    # Se imprime la cantidad de veces ganadas
    elif opcion == 2:
        print("\nJugador: Primer lugar, Segundo, tercero")
        for L in game["jugadas"]:
            print(f"J{L}: {game['jugadas'][L][1]}, {game['jugadas'][L][2]}, {game['jugadas'][L][3]}")
    # Se sale del juego
    elif opcion == 3:
        print("\nGracias Por jugar")
        break
    # Opción Erronea
    else:
        print("\nIngrese una opción válida")

# Se reescribe el archivo con el mismo formato
file = open("DDBB.txt", "w", encoding="UTF-8")

for L in game["jugadas"]:
    file.write(f"{L}:{game['jugadas'][L][1]},{game['jugadas'][L][2]},{game['jugadas'][L][3]}\n")

file.close()



