import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MONDAY_API_KEY")
URL = "https://api.monday.com/v2"

def run_query(query):
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(URL, json={"query": query}, headers=headers)

    if response.status_code != 200:
        raise Exception(response.text)

    return response.json()


def get_board_items(board_id):
    query = f"""
    query {{
        boards(ids: {board_id}) {{
            items_page {{
                items {{
                    name
                    column_values {{
                        column {{
                            title
                        }}
                        text
                    }}
                }}
            }}
        }}
    }}
    """
    return run_query(query)