MAX = 45
classes = {}

def mean(x):
    return sum(x) / len(x)

def median(x):
    n = len(x)
    i = n // 2
    if n % 2:
        return sorted(x)[i]
    return sum(sorted(x)[i - 1:i + 1]) / 2

# Read the data file
data = open('marks.csv')
lines = data.readlines()

for line in lines:
    # Figure out the name of the class
    lineNumber = lines.index(line) + 1
    className = 'Class ' + str(lineNumber)
    # Parse the csv to figure out the marks for each class
    marks = line.split(',')
    for i in marks:
        index = marks.index(i)
        marks[index] = int(i) # Ensure all of the marks are formatted as integers
    # Ensure that the max amount of marks is not breached
    for i in marks:
        if i > MAX:
            raise Exception('Line/Class {0} contains a mark higher than the max attainable ({1})'.format(str(lineNumber), str(MAX)))
    # Initialise the class dictionary, and assign the marks value
    classes[className] = {}
    classes[className]['marks'] = marks
    # Calculate the mean and median for each class
    classes[className]['mean'] = mean(marks)
    classes[className]['median'] = median(marks)
    # Calculate how many students are above and below the median
    above = 0
    below = 0
    for i in marks:
        if i > classes[className]['median']:
            above += 1
        elif i < classes[className]['median']:
            below += 1
    classes[className]['aboveMedian'] = above
    classes[className]['belowMedian'] = below

# Find the class with the highest mean
allMeans = []

for i in classes:
    allMeans.append(classes[i]['mean']) # Put all of the means into a list

highestMean = max(allMeans) # Find the highest of those means

for i in classes:
    for k, v in classes[i].items():
        if k == 'mean' and v == highestMean: # Find the matching key and value
            highestMean = i # Set the highestMean to the class name

# Find the median across all classes
allMarks = []

for i in classes:
    allMarks += classes[i]['marks'] # Concatenate all marks lists

medianAcross = median(allMarks) # Find the median of that concatenated list

# Output
print('Results!\n-----------')

for i in classes:
    c = classes[i]
    print('{0}:\n\nMean: {1}\nMedian: {2}\nAbove Median: {3}\nBelow Median: {4}\n-----------'.format(i, str(c['mean']), str(c['median']), str(c['aboveMedian']), str(c['belowMedian'])))

print('\nClass with the highest mean mark: {0}\nMedian mark across all classes: {1}'.format(str(highestMean), str(medianAcross)))