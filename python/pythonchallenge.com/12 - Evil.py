data = open("evil2.gfx", 'rb').read()
for i in range(5):
    open('{0}.jpg'.format(i), 'wb').write(data[i::5])