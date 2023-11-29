from __future__ import annotations
import tkinter as tk
import sqlite3
import hashlib

DB_NAME = "histQuiz.db"
H1=("Arial", 24)

class MainMenu(tk.Frame):
    def __init__(self, container: tk.Frame, app: App):
        super().__init__(container)

        # heading
        tk.Label(self, text="History Quiz", font=H1).grid(row=0, column=0)

        # create account button
        tk.Button(self, text="Create Account", command=lambda: app.set_screen(CreateAccount)).grid(row=1, column=0)

        # create question button
        tk.Button(self, text="Create Question", command=lambda: app.set_screen(CreateQuestion)).grid(row=1, column=1)

class CreateAccount(tk.Frame):
    @staticmethod
    def create_user(username: str, password: str):
        """Connects to the database to insert the new player."""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            user = cursor.execute("SELECT Username FROM tblPlayer WHERE Username = ?", (username,)).fetchone()

            if not user:
                hash = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                cursor.execute("INSERT INTO tblPlayer (Username, Password) VALUES (?, ?)", (username, hash))
                conn.commit()
                return True

        return False

    @staticmethod
    def submit(username: str, password: str, error: tk.StringVar, app: App):
        """Process the form submission."""
        if len(username) < 5:
            error.set("Username is too short! It should at least be five characters long.")
        elif len(password) < 8:
            error.set("Password is too short! It should at least be eight characters long.")
        elif not any(c.isupper() for c in password):
            error.set("Password should contain at least one upper case character!")
        elif not any(c.isnumeric() for c in password):
            error.set("Password should contain at least one number!")
        elif not any(not c.isalnum() for c in password):
            error.set("Password should contain at least one special character!")
        else:
            res = CreateAccount.create_user(username, password)
        
            if res:
                app.set_screen(MainMenu)
            else:
                error.set("User already exists with that username!")

    def __init__(self, container: tk.Frame, app: App):
        super().__init__(container)

        # heading
        tk.Label(self, text="Create Account", font=H1).grid(row=0, column=0)

        # username
        tk.Label(self, text="Username").grid(row=1, column=0)

        username = tk.Entry(self)
        username.grid(row=1, column=1)

        # password
        tk.Label(self, text="Password").grid(row=2, column=0)

        password = tk.Entry(self, show="*")
        password.grid(row=2, column=1)

        # error label
        error = tk.StringVar()
        tk.Label(self, textvariable=error).grid(row=5, column=0)

        # submit
        tk.Button(self, text="Submit", command=lambda: CreateAccount.submit(username.get(), password.get(), error, app)).grid(row=3, column=0)

class CreateQuestion(tk.Frame):
    @staticmethod
    def create_question(question: str, difficulty: int, answer: str):
        """Connects to the database to insert the new question"""
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            # insert question
            cursor.execute("INSERT INTO tblQuestion (Question, Difficulty) VALUES (?, ?)", (question, difficulty))
            conn.commit()

            # insert answer
            cursor.execute(f"INSERT INTO tblAnswer (Answer, QuestionID) VALUES ('{answer}', (SELECT QuestionID FROM tblQuestion WHERE Question = '{question}'))")
            conn.commit()

    def __init__(self, container: tk.Frame, app: App):
        super().__init__(container)

        # heading
        tk.Label(self, text="Create Question", font=H1).grid(row=0, column=0)

class App(tk.Tk):
    SCREENS = [MainMenu, CreateAccount, CreateQuestion]

    def __init__(self):
        super().__init__()
        
        self.geometry("680x480")
        self.title("History Quiz")

        # create a container frame
        container = tk.Frame(self)
        container.pack(side="top", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initialise all screens
        self.__screens = {}

        for S in App.SCREENS:
            frame = S(container, self)
            self.__screens[S] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # run the window
        self.set_screen(MainMenu)

    def set_screen(self, screen: tk.Frame):
        frame: tk.Frame = self.__screens[screen]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()