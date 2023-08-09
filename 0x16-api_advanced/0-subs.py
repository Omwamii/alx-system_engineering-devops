#!/usr/bin/python3
""" Return number of subscribers for a sub-reddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ return subs if valid subreddit else 0
    """
    req_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    sub_data = requests.get(req_url, headers={'User-agent': 'Uniq 0.1'})
    if sub_data.status_code != 200:
        return 0
    return sub_data.json()['data'].get('subscribers')
