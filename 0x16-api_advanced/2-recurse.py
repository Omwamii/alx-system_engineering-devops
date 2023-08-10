#!/usr/bin/python3
""" module to find all hot posts of subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Fn that that returns list of hot posts for subreddit
       Point: pagination used to recursively get data
    """
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
               "User-Agent": "Ubuntu.20.04:alx.advanced.api:v1.0 (by /u/sk001)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 50
    }

    response = requests.get(URL, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for k in results.get("children"):
        hot_list.append(k.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
