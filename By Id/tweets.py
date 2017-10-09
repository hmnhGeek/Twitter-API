'''
    AUTHOR: Himanshu Sharma
'''
import base64, requests

# defining user credentials.
api_key = 'jettPzQmkvioDiHlwMMkiCe3V'
access_secret = 'bvrxhshi5steYPm4A2LH43Z9BLDoIdwapvC6n7lAHwHSusn5Hj'

# whatever is inside .format(), it is placed in {}.
base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

# converting key proper base64 encoding which is an ASCII encoding only.
key_secret = '{}:{}'.format(api_key, access_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

# headers are key value pairs in the url.
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

# data that you need to POST in the url.
auth_data = {
    'grant_type': 'client_credentials'
}

# Making a POST request and getting the output as JSON.
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
access_token = auth_resp.json()['access_token']

def search(user, count = 1):
    # count implies most recent <count> tweet(s).

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)    
    }

    search_params = {
        'screen_name': user,
        'result_type': 'recent',
        'count': count
    }

    # see documentation as http://developers.twitter.com/ to get to know the url for specific typed of requests.
    search_url = base_url+'1.1/statuses/user_timeline.json'
    response = requests.get(search_url, headers = search_headers, params = search_params)

    tweet_data = response.json()
    
    for tweet in tweet_data:
        print tweet['text']+'\n'
