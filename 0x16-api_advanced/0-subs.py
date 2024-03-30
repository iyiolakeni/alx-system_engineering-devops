#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the URL for the Reddit API
    url = "https://api.reddit.com/r/{}/about".format(subreddit)

    # Set the headers for the API request
    headers = {
        "User-Agent": "MyUserAgent 1.0"
    }

    # Send the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Return the number of subscribers
        return data["subscribers"]

    # If the request was not successful, return 0
    return 0
