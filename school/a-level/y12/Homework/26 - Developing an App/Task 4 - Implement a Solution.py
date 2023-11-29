from __future__ import annotations
import bcrypt
from enum import Enum
import os.path
import tkinter as tk

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.geometry("500x500")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for Frame in (RegisterPage, LoginPage):
			page_name = Frame.__name__
			frame = Frame(container, self)
			self.frames[page_name] = frame

			# stack all of the frames on top of each other
			frame.grid(row=0, column=0, sticky="nsew", padx = 20, pady = 20)

		self.show_frame("RegisterPage")

	def show_frame(self, page_name: str):
		"""Show a frame for the given page name"""
		frame = self.frames[page_name]
		frame.tkraise()

class RegisterPage(tk.Frame):
	def __init__(self, parent: tk.Frame, controller: App):
		super().__init__(parent)
		self.controller = controller

		self.controller.title("Register Page")

		authentication_label = tk.Label(self, text = "Registration", font = ("bold", 20))
		authentication_label.grid(row = 1, column = 1, sticky = "nsew")
		
		username_label = tk.Label(self, text = "Username")
		username_label.grid_configure(row = 2, column = 1, pady = 10)

		username_entry = tk.Entry(self)
		username_entry.grid_configure(row = 2, column = 3)

		password = tk.StringVar()
		password.trace_add("write", lambda *args: print(User.password_strength(password.get()))) # ! test

		password_label = tk.Label(self, text = "Password")
		password_label.grid_configure(row = 3, column = 1, pady = 10)

		password_entry = tk.Entry(self, show = "*", textvariable = password)
		password_entry.grid_configure(row = 3, column = 3)

		confirm_password_label = tk.Label(self, text = "Confirm Password")
		confirm_password_label.grid_configure(row = 4, column = 1, pady = 10)

		confirm_password_entry = tk.Entry(self, show = "*")
		confirm_password_entry.grid_configure(row = 4, column = 3)

		register_button = tk.Button(self, text = "Register", command = lambda: self.register(username_entry.get(), password_entry.get()))
		register_button.grid_configure(row = 5, column = 2, pady = 10)

		goto_login_button = tk.Button(self, text = "Goto Login", command = lambda: self.controller.show_frame("LoginPage"))
		goto_login_button.grid_configure(row = 6, column = 2, pady = 20)

class LoginPage(tk.Frame):
	def __init__(self, parent: tk.Frame, controller: App):
		super().__init__(parent)
		self.controller = controller

		self.controller.title("Login Page")

		authentication_label = tk.Label(self, text = "Registration", font = ("bold", 20))
		authentication_label.grid(row = 1, column = 1, sticky = "nsew")
		
		username_label = tk.Label(self, text = "Username")
		username_label.grid_configure(row = 2, column = 1, pady = 10)

		username_entry = tk.Entry(self)
		username_entry.grid_configure(row = 2, column = 3)

		password_label = tk.Label(self, text = "Password")
		password_label.grid_configure(row = 3, column = 1, pady = 10)

		password_entry = tk.Entry(self, show = "*")
		password_entry.grid_configure(row = 3, column = 3)

		register_button = tk.Button(self, text = "Login", command = lambda: self.register(username_entry.get(), password_entry.get()))
		register_button.grid_configure(row = 5, column = 2, pady = 10)

		goto_register_button = tk.Button(self, text = "Goto Register", command = lambda: self.controller.show_frame("RegisterPage"))
		goto_register_button.grid_configure(row = 6, column = 2, pady = 20)


class UserError(Enum):
	"""UserError class"""
	USER_NOT_FOUND = 1
	INVALID_PASSWORD = 2
	USER_EXISTS = 3

class PasswordStrength(Enum):
	"""PasswordStrength class"""
	INVALID = 0
	WEAK = 1
	MEDIUM = 2
	STRONG = 3
	VERYSTRONG = 4

class User:
	def __init__(self, username: str) -> None:
		"""Initialize the user object"""
		self.__username__ = username

	@staticmethod
	def password_strength(password: str) -> PasswordStrength:
		# https://en.wikipedia.org/wiki/Password_strength#Random_passwords
		# only include ascii characters -> log_2(128) = 7
		score = 0 

		# more than 8 characters
		if len(password) >= 8:
			score += 1
		
		if len(password) >= 12:
			score += 1

		# special characters
		if len(list(filter(lambda x: not (x.isalpha() or x.isdigit()), password))) > 0:
			score += 1

		# lower and upper case
		if len(list(filter(lambda x: x.islower(), password))) > 0 and len(list(filter(lambda x: x.isupper(), password))) > 0:
			score += 1

		return PasswordStrength(score).name

	@staticmethod
	def register(username: str, password: str) -> UserError | None:
		"""Register a user with the given username and password"""
		# read all usernames from file
		with open(f"{SCRIPT_DIR}\\users.txt", "r") as f:
			usernames = [line.split(":")[0] for line in f.readlines()]
		
		# if username already exists, exit with error
		if username in usernames:
			return UserError.USER_EXISTS
			
		# hash password
		salt = bcrypt.gensalt()
		hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

		# write username and hashed password to the file
		with open(f"{SCRIPT_DIR}\\users.txt", "a") as f:
			f.write(f"{username}:{hashed.decode('utf-8')}\n")

	def login(username: str, password: str) -> User | UserError:
		"""Login a user with the given username and password"""
		
		# read all usernames and passwords from file
		with open(f"{SCRIPT_DIR}\\users.txt", "r") as f:
			lines = f.readlines()
			usernames = [line.split(":")[0] for line in lines]
			passwords = [line.split(":")[1].strip() for line in lines]

		# if username does not exist, exit with error
		if username not in usernames:
			return UserError.USER_NOT_FOUND

		# if password is incorrect, exit with error
		if not bcrypt.checkpw(password.encode("utf-8"), passwords[usernames.index(username)].encode("utf-8")):
			return UserError.INVALID_PASSWORD

		# return the user object
		return User(username)
	
	def set_password(self, new_password: str) -> None:
		"""Set a new password for the user"""
		# read all usernames and passwords from file
		with open(f"{SCRIPT_DIR}\\users.txt", "r") as f:
			lines = f.readlines()
			usernames = [line.split(":")[0] for line in lines]
			passwords = [line.split(":")[1].strip() for line in lines]

		# hash new password
		salt = bcrypt.gensalt()
		hashed = bcrypt.hashpw(new_password.encode("utf-8"), salt)

		# update password in file
		passwords[usernames.index(self.__username__)] = hashed.decode("utf-8")
		with open(f"{SCRIPT_DIR}\\users.txt", "w") as f:
			for i in range(len(lines)):
				f.write(f"{usernames[i]}:{passwords[i]}\n")

# ! test, testytest
# user = User.login("test", "testytest")
# print(user)

if __name__ == "__main__":
	app = App()
	app.mainloop()
