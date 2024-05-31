#!/usr/bin/env python3
import requests, csv, json

def fetch_and_print_posts():
    """
        fetches all post from JSONPlaceholder
    """
    url= "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    posts = response.json()

    print(f"Status Code: {response.status_code}")

    for post in posts:
        print(f"{post['title']}")


def fetch_and_save_posts():
    """
        If the request was sucessfull, instead of printing titles,
        structure the data into a list of dictionaries, where each dictionary
        represents a post with keys and values for id, title, and body.

        Using Python-s csv module, write this data into a CSV file called posts.csv
        with columns corresponding to the dictionary keys.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    posts = response.json()

    data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

    with open('posts.csv', 'w', newline='') as csvfile:
        fieldname = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames= fieldname)

        writer.writeheader()
        writer.writerows(data)