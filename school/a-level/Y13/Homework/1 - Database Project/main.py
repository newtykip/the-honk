import sqlite3

DB_NAME = "histQuiz.db"

def create_user(username: str, password: str):
	"""Connects to the database to insert the new player"""
	with sqlite3.connect(DB_NAME) as conn:
		cursor = conn.cursor()
		cursor.execute("INSERT INTO tblPlayer (Username, Password) VALUES (?, ?)", (username, password))
		conn.commit()

def check_password(password: str) -> bool:
	"""Checks the password for length and complexity"""
	if len(password) < 8:
		print("Password must be 8 characters or longer")
		return False

	if not any(c.islower() for c in password):
		print("Password must contain at least one lowercase letter")
		return False

	if not any(c.isnumeric() for c in password):
		print("Password must contain at least one number")
		return False

	if not any(not c.isalnum() for c in password):
		print("Password must contain at least one special character")
		return False

	return True

def input_player():
	"""Handles user input of a new player with basic validation of answer length and difficulty"""
	# get the player's username
	while True:
		username = input("Please enter your username: ").lower()
		
		if len(username) > 5:
			break
		else:
			print("Username must be 6 characters or longer")
	
	# get the player's password
	while True:
		password = input("Please enter your password: ")
		pass_ok = check_password(password)

		if pass_ok:
			try:
				create_user(username, password)
				break
			except Exception as err:
				print(err)
				print("Something went wrong with the database")

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

def input_question():
	"""Handles user input of new questions with basic validation of answer length and difficulty"""
	question = input("Please enter the question: ")
	answer = input("Please enter the answer: ")

	while True:
		try:
			difficulty = int(input("Please enter the difficulty (1-3): "))
		except ValueError:
			print("Please enter a valid integer")
		
		if difficulty < 1 or difficulty > 3:
			print("Please enter a valid difficulty")
		else:
			break

	try:
		create_question(question, difficulty, answer)
	except:
		print("Something went wrong with the database")

if __name__ == "__main__":
	# choose a function
	print("""Welcome to the Hisotry Quiz!

1. Play
2. Create a new account
3. Quit""")
	
	while True:
		try:
			choice = int(input("\nEnter your choice: "))
		except ValueError:
			print("Please enter a valid integer")

		if choice < 1 or choice > 3:
			print("Please enter a valid choice")
		else:
			break

	if choice == 1:
		pass
	elif choice == 2:
		input_player()
	elif choice == 3:
		exit()
