#!/usr/bin/python3
''' Python script that queries Reddit API and returns
no. of subscribers.
'''
import requests


def number_of_subscribers(subreddit):
    ''' Function that returns number of subscribers on a given subreddit. '''
    site = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditClient/1.0'}

    response = requests.get(site, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get('data')
    return result.get('subscribers')
