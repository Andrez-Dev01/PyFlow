import csv

def load_csv(file_path):
    characters = []

    try:
        with open(file_path) as file:
            reader = csv.DictReader(file)

            for row in reader:
                characters.append(row)

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    return characters
