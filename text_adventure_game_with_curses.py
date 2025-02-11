# text_adventure_game_with_curses.py

import curses

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.refresh()

    # Color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

    def draw_text_centered(y, text, color_pair=1):
        x = (curses.COLS // 2) - (len(text) // 2)
        stdscr.addstr(y, x, text, curses.color_pair(color_pair))

    def introduction():
        stdscr.clear()
        draw_text_centered(2, "Welcome to the Indie Text Adventure Game!", 2)
        draw_text_centered(4, "In this game, you'll explore different locations and make choices that affect your journey.", 3)
        draw_text_centered(6, "Let's begin!\n", 4)
        stdscr.refresh()
        stdscr.getch()

    def get_player_name():
        stdscr.clear()
        draw_text_centered(2, "Enter your name, brave adventurer: ", 2)
        stdscr.refresh()
        curses.echo()
        name = stdscr.getstr(4, curses.COLS // 2 - 10, 20).decode('utf-8')
        curses.noecho()
        draw_text_centered(6, f"Welcome, {name}!\n", 4)
        stdscr.refresh()
        stdscr.getch()
        return name

    def forest_scenario():
        stdscr.clear()
        draw_text_centered(2, "You find yourself in a dense forest. The trees are tall and the path is narrow.", 2)
        draw_text_centered(4, "1. Follow the path deeper into the forest.", 3)
        draw_text_centered(5, "2. Climb a tree to get a better view.", 3)
        draw_text_centered(6, "3. Return to the village.", 3)
        stdscr.refresh()
        choice = stdscr.getch()
        return choice

    def cave_scenario():
        stdscr.clear()
        draw_text_centered(2, "You enter a dark cave. The air is damp and you can hear water dripping.", 2)
        draw_text_centered(4, "1. Explore the cave further.", 3)
        draw_text_centered(5, "2. Light a torch.", 3)
        draw_text_centered(6, "3. Exit the cave.", 3)
        stdscr.refresh()
        choice = stdscr.getch()
        return choice

    def village_scenario():
        stdscr.clear()
        draw_text_centered(2, "You are in the village. The villagers are busy with their daily tasks.", 2)
        draw_text_centered(4, "1. Talk to the village elder.", 3)
        draw_text_centered(5, "2. Visit the market.", 3)
        draw_text_centered(6, "3. Rest at the inn.", 3)
        stdscr.refresh()
        choice = stdscr.getch()
        return choice

    introduction()
    player_name = get_player_name()
    game_active = True
    
    while game_active:
        stdscr.clear()
        draw_text_centered(2, "Choose your next location:", 2)
        draw_text_centered(4, "1. Forest", 3)
        draw_text_centered(5, "2. Cave", 3)
        draw_text_centered(6, "3. Village", 3)
        draw_text_centered(7, "4. Exit Game", 3)
        stdscr.refresh()
        location_choice = stdscr.getch()
        
        if location_choice == ord('1'):
            forest_choice = forest_scenario()
            stdscr.clear()
            if forest_choice == ord('1'):
                draw_text_centered(2, "You venture deeper into the forest and discover a hidden waterfall.", 2)
            elif forest_choice == ord('2'):
                draw_text_centered(2, "You climb a tree and spot a distant mountain range.", 2)
            elif forest_choice == ord('3'):
                draw_text_centered(2, "You return to the village safely.", 2)
            else:
                draw_text_centered(2, "Invalid choice. Please choose again.", 1)
            stdscr.refresh()
            stdscr.getch()
        
        elif location_choice == ord('2'):
            cave_choice = cave_scenario()
            stdscr.clear()
            if cave_choice == ord('1'):
                draw_text_centered(2, "You find an ancient relic hidden in the depths of the cave.", 2)
            elif cave_choice == ord('2'):
                draw_text_centered(2, "You light a torch and see beautiful cave formations.", 2)
            elif cave_choice == ord('3'):
                draw_text_centered(2, "You exit the cave and breathe fresh air.", 2)
            else:
                draw_text_centered(2, "Invalid choice. Please choose again.", 1)
            stdscr.refresh()
            stdscr.getch()
        
        elif location_choice == ord('3'):
            village_choice = village_scenario()
            stdscr.clear()
            if village_choice == ord('1'):
                draw_text_centered(2, "The village elder shares a secret about a hidden treasure.", 2)
            elif village_choice == ord('2'):
                draw_text_centered(2, "You buy some supplies from the market.", 2)
            elif village_choice == ord('3'):
                draw_text_centered(2, "You rest at the inn and regain your strength.", 2)
            else:
                draw_text_centered(2, "Invalid choice. Please choose again.", 1)
            stdscr.refresh()
            stdscr.getch()
        
        elif location_choice == ord('4'):
            draw_text_centered(2, "Thank you for playing! Goodbye!", 2)
            stdscr.refresh()
            stdscr.getch()
            game_active = False
        
        else:
            stdscr.clear()
            draw_text_centered(2, "Invalid choice. Please choose again.", 1)
            stdscr.refresh()
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
