import json

from src.reader import EXPECTED_FIELDS, is_whole_number


def load_json(file_path):
    try:
        with open(file_path, encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
    except json.JSONDecodeError as error:
        raise ValueError(f"Malformed JSON in {file_path}: {error}") from error

    validate_records(records, file_path)
    return records


def write_json(file_path, records):
    validate_records(records, file_path)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)
        file.write("\n")


def validate_records(records, source):
    if not isinstance(records, list):
        raise ValueError(f"Expected a list of records in {source}")

    if len(records) == 0:
        raise ValueError(f"No characters found in {source}")

    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Record {index} in {source} is not an object")

        missing = [field for field in EXPECTED_FIELDS if field not in record]
        if missing:
            raise ValueError(
                f"Record {index} in {source} is missing fields: {', '.join(missing)}"
            )

        if not is_whole_number(record["Power Level"]):
            raise ValueError(
                f"Record {index} in {source} has an invalid Power Level: {record['Power Level']!r}"
            )
