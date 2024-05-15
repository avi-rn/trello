# Trello.py

Trello.py is a command line interface (CLI) python script to create cards for trello.com boards.
I estimate it took around 4 hours to work on this.

# Environment Variables

Create a .env file with your API_KEY and API_TOKEN variables. These can be generated following this https://trello.com/app-key.

API_KEY = ''
API_TOKEN = ''

## Usage

python trello.py 

--label_name {str list of label names} 
--label_colors {str list of label colors} 
--comment {str} 
--column {str column / list to add the card to} 
--create_board {True if you need a board created, else skip this variable}
--board {board id if you already have a Trello board}

Example 1: 

python trello.py --label_names ToDo Doing --label_colors green yellow --column testlist --board {boardId} --comment test

Example 2:

python trello.py --label_names label --label_colors green --column testlist --create_board True --comment test

## Dependencies

This script uses the argparse and requests modules.

## Next Steps

I would create unit tests for each function within the script i.e. create_card(), create_board(), etc. using the pytest module. I would also explore adding functionality to delete and move existing cards on the Trello board. Additionally, for a production environment I would look for a secure way to store the
API keys and tokens.