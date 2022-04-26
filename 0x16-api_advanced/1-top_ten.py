#!/usr/bin/python3
""" module """
import requests
import sys


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""

    headers = {'User-Agent': 'product-version-comment'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    par_lim = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=par_lim)

    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
