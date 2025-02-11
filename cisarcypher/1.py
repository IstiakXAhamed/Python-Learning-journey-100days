print('''                                                                                                                                     
                                                                                                                                     
  ,----..                                                                 ,----..                       ,---,                        
 /   /   \                                                               /   /   \   ,--,   ,-.----.  ,--.' |                        
|   :     :                                              __  ,-.        |   :     :,--.'|   \    /  \ |  |  :                __  ,-. 
.   |  ;. /                       .--.--.              ,' ,'/ /|        .   |  ;. /|  |,    |   :    |:  :  :              ,' ,'/ /| 
.   ; /--`   ,--.--.     ,---.   /  /    '    ,--.--.  '  | |' |        .   ; /--` `--'_    |   | .\ ::  |  |,--.   ,---.  '  | |' | 
;   | ;     /       \   /     \ |  :  /`./   /       \ |  |   ,'        ;   | ;    ,' ,'|   .   : |: ||  :  '   |  /     \ |  |   ,' 
|   : |    .--.  .-. | /    /  ||  :  ;_    .--.  .-. |'  :  /          |   : |    '  | |   |   |  \ :|  |   /' : /    /  |'  :  /   
.   | '___  \__\/: . ..    ' / | \  \    `.  \__\/: . .|  | '           .   | '___ |  | :   |   : .  |'  :  | | |.    ' / ||  | '    
'   ; : .'| ," .--.; |'   ;   /|  `----.   \ ," .--.; |;  : |           '   ; : .'|'  : |__ :     |`-'|  |  ' | :'   ;   /|;  : |    
'   | '/  :/  /  ,.  |'   |  / | /  /`--'  //  /  ,.  ||  , ;           '   | '/  :|  | '.'|:   : :   |  :  :_:,''   |  / ||  , ;    
|   :    /;  :   .'   \   :    |'--'.     /;  :   .'   \---'            |   :    / ;  :    ;|   | :   |  | ,'    |   :    | ---'     
 \   \ .' |  ,     .-./\   \  /   `--'---' |  ,     .-./                 \   \ .'  |  ,   / `---'.|   `--''       \   \  /           
  `---`    `--`---'     `----'              `--`---'                      `---`     ---`-'    `---`                `----'            
                                                                                                                                     ''')
print("Welcome to out encryption and decryption tool!! have fun !! hope you like the tool stay tuned!!!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text, shift,direction):
    if direction=="e":
        cipher_text=""
        
        for letter in text:
            if letter in alphabet:
                indexOld= alphabet.index(letter)
                newIndex= (indexOld+shift)%26
                cipher_text = cipher_text+alphabet[newIndex] 
            else:
                cipher_text= cipher_text+letter
        print(cipher_text)
            
    elif direction=="d":
        cipher_text=""
        
        for letter in text:
            if letter in alphabet:
                indexOld= alphabet.index(letter)
                newIndex= (indexOld-shift)%26
                cipher_text = cipher_text+alphabet[newIndex] 
            else:
                cipher_text= cipher_text+letter
        print(cipher_text)
    
          
repeat = True

while repeat==True :
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    if direction!="e" and direction!="d":
        print("Please enter the valid option between e or d!!!!")
        continue
    elif direction=="e" or direction=="d":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))  
        ceaser(text,shift,direction)            
        repeatWhole = input( "do you want to use again ?")
        if repeatWhole == "yes":
            repeat=True
        elif repeatWhole == "no":
            repeat=False  
            
print("Hope You had fun. We will wait for you...see yaaa!!") 
print("""                                                                                  
                                                                        
,----..                                              ,---,.                     
/   /   \                            ,---,          ,'  .'  \                    
|   :     :    ,---.     ,---.      ,---.'|        ,---.' .' |                    
.   |  ;. /   '   ,'\   '   ,'\     |   | :        |   |  |: |                    
.   ; /--`   /   /   | /   /   |    |   | |        :   :  :  /     .--,   ,---.   
;   | ;  __ .   ; ,. :.   ; ,. :  ,--.__| |        :   |    ;    /_ ./|  /     \  
|   : |.' .''   | |: :'   | |: : /   ,'   |        |   :     \, ' , ' : /    /  | 
.   | '_.' :'   | .; :'   | .; :.   '  /  |        |   |   . /___/ \: |.    ' / | 
'   ; : \  ||   :    ||   :    |'   ; |:  |        '   :  '; |.  \  ' |'   ;   /| 
'   | '/  .' \   \  /  \   \  / |   | '/  '        |   |  | ;  \  ;   :'   |  / | 
|   :    /    `----'    `----'  |   :    :|        |   :   /    \  \  ;|   :    | 
\   \ .'                        \   \  /          |   | ,'      :  \  \\   \  /  
`---`                           `----'           `----'         \  ' ; `----'   
                                                                `--`           """) 
        