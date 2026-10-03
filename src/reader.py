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

    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")

    except csv.Error as e:
        raise csv.Error(f"Malformed CSV in {file_path}: {e}")

    return characters
