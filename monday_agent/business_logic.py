from data_cleaning import extract_number

def compute_pipeline(df, sector):

    if "Sector" not in df.columns:
        return {"error": "Sector column not found"}

    if "Deal Value" not in df.columns:
        return {"error": "Deal Value column not found"}

    df["Sector"] = df["Sector"].str.lower()
    df["Deal Value"] = df["Deal Value"].apply(extract_number)

    filtered = df[df["Sector"] == sector.lower()]

    total = filtered["Deal Value"].sum()
    count = len(filtered)
    avg = total / count if count else 0

    return {
        "total_pipeline_value": total,
        "deal_count": count,
        "average_deal_size": avg
    }