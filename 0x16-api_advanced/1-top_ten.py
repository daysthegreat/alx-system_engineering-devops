#!/usr/bin/python3
"""A function that print the first 10 hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """ GPrint the titles of the 10 hottest posts on a given subreddit. """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'philsrequest'}
    r = requests.get(url, headers=headers)
    if (r.status_code is 404):
        print("None")
    elif 'data' not in r.json():
        print("None")
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
