#!/usr/bin/python3
""" Return list of hot posts for subreddit
"""
import requests
import uuid


def recurse(subreddit, hot_list=[], after=None):
    req_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    headers = {'User-agent': 'Uniq 1.0'}

    response = requests.get(req_url, params=params, headers=headers)

    if response.status_code != 200:  # subreddit does not exist
        return None

    data = response.json().get('data')
    after = data.get('after')

    def r_pages(subreddit, hot_list, after):
        """ recursively append hot lists
        """
        if after is None:
            return

        req_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        params = {'after': after}
        headers = {'User-agent': 'Uniq 1.0'}
        response = requests.get(req_url, params=params, headers=headers)

        data = response.json().get('data')
        children = data.get('children', [])
        for child in children:
            hot_list.append(child['data']['title'])
        after = data.get('after')
        return r_pages(subreddit, hot_list, after)
    r_pages(subreddit, hot_list, after)
    return hot_list
