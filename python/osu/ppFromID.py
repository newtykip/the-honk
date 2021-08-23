import oppaipy
import requests
import os

# Request information about the beatmap
id = input('Please enter a beatmap ID: ').strip()
beatmap = requests.get('https://osu.ppy.sh/osu/{0}'.format(id)) # Fetch the osu file
open('{0}.osu'.format(id), 'w').write(beatmap.text.replace('\n', '')) # Write this difficulty to the disk
lines = open('{0}.osu'.format(id), 'r').readlines() # Read the lines of the osu file
artist = [x[7:len(x)].strip() for x in lines if x.startswith('Artist:')][0] # Figure out the artist of the song
name = [x[6:len(x)].strip() for x in lines if x.startswith('Title:')][0] # Figure out the name of the song
diff = [x[8:len(x)].strip() for x in lines if x.startswith('Version:')][0] # Figure out the difficulty name
name = '{0} - {1} [{2}]'.format(artist, name, diff) # Put these three together into a parseable format by osu

# Calculate beatmap stats
calc = oppaipy.Calculator() # Create an instance of the pp calculator
calc.set_beatmap('{0}.osu'.format(id)) # Load the newly written difficulty file
calc.calculate() # Calculate the stats
calc.close() # Close the calculator to save resources

# Round beatmap stats to be readable
stars = {
    'total': round(calc.stars, 2),
    'aim': round(calc.aim_stars, 2),
    'speed': round(calc.speed_stars, 2)
}

pp = {
    'total': round(calc.pp, 2),
    'aim': round(calc.aim_pp, 2),
    'speed': round(calc.speed_pp, 2),
    'acc': round(calc.acc_pp, 2)
}

# Output information
print("""
{0} ({1}*)

{2}* Aim
{3}* Speed
{4}pp ({5} aim pp, {6} speed pp, {7} acc pp)
""".format(name, stars['total'], stars['aim'], stars['speed'], pp['total'], pp['aim'], pp['speed'], pp['acc']))

# Cleanup by deleting the written difficulty file afterwards
os.remove('{0}.osu'.format(id))
