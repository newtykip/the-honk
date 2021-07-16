from twitter import Account
from datetime import datetime
from locale import format, setlocale, LC_ALL
from statistics import stdev

barrack = Account('BarackObama.txt')
swift = Account('taylorswift13.txt')
formatNum = lambda x: format('%d', x, grouping=True)
setlocale(LC_ALL, 'en_US')

def profileStats(profile):
  meanLikes = round(profile.totalLikes / len(profile._tweets), 2)
  meanRetweets = round(profile.totalRetweets / len(profile._tweets), 2)
  likes = [tweet.likes for tweet in profile._tweets]
  retweets = [tweet.retweets for tweet in profile._tweets]
  stdevLikes = round(stdev(likes), 2)
  stdevRetweets = round(stdev(retweets), 2)
  return (profile.totalLikes, profile.totalRetweets, meanLikes, meanRetweets, stdevLikes, stdevRetweets)
  
def tweetStats(profile, tweet):
  dateValues = [int(x) for x in tweet.date_time.split(' ')[0].split('-')]
  timeValues = [int(x) for x in tweet.date_time.split(' ')[1].split(':')]
  date = datetime(dateValues[0], dateValues[1], dateValues[2], timeValues[0], timeValues[1], timeValues[2])
  dateStr = date.strftime('%A %d %B, %Y at %I:%M %p')
  likePercent = '{0}%'.format(round((tweet.likes / profile.totalLikes) * 100, 2))
  retweetPercent = '{0}%'.format(round((tweet.retweets / profile.totalRetweets) * 100, 2))
  return (formatNum(tweet.likes), likePercent, formatNum(tweet.retweets), retweetPercent, dateStr, tweet.text)

for profile in [barrack, swift]:
  print('----------------------------------\n%s\'s tweets!' % (profile.handle))
  print('Total Likes: %s\nTotal Retweets: %s\nMean Likes: %s\nMean Retweets: %s\nStandard Deviation of Likes: %s\nStandard Deviation of Retweets: %s\n\n' % profileStats(profile))
  for tweet in profile:
    if tweet.text == '':
      tweet.text = '<Retweet>'
    if tweet.likes >= 500000:
      print('Likes: %s (%s) Retweets: %s (%s)\nPosted at: %s\nContent: %s\n\n' % tweetStats(profile, tweet))
      
barrackStats = profileStats(barrack)
swiftStats = profileStats(swift)
print('----------------------------------\n')
print('Who gets the most likes? %s' % ('Barrack Obama' if barrackStats[2] > swiftStats[2] else 'Taylor Swift'))
print('Who gets the most retweets? %s' % ('Barrack Obama' if barrackStats[3] > swiftStats[3] else 'Taylor Swift'))
