# read the text file
f = open('user.txt')
r = f.read()

# populate a dictionary with the data
users = {}
for i in r.split('\n'):
    username = i.split(', ')[0]
    password = i.split(', ')[1]
    users[username] = password

# login function
def login(username, password):
    if username in users.keys() and users[username] == password:
        print('Yes!')
    else:
        print('No!')

# password validation
def validatePassword(password):
    errors = []
    password = str(password)
    if len(password) < 8:
        errors.append('Your password is not long enough! It must be a minimum of eight chracters.')
    if any(i.islower() for i in password) == False:
        errors.append('Your password does not include a lower case letter!')
    if any(i.isupper() for i in password) == False:
        errors.append('Your password does not include a upper case letter!')
    print(errors)

validatePassword('hi')
validatePassword('ajsggfhgshjgGFSAFJGFG')
validatePassword('HELLO')