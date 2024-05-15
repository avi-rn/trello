import argparse
from dotenv import load_dotenv
import os
import requests

def parse_args():
    parser = argparse.ArgumentParser("Trello Card CLI")
    parser.add_argument("--label_names", nargs="+", help="User inputted label names", type=str)
    parser.add_argument("--label_colors", nargs="+", help="User inputted label colors", type=str)
    parser.add_argument("--comment", help="User inputted comment", type=str)
    parser.add_argument("--column", help="User inputted column", type=str)
    parser.add_argument("--create_board", help="True if user needs board to be created, False if they have a board created", type=bool)
    parser.add_argument("--board", help="Board ID", type=str)
    

    args = parser.parse_args()

    return args

# Create labels
def create_labels(label_names, label_colors, board, api_key, api_token):

    url = "https://api.trello.com/1/labels"

    labels = []

    for names, colors in zip(label_names, label_colors):

        query = {
        'name': names,
        'color': colors,
        'idBoard': board,
        'key': api_key,
        'token': api_token,
        }

        response = requests.request(
        "POST",
        url,
        params=query
        )

        label_id = response.json()["id"]

        labels.append(label_id)

    return labels

def create_board(api_key, api_token):
    url = "https://api.trello.com/1/boards/"

    query = {
    'name': "test board",
    'key': api_key,
    'token': api_token
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )

    #print(response.text)

    if response.status_code == 200:

        data = response.json()

        board_id = data["id"]

        return board_id
    
    else:
        print("Error:", response.text)

# Create a list

def create_list(board, column, api_key, api_token):

    url = "https://api.trello.com/1/lists"

    query = {
    'name': column,
    'idBoard': board,
    'key': api_key,
    'token': api_token
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )

    if response.status_code == 200:

        data = response.json()

        list_id = data["id"]

        return list_id
    
    else:
        print("Error:", response.text)




def create_card(column, labels, comment, api_key, api_token):
    url = "https://api.trello.com/1/cards"

    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': column,
    'idLabels': labels,
    'key':  api_key,
    'token': api_token
    }

    response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
    )

    if response.status_code == 200:

        resp_json = response.json()

        id = resp_json["id"]

        print("Card created successfully!")
    
    else:
        print("Error:", response.text)

    comment_url = url + "/" + id + "/actions/comments"

    comment_query = {
    'text': comment,
    'key': api_key,
    'token': api_token
    }

    comment_response = requests.request(
    "POST",
    comment_url,
    headers=headers,
    params=comment_query
    )


    if comment_response.status_code == 200:

        print("Comment created successfully!")
    
    else:
        print("Error:", response.text)


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    try:
        api_key = os.environ.get("API_KEY")
        api_token = os.environ.get("API_TOKEN")
    except KeyError as e:
        print(f"Error: Missing environment variable: {e}")
        return

    args = parse_args()

    if args.create_board:

        board = create_board(api_key, api_token)

    else:
        board = args.board

    column = create_list(board, args.column, api_key, api_token)

    labels = create_labels(args.label_names, args.label_colors, board, api_key, api_token)

    create_card(column, labels, args.comment, api_key, api_token)



if __name__ == "__main__":
    main()