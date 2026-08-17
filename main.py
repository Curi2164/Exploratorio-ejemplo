import random

# no sabia como hacerlo lo hice asi y funciona asi jkfhdhs
dictionario = {1: "Piedra", 2: "Papel", 3:"Tijera", 4:"Lizard", 5:"Spock"}
ganan_a_piedra = (2, 5)
ganan_a_papel = (3, 4)
ganan_a_tijera = (1, 5)
ganan_a_lizard = (1, 3)
ganan_a_spock = (2, 4)
matriz = ((0,1,0,0,1), (0,0,1,1,0), (1,0,0,0,1), (1,0,1,0,0), (0,1,0,1,0))
inputs_correctos = (1,2,3,4,567)

def start_game():
    print("*********************")
    print("BIENVENIDO!") #ndeaah
    print("Para jugar debes seleccionar tu próximo movimiento entre estas opciones")
    for i in range(1,6):
        print(f"{i}. {dictionario[i]}")
    print("Indica tu opción:")
    user_input = int(input())
    while user_input not in inputs_correctos:
        if user_input == 67:
                    print("SIX SEVEN!!!")
        print("Opcion no valida, reintenta")
        user_input = int(input())
    random_input = random.randint(1,5)
    print(f"tu eleccion: {dictionario[user_input]}")
    print(f"eleccion de la máquina: {dictionario[random_input]}")
    if user_input == random_input:
        print(f"Empate! Ambos eligieron {dictionario[user_input]}!")
    elif matriz[random_input - 1][user_input - 1] == 1:
        print("Has ganado ostia!")
    else:
        print("Has perdido :(")


start_game()
