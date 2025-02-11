import sys

# Color codes for terminal output
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

# ASCII Art
caesar_art = '''
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
'''

goodbye_art = '''
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
                                                                   `--`            
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
history = []

def ceaser(text, shift, direction, custom_alphabet):
    if not custom_alphabet:
        custom_alphabet = alphabet
    cipher_text = ""
    shift = shift % len(custom_alphabet)
    
    if direction == "e":
        for letter in text:
            if letter in custom_alphabet:
                index_old = custom_alphabet.index(letter)
                new_index = (index_old + shift) % len(custom_alphabet)
                cipher_text += custom_alphabet[new_index]
            else:
                cipher_text += letter
        return cipher_text
            
    elif direction == "d":
        for letter in text:
            if letter in custom_alphabet:
                index_old = custom_alphabet.index(letter)
                new_index = (index_old - shift) % len(custom_alphabet)
                cipher_text += custom_alphabet[new_index]
            else:
                cipher_text += letter
        return cipher_text

def add_to_history(direction, text, shift, result):
    history.append({
        'direction': direction,
        'text': text,
        'shift': shift,
        'result': result
    })

def view_history():
    if not history:
        print(f"{RED}No history available.{RESET}")
        return
    for i, entry in enumerate(history):
        print(f"{BOLD}Entry {i+1}:{RESET}")
        print(f"Direction: {'Encrypt' if entry['direction'] == 'e' else 'Decrypt'}")
        print(f"Original Text: {entry['text']}")
        print(f"Shift: {entry['shift']}")
        print(f"Result: {entry['result']}\n")

def show_menu():
    print(f"\n{YELLOW}Menu:{RESET}")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. View History")
    print("4. Exit")

def handle_menu_option(option):
    if option == '1' or option == '2':
        direction = 'e' if option == '1' else 'd'
        custom_alphabet = input("Enter a custom alphabet (or press Enter to use default):\n").lower()
        if not custom_alphabet:
            custom_alphabet = alphabet

        text = input("Type your message:\n").lower()
        
        try:
            shift = int(input("Type the shift number:\n"))
            if shift < 0:
                print(f"{RED}Shift number must be non-negative!{RESET}")
                return
        except ValueError:
            print(f"{RED}Invalid shift number!{RESET}")
            return

        cipher_text = ceaser(text, shift, direction, custom_alphabet)
        print(f"{GREEN}Result: {cipher_text}{RESET}")
        add_to_history(direction, text, shift, cipher_text)

    elif option == '3':
        view_history()

    elif option == '4':
        print(f"{YELLOW}{goodbye_art}{RESET}")
        print(f"{YELLOW}Hope you had fun. See you next time!{RESET}")
        sys.exit()

    else:
        print(f"{RED}Invalid option! Please select a valid menu option.{RESET}")

# Main Program Loop
print(f"{BOLD}{caesar_art}{RESET}")

while True:
    show_menu()
    choice = input(f"\n{YELLOW}Please choose an option (1-4):{RESET} ").strip()
    handle_menu_option(choice)
