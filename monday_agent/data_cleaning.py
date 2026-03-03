import pandas as pd
import re

def extract_number(value):
    if value is None:
        return 0
    match = re.search(r'\d+(\.\d+)?', str(value))
    return float(match.group()) if match else 0


def convert_to_dataframe(api_response):
    items = api_response["data"]["boards"][0]["items_page"]["items"]
    rows = []

    for item in items:
        row = {"Item Name": item["name"]}
        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]
        rows.append(row)

    return pd.DataFrame(rows)