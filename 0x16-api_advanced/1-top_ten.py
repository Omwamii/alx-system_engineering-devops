#!/usr/bin/python3
""" Return number of subscribers for a sub-reddit
"""
import requests


def top_ten(subreddit):
    """ print top ten posts of subred if valid else None
    """
    req_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    sub_data = requests.get(req_url, headers={'User-agent': 'Uniq 0.1'})
    if sub_data.status_code != 200:
        return print(None)
    else:
        hot = 0
        for post in sub_data.json()['data']['children']:
            if hot > 9:
                break
            print(post['data']['title'])
            hot += 1
