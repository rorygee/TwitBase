
# coding: utf-8

# In[6]:

import twython

from twython import Twython
ConsumerKey = 'DHvPpUKNhPBqmOoWHTioL8R8g'
ConsumerSecret = 'HaCvbsQLXy61rdxbs1AuojrP0y9eunUQLYfzyzt3gOzek1BdkC'
AccessToken = '2723648388-vUN5LPJCXUyM2juD5dVGegyX02gwjwOT66LisIe'
AccessTokenSecret = 'Wfu5QgkHiLqdaPF7t3AcM3XCihVpxUJbrUk4dkKBjJCcZ'
twitter = Twython(ConsumerKey,ConsumerSecret,AccessToken,AccessTokenSecret)

print('What would you like to do?')
print('\nTo search for a specific tweet, press \'T\'')
print('To search for a Twitter profile, press \'P\'')
print('To search for the trends in a location, press \'L\'')
      
MenuChoice = input('What choice will you make: ')
#MenuChoice.upper()

if MenuChoice == 't':
    print
    SearchWord = input('Enter the word you wish to search for: ')
    result = twitter.search(q = SearchWord)
    for status in result['statuses']:
        print('\nuser: {0} \ntext: {1}'.format(status['user']['name'],status['text']))
        
elif MenuChoice == 'p':
    Username = input('What username would you like tos search for: ')
    TweetNo = int(input('Please enter the number of tweets you wish to view: '))
    
    tl = twitter.get_user_timeline(screen_name = Username, count = TweetNo)
    for tweet in tl:
        print('user {0} \nCreated: {1} \nText: {2}'.format(tweet['user']['name'],tweet['created_at'],tweet['text']))

elif MenuChoice == 'l':
    GeoID = int(input('Please enter the WOEID code of the location you wish to search for: '))
    id = (GeoID)
    result = twitter.get_place_trends(id = GeoID )
    if result:
        for trend in result[0].get('trends',[]):
            print('{0} \n'.format(trend['name']))
    


# In[ ]:



