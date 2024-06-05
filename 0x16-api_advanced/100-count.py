#!/usr/bin/python3
""" Recursively require the reddit api, and output
sorted count of given keyword
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, count={}):
    """ Recursively queries the Reddit API, parse the titles of hot articles,
    and prints a sorted count of given keywords.
    Args:
        subreddit (str): The required subreddit name.
        word_list (list): list of keywords to count.
        hot_list (list): List to store titles of hot articles
        after (str): The 'after paramete for pegination
        counts (dict): Dictionary to store counts of keywords
    Returns:
        None
    """
    # make the url
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # st up headers to make the rquest
    headers = {'User-Agent': 'Mozilla/5.0'}

    # ste up parameter for pagination
    params = {'after': after} if after else {}

    try:
        # make request
        response = requests.get(url, headers=headers, params=params, allow_redirection=False)
        # check subreddit validity
        if response.status_code != 200:
            return

        # parse the JSON
        data = response.json()

        # Extract the list of posts
        posts = data['data']['children']


        # Add the titles of the current page to the hot_list
        for post in posts:
            hot_list.append(post['data']['title'].lower())

        # update keyword counts
        for title in hot_list:
            words = title.split()
            for word in words:
                cleaned_word = word.lower().strip('.,!?;:')
                if cleaned_word in counts:
                    counts[cleaned_word] = +1
                elif cleaned_word in word_list:
                    counts[cleaned_word] = 1

        # Get the 'after' value for the next page
        after = data['data']['after']

        # Base case: nomore pages
        if not after:

            # process and print the counts
            sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return

        # Recursive case: more pages to fetch
        return count_words(subreddit, word_list, hot_list, after, counts)

    except Exception as e:
        return
