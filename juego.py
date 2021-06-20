# -*- coding: utf-8 -*-

from random import randint, sample

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

    lista = list(range(game["num_players"]))
    ran_list = []
    itera = len(lista)
    for i in range(itera):
        ran_num = sample(lista, 1)[0]
        index = lista.index(ran_num)
        ran_list.append(lista[index])
        lista.remove(ran_num)

    copia = ran_list[:]
    for i in copia:
        if game["jug"][i]["conductor"]["pos"] == tamano_pista:
            orden = game["ganadores"]["orden"]
            game["ganadores"][orden] = i + 1
            game["jugadas"][i + 1][orden] += 1
            game["ganadores"]["orden"] += 1
            ran_list.remove(i)

        if game["ganadores"]["orden"] == 4:
            continuar = 0
            break

print("Ganadores:")
print("Primer lugar:", "J" + str(game["ganadores"][1]))
print("segundo lugar:", "J" + str(game["ganadores"][2]))
print("tercer lugar:", "J" + str(game["ganadores"][3]))

file = open("rata.txt", "w", encoding="UTF-8")

for L in game["jugadas"]:
    file.write(f"{L}:{game['jugadas'][L][1]},{game['jugadas'][L][2]},{game['jugadas'][L][3]}\n")

file.close()




