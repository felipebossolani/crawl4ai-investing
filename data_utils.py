import csv

from models import Index

def save_to_csv(data: list, filename: str):
    if not data:
        print("No data to save.")
        return

    # Get fieldnames from the first item in the data
    fieldnames = ['country', 'name', 'last_value', 'error']

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} indexes to '{filename}'.")
