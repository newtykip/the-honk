import curses
from typing import List, Tuple, Callable, Any

class Application:
    def __init__(self):
        # Initialise curses
        self.__curses = curses.initscr()
        self.__curses.keypad(True)

        curses.start_color() # todo: check for colour support
        curses.cbreak()
        curses.noecho()

        # Default colours
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK) # default
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE) # selected

    def selectMenu(self, options: List[Tuple[str, Callable[[], Any]]]):
        selectedIndex = 0
        optionCount = len(options)
        screen = self.__curses

        while True:
            screen.clear()
            screen.addstr("Pick an option:\n\n", curses.A_BOLD)

            for i in range(optionCount):
                colour = curses.color_pair(2) if i == selectedIndex else curses.color_pair(1)
                screen.addstr(f"{i + 1}. ")
                screen.addstr(f"{options[i][0]}\n", colour)

            c = screen.getch()

            if c in [curses.KEY_UP, curses.KEY_LEFT]:
                selectedIndex = (selectedIndex + optionCount - 1) % optionCount
            elif c in [curses.KEY_DOWN, curses.KEY_RIGHT]:
                selectedIndex = (selectedIndex + 1) % optionCount
            elif c == curses.KEY_ENTER or chr(c) in '\n\r':
                break
        
        options[selectedIndex][1]()

    def quit(self):
        curses.nocbreak()
        self.__curses.keypad(False)
        curses.echo()
        curses.endwin()

app = Application()
app.selectMenu([("yes", lambda: (app.quit(),print("i dont think so"))), ("no", lambda: (app.quit(), print("no need to be a cynic")))])