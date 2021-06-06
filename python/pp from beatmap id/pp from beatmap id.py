import oppaipy
import requests
import zipfile
import os
import io

# Request information about the beatmap
id = input('Please enter a beatmap ID: ').strip()
r = requests.get('https://osu.ppy.sh/b/{0}'.format(id)) # Fetch the diff page - redirects to the mapset
setId = r.url[31:len(r.url)-(5+len(id))] # Figure out the ID of the mapset
d = requests.get('https://api.chimu.moe/v1/download/{0}?n=0'.format(setId)) # Try and find the beatmap on chimu - an osu beatmap mirror as the osu API does not have beatmap download support

# Read all of the .osu files and find the correct one for the difficulty
name = ''

with zipfile.ZipFile(io.BytesIO(d.content)) as zip: # Open the fetched osz (beatmap) as a zip
    for zipinfo in zip.infolist(): # For each file
        if zipinfo.filename.endswith('.osu'): # If the file is a .osu (difficulty)
            file = zip.read(zipinfo) # Read the file
            file = file.decode('UTF-8') # Decode it to what it usually would be like
            lines = file.splitlines() # Split the lines
            diffId = [x[10:len(x)].strip() for x in lines if x.startswith('BeatmapID:')][0] # Find the ID of this difficulty
            if diffId == id:
                open('{0}.osu'.format(id), 'w').write(file) # Write this difficulty to the disk
                artist = [x[7:len(x)].strip() for x in lines if x.startswith('Artist:')][0] # Figure out the artist of the song
                name = [x[13:len(x)].strip() for x in lines if x.startswith('TitleUnicode:')][0] # Figure out the name of the song
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