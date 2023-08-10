#!/usr/bin/python3
"""Module to return count of keywords in hot posts
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """ Parse list of hot posts and return count of certain keywords
    """
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Ubuntu.20.04:alx.advanced.api:v1.0 (by /u/sk001)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(URL, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for k in results.get("children"):
        title = k.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([i for i in title if i == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda keyval: (-keyval[1],
                                                                  keyval[0]))
        [print("{}: {}".format(key, val)) for key, val in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
