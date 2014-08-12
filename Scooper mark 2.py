
# coding: utf-8

# In[23]:

from twython import TwythonStreamer
from twython import Twython
App_Key = 'DHvPpUKNhPBqmOoWHTioL8R8g'
App_Secret = 'HaCvbsQLXy61rdxbs1AuojrP0y9eunUQLYfzyzt3gOzek1BdkC'
Oauth_Token = '2723648388-vUN5LPJCXUyM2juD5dVGegyX02gwjwOT66LisIe'
Oauth_Token_Secret = 'Wfu5QgkHiLqdaPF7t3AcM3XCihVpxUJbrUk4dkKBjJCcZ'
astrack = 'Milton Keynes'
follow = 'rorygee,scoopdogg3'
delimited = 15

twitter = Twython(App_Key,App_Secret,Oauth_Token,Oauth_Token_Secret)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):        
        if 'text' in data:
            filter(track,follow)
            print (data['text'])#.encode('utf-8'))

            def on_error(self, status_code, data):
                print (status_code)
                

stream = MyStreamer(App_Key,App_Secret,Oauth_Token,Oauth_Token_Secret)
stream.statuses.filter(track='twitter')


# In[6]:



