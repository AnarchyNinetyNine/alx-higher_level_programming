#!/usr/bin/python3

"""
    This script lists 10 commits (from the most recent to oldest)
    of a repository by a specified owner, using the GitHub API.
"""


import sys
import requests


if __name__ == "__main__":

    # GitHub repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint for repository commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        # Send GET request to GitHub API
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            commits = response.json()

            # Print the sha and author name of the last 10 commits
            for commit in commits[:10]:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            # Print an error message if request was not successful
            print("Unable to fatch commits")

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions
        print(f"Error: {e}")
