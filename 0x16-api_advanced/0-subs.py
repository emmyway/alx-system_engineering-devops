#!/usr/bin/python3
"""Script request a reddit api """
import requests


def number_of_subscribers(subreddit):
    """
    fxn queries the api
    Args:
        subreddit - the required subreddit
    Returns: number of subscibers on success else 0
    """
    # URL to get information about the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # set up the header
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # make the api request
        response = requests.get(url, headers=headers, allow_redirects=False)

        # check if the subreddit is valid by checking the status code
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            return 0  # if subreddt is invalid
    except Exception as e:
        return 0
