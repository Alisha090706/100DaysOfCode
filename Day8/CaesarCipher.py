logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
def caesar_cipher(mes,shift,direction):
    new_mes=""
    if direction=='decode':
        shift*=-1
    for i in mes:
        if i.isalpha():
            if i.islower():
                new_mes+=chr(ord('a') +(ord(i)-ord('a')+shift)%26)
            else:
                new_mes+=chr(ord('A') +(ord(i)-ord('A')+shift)%26)
        else:
            new_mes+=i
    
    print(f"Here is your {direction} result: {new_mes}")
while True:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    mes=input("Type a message\n")
    shift=int(input("Type shift\n"))
    caesar_cipher(mes,shift,direction)
    choice=input("Type 'yes' if you want to go again, otherwise 'no'\n").lower()
    if choice=='no':
        break

    
