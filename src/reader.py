import csv

# One record shape for CSV and JSON. Later milestones transform this data;
# they should not invent a second set of column names.
EXPECTED_FIELDS = [
    "Name",
    "Race",
    "Gender",
    "Power Level",
    "Ki Blast",
    "Melee Combat",
    "Speed",
    "Special Attack",
    "Transformation",
]


def load_csv(file_path):
    characters = []

    try:
        with open(file_path, encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            _require_columns(reader.fieldnames, file_path)

            for line_number, row in enumerate(reader, start=2):
                _validate_power_level(row.get("Power Level"), file_path, line_number)
                characters.append(row)

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")

    except csv.Error as error:
        raise csv.Error(f"Malformed CSV in {file_path}: {error}")

    if len(characters) == 0:
        raise ValueError(f"No characters found in {file_path}")

    return characters


def is_whole_number(value):
    """True for an int or a numeric string. False for bool, because bool is an int subclass."""
    if isinstance(value, bool) or value is None:
        return False
    if isinstance(value, int):
        return True
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("-"):
            text = text[1:]
        return text.isdigit()
    return False


def _require_columns(fieldnames, file_path):
    if not fieldnames:
        raise ValueError(f"No characters found in {file_path}")

    missing = [name for name in EXPECTED_FIELDS if name not in fieldnames]
    if missing:
        raise ValueError(f"Missing columns in {file_path}: {', '.join(missing)}")


def _validate_power_level(power_level, file_path, line_number):
    if not is_whole_number(power_level):
        raise ValueError(
            f"Invalid Power Level in {file_path} on line {line_number}: {power_level!r}"
        )
