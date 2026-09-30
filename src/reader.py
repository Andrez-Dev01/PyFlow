import csv

def load_csv(file_path):
    characters = []

    with open(file_path) as file:
        reader = csv.DictReader(file)

        for row in reader:
            characters.append(row)

    return characters
