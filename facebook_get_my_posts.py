# Chap04/facebook_get_my_posts.py
import os
import json
import facebook
import my_api_token
import requests
if __name__ == '__main__':
    token = my_api_token.tkn
    graph = facebook.GraphAPI(token)
    posts = graph.get_connections('me', 'posts')
    while True: # keep paginating
        try:
            with open('my_posts.jsonl', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                    posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # no more pages, break the loop
            break
