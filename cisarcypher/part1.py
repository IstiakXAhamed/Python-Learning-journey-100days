alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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

repeat = True
while repeat==True :
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt(text, shift):
        cipher_text=""
        
        for letter in text:
            if letter in alphabet:
                indexOld= alphabet.index(letter)
                newIndex= (indexOld+shift)%26
                cipher_text = cipher_text+alphabet[newIndex] 
            else:
                cipher_text= cipher_text+letter
        print(cipher_text)       
    if direction=="e":
        encrypt(text,shift)                
    elif direction== "d":
        encrypt(text,-shift)          
    repeatWhole = input( "do you want to use again ?")
    if repeatWhole == "y":
        repeat=True
    elif repeatWhole == "n":
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
         