# windows: pip install windows-curses
import curses
from operator import and_, or_, xor

def initCurses() -> tuple:
    """Initialise curses and any necessary colour pairs"""
    screen = curses.initscr()
    screen.keypad(True)

    curses.cbreak()
    curses.noecho()
    curses.start_color()

    # default
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    default = curses.color_pair(1)

    # highlighted
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    highlighted = curses.color_pair(2)

    # error
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    error = curses.color_pair(3)
    
    return (screen, (default, highlighted, error))

def destroyCurses(screen):
    """Close out of curses and reverse any destructive changes to the terminal"""
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()

def selectMenu(screen, options: list, header: str = "Pick an option:"):
    selectedIndex = 0
    optionCount = len(options)

    while True:
        screen.clear()
        screen.addstr(f"{header}\n\n", curses.A_BOLD)

        for i in range(optionCount):
            screen.addstr(f"{i + 1}. ")
            screen.addstr(f"{options[i]}\n", highlighted if i == selectedIndex else default)

        c = screen.getch()

        if c == curses.KEY_UP or c == curses.KEY_LEFT:
            selectedIndex -= 1 - optionCount
            selectedIndex %= optionCount
        
        elif c == curses.KEY_DOWN or c == curses.KEY_RIGHT:
            selectedIndex += 1
            selectedIndex %= optionCount

        elif c == curses.KEY_ENTER or chr(c) in '\n\r':
            return selectedIndex + 1

def getBinary(screen, prompt: str, length: int = None) -> list:
    errorMessage = None

    while True:
        screen.clear()
        screen.addstr(0, 0, f"{prompt}", curses.A_BOLD)

        # display an error message if necessary
        if errorMessage:
            screen.addstr(3, 0, errorMessage, error | curses.A_BOLD)
            errorMessage = None

        # fetch the inputted data
        curses.echo()
        bits = list(screen.getstr(1, 0, 50).decode("utf-8"))
        curses.noecho()

        # validate that a binary value was entered
        for bit in bits:
            if bit not in ["0", "1"]:
                errorMessage = "Invalid binary number. Please try again."
                    
        if len(bits) == 0:
            errorMessage = "Please make sure you enter a value."

        elif length and len(bits) != length:
            errorMessage = f"Please make sure the value is {length} bits long."

        if errorMessage:
            continue

        return [int(x) for x in bits]

def applyOperator(screen, binary: list, mask: list) -> list:
    # todo: fix
    # operatorList = list(OPERATORS.keys())
    # symbol, operator = OPERATORS[operatorList[selectMenu(screen, operatorList) - 1]]
    # output = "".join(str(operator(a, b)) for a, b in zip(binary, mask))
    binary = "".join(str(x) for x in binary)
    mask = "".join(str(x) for x in mask)
    print(binary, mask, screen)

    while True:
        screen.clear()
        screen.addstr(0, 0, f"{binary} {mask}", curses.A_BOLD)
        screen.addstr(3, 0, "Press the backspace key to get back to the main menu.")
        screen.addstr(4, 0, "")

        # get pressed key
        c = screen.getch()

        if c == 8 or c == 127 or c == curses.KEY_BACKSPACE:
            break

OPERATORS = {
    'AND':  ('&', lambda binary, mask: applyOperator(binary, mask, and_)),
    'OR': ('|', lambda binary, mask: applyOperator(binary, mask, or_)),
    'XOR': ('^', lambda binary, mask: applyOperator(binary, mask, xor))
}

if __name__ == "__main__":
    # init curses
    screen, (default, highlighted, error) = initCurses()
    binary, mask = [], []

    while True:
        binaryStr = "[NONE]" if len(binary) == 0 else "".join(str(x) for x in binary)
        maskStr = "[NONE]" if len(mask) == 0 else "".join(str(x) for x in mask)

        choice = selectMenu(screen, ["Apply a gate", "Change the binary number", "Change the mask", "Exit"], f"Current binary number: {binaryStr}\nCurrent mask: {maskStr}\n\nWhat would you like to do?")

        if choice == 1:
            applyOperator(screen, binary, mask)
        elif choice == 2:
            binary = getBinary(screen, "Please enter a new binary value:", None if len(mask) == 0 else len)
        elif choice == 3:
            mask = getBinary(screen, "Please enter a new mask:", None if len(binary) == 0 else len(binary))
        elif choice == 4:
            break

    # destroy curses
    destroyCurses(screen)