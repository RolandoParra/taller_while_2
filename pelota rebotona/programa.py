import time
bienvenido = r"""
BBBBBBBBBBBBBBBBB   IIIIIIIIIIEEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNNVVVVVVVV           VVVVVVVVEEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNNIIIIIIIIIIDDDDDDDDDDDDD             OOOOOOOOO     
B::::::::::::::::B  I::::::::IE::::::::::::::::::::EN:::::::N       N::::::NV::::::V           V::::::VE::::::::::::::::::::EN:::::::N       N::::::NI::::::::ID::::::::::::DDD        OO:::::::::OO   
B::::::BBBBBB:::::B I::::::::IE::::::::::::::::::::EN::::::::N      N::::::NV::::::V           V::::::VE::::::::::::::::::::EN::::::::N      N::::::NI::::::::ID:::::::::::::::DD    OO:::::::::::::OO 
BB:::::B     B:::::BII::::::IIEE::::::EEEEEEEEE::::EN:::::::::N     N::::::NV::::::V           V::::::VEE::::::EEEEEEEEE::::EN:::::::::N     N::::::NII::::::IIDDD:::::DDDDD:::::D  O:::::::OOO:::::::O
  B::::B     B:::::B  I::::I    E:::::E       EEEEEEN::::::::::N    N::::::N V:::::V           V:::::V   E:::::E       EEEEEEN::::::::::N    N::::::N  I::::I    D:::::D    D:::::D O::::::O   O::::::O
  B::::B     B:::::B  I::::I    E:::::E             N:::::::::::N   N::::::N  V:::::V         V:::::V    E:::::E             N:::::::::::N   N::::::N  I::::I    D:::::D     D:::::DO:::::O     O:::::O
  B::::BBBBBB:::::B   I::::I    E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N   V:::::V       V:::::V     E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N  I::::I    D:::::D     D:::::DO:::::O     O:::::O
  B:::::::::::::BB    I::::I    E:::::::::::::::E   N::::::N N::::N N::::::N    V:::::V     V:::::V      E:::::::::::::::E   N::::::N N::::N N::::::N  I::::I    D:::::D     D:::::DO:::::O     O:::::O
  B::::BBBBBB:::::B   I::::I    E:::::::::::::::E   N::::::N  N::::N:::::::N     V:::::V   V:::::V       E:::::::::::::::E   N::::::N  N::::N:::::::N  I::::I    D:::::D     D:::::DO:::::O     O:::::O
  B::::B     B:::::B  I::::I    E::::::EEEEEEEEEE   N::::::N   N:::::::::::N      V:::::V V:::::V        E::::::EEEEEEEEEE   N::::::N   N:::::::::::N  I::::I    D:::::D     D:::::DO:::::O     O:::::O
  B::::B     B:::::B  I::::I    E:::::E             N::::::N    N::::::::::N       V:::::V:::::V         E:::::E             N::::::N    N::::::::::N  I::::I    D:::::D     D:::::DO:::::O     O:::::O
  B::::B     B:::::B  I::::I    E:::::E       EEEEEEN::::::N     N:::::::::N        V:::::::::V          E:::::E       EEEEEEN::::::N     N:::::::::N  I::::I    D:::::D    D:::::D O::::::O   O::::::O
BB:::::BBBBBB::::::BII::::::IIEE::::::EEEEEEEE:::::EN::::::N      N::::::::N         V:::::::V         EE::::::EEEEEEEE:::::EN::::::N      N::::::::NII::::::IIDDD:::::DDDDD:::::D  O:::::::OOO:::::::O
B:::::::::::::::::B I::::::::IE::::::::::::::::::::EN::::::N       N:::::::N          V:::::V          E::::::::::::::::::::EN::::::N       N:::::::NI::::::::ID:::::::::::::::DD    OO:::::::::::::OO 
B::::::::::::::::B  I::::::::IE::::::::::::::::::::EN::::::N        N::::::N           V:::V           E::::::::::::::::::::EN::::::N        N::::::NI::::::::ID::::::::::::DDD        OO:::::::::OO   
BBBBBBBBBBBBBBBBB   IIIIIIIIIIEEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNN            VVV            EEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNNIIIIIIIIIIDDDDDDDDDDDDD             OOOOOOOOO     
"""

proceso = r"""
,-.----.                 ,----..                                                            ,--.                 ,----..                 
\    /  \  ,-.----.     /   /   \    ,----..      ,---,.  .--.--.      ,---,              ,--.'|    ,---,       /   /   \                
|   :    \ \    /  \   /   .     :  /   /   \   ,'  .' | /  /    '.   '  .' \         ,--,:  : |  .'  .' `\    /   .     :               
|   |  .\ :;   :    \ .   /   ;.  \|   :     :,---.'   ||  :  /`. /  /  ;    '.    ,`--.'`|  ' :,---.'     \  .   /   ;.  \              
.   :  |: ||   | .\ :.   ;   /  ` ;.   |  ;. /|   |   .';  |  |--`  :  :       \   |   :  :  | ||   |  .`\  |.   ;   /  ` ;              
|   |   \ :.   : |: |;   |  ; \ ; |.   ; /--` :   :  |-,|  :  ;_    :  |   /\   \  :   |   \ | ::   : |  '  |;   |  ; \ ; |              
|   : .   /|   |  \ :|   :  | ; | ';   | ;    :   |  ;/| \  \    `. |  :  ' ;.   : |   : '  '; ||   ' '  ;  :|   :  | ; | '              
;   | |`-' |   : .  /.   |  ' ' ' :|   : |    |   :   .'  `----.   \|  |  ;/  \   \'   ' ;.    ;'   | ;  .  |.   |  ' ' ' :              
|   | ;    ;   | |  \'   ;  \; /  |.   | '___ |   |  |-,  __ \  \  |'  :  | \  \ ,'|   | | \   ||   | :  |  ''   ;  \; /  |              
:   ' |    |   | ;\  \\   \  ',  / '   ; : .'|'   :  ;/| /  /`--'  /|  |  '  '--'  '   : |  ; .''   : | /  ;  \   \  ',  /               
:   : :    :   ' | \.' ;   :    /  '   | '/  :|   |    \'--'.     / |  :  :        |   | '`--'  |   | '` ,/    ;   :    /___  ___  ___   
|   | :    :   : :-'    \   \ .'   |   :    / |   :   .'  `--'---'  |  | ,'        '   : |      ;   :  .'       \   \ .'/  .\/  .\/  .\  
`---'.|    |   |.'       `---`      \   \ .'  |   | ,'              `--''          ;   |.'      |   ,.'          `---`  \  ; \  ; \  ; | 
  `---`    `---'                     `---`    `----'                               '---'        '---'                    `--" `--" `--"  
"""


print(bienvenido)

print()
print()
h = float(input("Ingrese la altura de la que se suelta la pelota: "))
quinta_parte = h / 5
new_h = h
rebotes = 0




print()
print("________________________________________________________________________________________________________________________________________________________________________________")
print(proceso)
print()
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
print()
print("________________________________________________________________________________________________________________________________________________________________________________")
print()
print()



while new_h > quinta_parte:
    new_h = new_h * 0.5
    rebotes += 1
    print()
    print("...")
    time.sleep(2)
    print(f"Rebote {rebotes}: {new_h}")
    if new_h <= quinta_parte:
        print()
        print("La pelota llegó a su quinta parte de la altura inicial o menos")
        print(new_h)
        break
print()
print(f"La pelota rebotó {rebotes} veces")

input()