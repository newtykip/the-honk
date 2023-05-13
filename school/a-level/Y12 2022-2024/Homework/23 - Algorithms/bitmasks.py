from typing import List, Dict, TypedDict
from enum import IntEnum
from random import choice
import pickle
import bcrypt
import os

class Permissions(IntEnum):
	Read = 1
	Write = 2

class AccountType(TypedDict):
	username: str
	password: str
	permissions: Dict[str, int]

class Account:
	def __init__(self, permissions: Dict[str, int]):
		self.__permissions = permissions

	def __has_permission(self, filename: str, permission: Permissions) -> bool:
		if filename in self.__permissions:
			return self.__permissions[filename] & (1 << (permission - 1)) == permission

		return False
	
	def open_file(self, filename: str) -> str:
		if self.__has_permission(filename, Permissions.Read):
			with open(filename, "r") as file:
				return file.read()
		
		return None
	
	def write_file(self, filename: str, content: str) -> str:
		if self.__has_permission(filename, Permissions.Write):
			with open(filename, "w") as file:
				return file.write(content)
		
		return None

class AuthManager:
	def __init__(self, filename: str = "accounts.pickle"):
		self.__filename = filename
		
		if os.path.exists(filename):
			with open(filename, "rb") as file:
				self.__accounts: List[AccountType] = pickle.load(file)
				dead_files = []

				for i, account in enumerate(self.__accounts):
					for file in account["permissions"]:
						if not os.path.exists(file):
							dead_files.append((i, file))

				for i, file in dead_files:
					del self.__accounts[i]["permissions"][file]
		else:
			self.__accounts = []

	def __save(self):
		with open(self.__filename, "wb") as file:
			pickle.dump(self.__accounts, file)

	def register(self, username: str, password: str):
		for account in self.__accounts:
			if account["username"] == username:
				return

		bytes = password.encode("utf-8")
		salt = bcrypt.gensalt()
		hash = bcrypt.hashpw(bytes, salt)

		self.__accounts.append({
			"username": username,
			"password": hash,
			"permissions": {}
		})

		self.__save()
	
	def login(self, username: str, password: str) -> Account:
		hash = None
		permissions = None

		for account in self.__accounts:
			if account["username"] == username:
				hash = account["password"]
				permissions = account["permissions"]

		if hash is None:
			return None
		elif bcrypt.checkpw(password.encode("utf-8"), hash):
			return Account(permissions)
		else:
			return None
		
	def add_permission(self, username: str, filename: str, permission: Permissions) -> bool:
		if not os.path.exists(filename):
			return False

		foundAccount = False

		for i, account in enumerate(self.__accounts):
			if account["username"] == username:
				foundAccount = True
				break

		if not foundAccount:
			return False
		else:
			if filename in self.__accounts[i]["permissions"]:
				if self.__accounts[i]["permissions"][filename] & (1 << (permission - 1)) == permission:
					return False
				self.__accounts[i]["permissions"][filename] += permission
			else:
				self.__accounts[i]["permissions"][filename] = int(permission)

			self.__save()
			
			return True
		
	def remove_permission(self, username: str, filename: str, permission: Permissions) -> bool:
		foundAccount = False

		for i, account in enumerate(self.__accounts):
			if account["username"] == username:
				foundAccount = True
				break

		if not foundAccount:
			return False
		else:
			if not filename in self.__accounts[i]["permissions"]:
				return False
			elif self.__accounts[i]["permissions"][filename] & (1 << (permission - 1)) != permission:
				return False
			
			self.__accounts[i]["permissions"][filename] -= permission
			self.__save()
			
			return True

auth = AuthManager()
# auth.register("test", "password")
# auth.add_permission("test", "test.txt", Permissions.Read)
# auth.register("test2", "password")
# auth.register("test3", "password")
# auth.add_permission("test3", "test.txt", Permissions.Write)

acc = auth.login("test", "password") # has permission to read
acc2 = auth.login("test2", "password") # does not have any permissions
acc3 = auth.login("test3", "password") # has permission to write

acc3.write_file("test.txt", choice([f"test{i}" for i in range(20)]))

assert acc.open_file("test.txt") is not None
assert acc2.open_file("test.txt") is None
