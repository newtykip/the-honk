import xmlrpc.client

connection = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(connection.system.listMethods()) # methods
print(connection.system.methodHelp('phone')) # what does phone do?
print(connection.system.methodSignature('phone')) # takes a string, returns a string
print(connection.phone('Bert')) # italy!!!
