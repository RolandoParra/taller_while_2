import random
import time
vida_player = 50
vida_enemigo = 50
ataque_player = 0
ataque_enemigo = 0

input("Bienvenido al juego de rol, presiona enter para comenzar")
print()
print("__________________________________________________________________________________________________________________________")
while vida_player > 0 and vida_enemigo > 0:
    time.sleep(1)
    print()
    print(f"\033[32mtu vida es: {vida_player}\033[0m")
    print(f"\033[31mvida del enemigo es: {vida_enemigo}\033[0m")
    ataque_player = random.randint(1, 20)
    ataque_enemigo = random.randint(1, 20)
    vida_enemigo -= ataque_player
    vida_player -= ataque_enemigo
    time.sleep(1)
    print()
    print(f"\033[32mTu atacaste al enemigo con {ataque_player} puntos de daño\033[0m")
    print(f"\033[31mEl enemigo te atacó con {ataque_enemigo} puntos de daño\033[0m")
    if vida_player <= 0:
        break
    if vida_enemigo <= 0:
        break

print()
print()
print("__________________________________________________________________________________________________________________________")
if vida_player <= 0:
    print("Has sido derrotado por el enemigo, mejor suerte la próxima vez")
elif vida_enemigo <= 0:
    print("Felicidades, has derrotado al enemigo, eres un gran guerrero")

input()