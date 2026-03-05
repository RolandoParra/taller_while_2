import random
import time
bienvenido = r"""
_______   ______  ________  __    __  __     __  ________  __    __  ______  _______    ______  
|       \ |      \|        \|  \  |  \|  \   |  \|        \|  \  |  \|      \|       \  /      \ 
| $$$$$$$\ \$$$$$$| $$$$$$$$| $$\ | $$| $$   | $$| $$$$$$$$| $$\ | $$ \$$$$$$| $$$$$$$\|  $$$$$$\
| $$__/ $$  | $$  | $$__    | $$$\| $$| $$   | $$| $$__    | $$$\| $$  | $$  | $$  | $$| $$  | $$
| $$    $$  | $$  | $$  \   | $$$$\ $$ \$$\ /  $$| $$  \   | $$$$\ $$  | $$  | $$  | $$| $$  | $$
| $$$$$$$\  | $$  | $$$$$   | $$\$$ $$  \$$\  $$ | $$$$$   | $$\$$ $$  | $$  | $$  | $$| $$  | $$
| $$__/ $$ _| $$_ | $$_____ | $$ \$$$$   \$$ $$  | $$_____ | $$ \$$$$ _| $$_ | $$__/ $$| $$__/ $$
| $$    $$|   $$ \| $$     \| $$  \$$$    \$$$   | $$     \| $$  \$$$|   $$ \| $$    $$ \$$    $$
 \$$$$$$$  \$$$$$$ \$$$$$$$$ \$$   \$$     \$     \$$$$$$$$ \$$   \$$ \$$$$$$ \$$$$$$$   \$$$$$$ 
"""
felicidades = r"""
 (                                                   
 )\ )      (               (           (             
(()/(   (  )\ (       (    )\ )    )   )\ )   (      
 /(_)) ))\((_))\   (  )\  (()/( ( /(  (()/(  ))\ (   
(_))_|/((_)_ ((_)  )\((_)  ((_)))(_))  ((_))/((_))\  
| |_ (_)) | | (_) ((_)(_)  _| |((_)_   _| |(_)) ((_) 
| __|/ -_)| | | |/ _| | |/ _` |/ _` |/ _` |/ -_)(_-< 
|_|  \___||_| |_|\__| |_|\__,_|\__,_|\__,_|\___|/__/ 
"""

pc_number = random.randint(1, 100)
player_number = 0

print(bienvenido)
print()
print("Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100, ¿puedes adivinar cuál es?")
player_number = int(input("Ingresa tu número: "))

if player_number > 100 or player_number < 1:
    print("\033[31mNúmero inválido, por favor ingresa un número entre 1 y 100\033[0m")
    exit()
while player_number != pc_number:
    print()
    if player_number < pc_number:
        print("El número es mayor que", player_number)
    else:
        print("El número es menor que", player_number)
    player_number = int(input("Ingresa tu número: "))

print("Felicidades! adivinaste el número!!!! ^w^")
input()