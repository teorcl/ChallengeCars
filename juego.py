# Archivo principal

from random import randint, sample

#import jugador

dicc = {}

file = open("DDBB.txt", encoding="UTF-8")

for linea in file:
    index = linea.index(":")
    num = linea[:index]
    a = linea[index + 1:-1]
    b = a.split(",")
    dicc[int(num)] = {1: int(b[0]), 2: int(b[1]), 3: int(b[2])}

file.close()

while True:
    #num = jugador.jugador1.num_players
    #print(num)
    num_players = int(input("Ingrese # jugadores"))
    if num_players < 3:
        print('Debe ingresar como mínimo 3 jugadores')
    elif num_players > 20:
        print('Deben de ser menos de 20 jugadores')
    else:
        break
tamano_pista = 30  # multiplicar por 1000

game = {"jug": [], "num_players": 0, "ganadores": {1: "", 2: "", 3: "", "orden": 1}, "jugadas": dicc}
game["num_players"] = num_players

for i in range(num_players):
    carril = str(i + 1) + " " * (tamano_pista - len(str(i + 1)))
    game["jug"].append({"carril": {"pista": carril, "tama": [], "num": []}, "conductor": {"pos": 2}})

for i in range(len(game["jug"])):
    a = str(int(game["jug"][i]["carril"]["pista"]))
    game["jug"][i]["carril"]["num"] = a
    b = len(a)
    game["jug"][i]["carril"]["tama"] = b

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

continuar = 1
lista = list(range(game["num_players"]))
while continuar:
    input("Ingrese una tecla para continuar")

    for i in game["jug"]:
        if i["conductor"]["pos"] < tamano_pista:
            ran = randint(1, 6)
            i["conductor"]["pos"] += ran

            if i["conductor"]["pos"] > tamano_pista:
                i["conductor"]["pos"] = tamano_pista

    for j in range(len(game["jug"])):
        num = game["jug"][j]["carril"]["num"]
        index = game["jug"][j]["conductor"]["pos"]
        pista = " " * (index - 1) + num
        pista += " " * (tamano_pista - len(pista))
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

    ran_list = []
    itera = len(lista)
    copia = lista[:]
    for i in range(itera):
        ran_num = sample(copia, 1)[0]
        index = copia.index(ran_num)
        ran_list.append(copia[index])
        copia.remove(ran_num)

    for i in ran_list:
        if game["jug"][i]["conductor"]["pos"] == tamano_pista:
            orden = game["ganadores"]["orden"]
            game["ganadores"][orden] = i + 1
            game["jugadas"][i + 1][orden] += 1
            game["ganadores"]["orden"] += 1
            lista.remove(i)

        if game["ganadores"]["orden"] == 4:
            continuar = 0
            break

print("-----------PODIO------------")
print('\n')
for i in range(3):
    print((' '*6)+('*'*6))
for i in range(3):
    print(('*'*18))

print('\n')
print("Primer lugar:", "J" + str(game["ganadores"][1]))
print("segundo lugar:", "J" + str(game["ganadores"][2]))
print("tercer lugar:", "J" + str(game["ganadores"][3]))

file = open("DDBB.txt", "w", encoding="UTF-8")

for L in game["jugadas"]:
    file.write(f"{L}:{game['jugadas'][L][1]},{game['jugadas'][L][2]},{game['jugadas'][L][3]}\n")

file.close()

print("Jugadores y veces ganadas según la posicion")
print("Jugador: #veces primer puesto, #veces segundo puesto, #veces tercer puesto, ")
file = open("DDBB.txt", "r")
print(file.read())

file.close()




