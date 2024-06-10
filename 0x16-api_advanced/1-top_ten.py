#!/usr/bin/python3
"""ueries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    Args:
        subreddit - the specific subreddit
    """
    # make the url
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    # set up header
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # make response
        response = requests.get(url, headers=headers, allow_redirects=False)

        # check response status
        if response.status_code == 200:
            data = response.json()
            # get lists of posts
            posts = data['data']['children']

            # print title of first ten post
            for i in range(min(10, len(posts))):
                print(posts[i]['data']['title'])
        else:
            print(None)  # for invalid subreddit

    except Exception as e:
        print(None)
