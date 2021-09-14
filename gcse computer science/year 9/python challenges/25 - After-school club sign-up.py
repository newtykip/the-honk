import uuid

# ask for the information
firstName = input('What is your first name?')
lastName = input('What is your last name?')
gender = input('What is your gender?')
form = input('What is your form?')

# save the information in a file
f = open('registration-' + str(uuid.uuid1()) + '.txt', 'x')

f.write('Name: ' + firstName + ' ' + lastName)
f.write('\nGender: ' + gender)
f.write('\nForm: ' + form)

f.close()
print('Written to file.')