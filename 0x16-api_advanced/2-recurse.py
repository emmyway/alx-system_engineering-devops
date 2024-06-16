#!/usr/bin/python3
"""Script to request reddit API"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    function queries the reddt API and returns the number a list of titles of all hot articles for a given subreddit.
    Args:
        sureddit (str): The required subreddit name
        hot_list (list): list to store titles of hot articles
        after (str): The 'after' parameter for pagination.
    Returns:
        list: List of titles if successful, otherwise none
    """
    if hot_list is None:
        hot_list = []
    # make the URL 
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # set up the header
    headers = {'User-Agent': 'Mozilla/5.0'}

    # set up parameters for pagination
    params = {'after': after} if after else {}


    try:
        # make the API request
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        # check if the subreddit is valid by checking the status code
        if response.status_code != 200:
            return None

        # parse the JSON response
        data = response.json()
        
        # Extract the list of posts
        posts = data['data']['children']

        # Add the title of the current page to the hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Get the 'after' value for the next page
        after = data['data']['after']

        # Basee case: no more pages
        if not after:
            return hot_list

        # recursive case: more paes to fetch
        return recurse(subreddit, hot_list, after)

    except Exception as e:
        return None
