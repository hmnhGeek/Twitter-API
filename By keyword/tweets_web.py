'''
    AUTHOR: Himanshu Sharma
'''
import urllib2, json, base64, requests

# User credentials here. To be kept secret.
api_key = 'jettPzQmkvioDiHlwMMkiCe3V'
access_secret = 'bvrxhshi5steYPm4A2LH43Z9BLDoIdwapvC6n7lAHwHSusn5Hj'

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

# encodes key in base64 which is an ascii encoding only.
key_secret = '{}:{}'.format(api_key, access_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

# headers are key value pairs in the url.
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

# Make a POST request to the API to authenticate.
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
access_token = auth_resp.json()['access_token']

def search(keyword, count = 1):

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)    
    }

    search_params = {
        'q': keyword,
        'result_type': 'recent',
        'count': count
    }

    # refer https://developers.twitter.com/ for more information regarding tweets using specific params.
    search_url = base_url+'1.1/search/tweets.json'
    response = requests.get(search_url, headers = search_headers, params = search_params)

    tweet_data = response.json()

    for tweet in tweet_data['statuses']:
        print tweet['text'] + '\n'
