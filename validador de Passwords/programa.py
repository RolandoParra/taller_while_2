import time
bienvenida = r"""
                                      ,--.                               ,--.                         ,----..    
    ,---,.    ,---,    ,---,.       ,--.'|                ,---,.       ,--.'|   ,---,    ,---,       /   /   \   
  ,'  .'  \,`--.' |  ,'  .' |   ,--,:  : |       ,---.  ,'  .' |   ,--,:  : |,`--.' |  .'  .' `\    /   .     :  
,---.' .' ||   :  :,---.'   |,`--.'`|  ' :      /__./|,---.'   |,`--.'`|  ' :|   :  :,---.'     \  .   /   ;.  \ 
|   |  |: |:   |  '|   |   .'|   :  :  | | ,---.;  ; ||   |   .'|   :  :  | |:   |  '|   |  .`\  |.   ;   /  ` ; 
:   :  :  /|   :  |:   :  |-,:   |   \ | :/___/ \  | |:   :  |-,:   |   \ | :|   :  |:   : |  '  |;   |  ; \ ; | 
:   |    ; '   '  ;:   |  ;/||   : '  '; |\   ;  \ ' |:   |  ;/||   : '  '; |'   '  ;|   ' '  ;  :|   :  | ; | ' 
|   :     \|   |  ||   :   .''   ' ;.    ; \   \  \: ||   :   .''   ' ;.    ;|   |  |'   | ;  .  |.   |  ' ' ' : 
|   |   . |'   :  ;|   |  |-,|   | | \   |  ;   \  ' .|   |  |-,|   | | \   |'   :  ;|   | :  |  ''   ;  \; /  | 
'   :  '; ||   |  ''   :  ;/|'   : |  ; .'   \   \   ''   :  ;/|'   : |  ; .'|   |  ''   : | /  ;  \   \  ',  /  
|   |  | ; '   :  ||   |    \|   | '`--'      \   `  ;|   |    \|   | '`--'  '   :  ||   | '` ,/    ;   :    /   
|   :   /  ;   |.' |   :   .''   : |           :   \ ||   :   .''   : |      ;   |.' ;   :  .'       \   \ .'    
|   | ,'   '---'   |   | ,'  ;   |.'            '---" |   | ,'  ;   |.'      '---'   |   ,.'          `---`      
`----'             `----'    '---'                    `----'    '---'                '---'                       
"""
boom = r"""
$$$$$$$\   $$$$$$\   $$$$$$\  $$\      $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |
$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$\  $$$$ |
$$$$$$$\ |$$ |  $$ |$$ |  $$ |$$\$$\$$ $$ |
$$  __$$\ $$ |  $$ |$$ |  $$ |$$ \$$$  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |
$$$$$$$  | $$$$$$  | $$$$$$  |$$ | \_/ $$ |
\_______/  \______/  \______/ \__|     \__|
"""
fallas = 0


print(bienvenida)

print()
print("Bienvenido a la caja fuerte del banco nacional mundial, por favor, ingrese la contraseña para acceder a los datos, señor Presidente")
print()
print()
password = input("\033[32mIngrese la contraseña: \033[0m")

while password != "python123":
    print("\033[31mERROR: Contraseña incorrecta, por favor intente de nuevo\033[0m")
    fallas += 1
    if fallas == 3:
        print("\033[31mERROR: Haz excedido el límite de intetos, el programa se auto destruirá\033[0m")
        time.sleep(1)
        print("\033[31m3\033[0m")
        time.sleep(1)
        print("\033[31m2\033[0m")
        time.sleep(1)
        print("\033[31m1\033[0m")
        time.sleep(1)
        print(boom)
        exit()
    password = input("\033[32mIngrese la contraseña: \033[0m")

print("\033[32mContraseña correcta, bienvenido señor Presidente\033[0m")
input()