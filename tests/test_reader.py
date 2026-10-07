import csv

import pytest

from src.reader import EXPECTED_FIELDS, load_csv

SAMPLE_CSV = "data/dragon_ball_z.csv"


def test_sample_csv_loads_characters():
    characters = load_csv(SAMPLE_CSV)

    assert len(characters) > 0
    assert characters[0]["Name"] == "Goku"
    assert set(EXPECTED_FIELDS).issubset(characters[0])
    assert characters[0]["Power Level"] == "9000"


def test_missing_file_raises(tmp_path):
    missing = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError, match="File not found"):
        load_csv(missing)


def test_empty_file_raises(tmp_path):
    empty = tmp_path / "empty.csv"
    empty.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="No characters found"):
        load_csv(empty)


def test_header_only_file_raises(tmp_path):
    header_only = tmp_path / "header.csv"
    header_only.write_text(",".join(EXPECTED_FIELDS) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="No characters found"):
        load_csv(header_only)


def test_missing_column_raises(tmp_path):
    path = tmp_path / "partial.csv"
    path.write_text("Name,Race\nGoku,Saiyan\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Missing columns"):
        load_csv(path)


def test_non_numeric_power_level_raises(tmp_path):
    header = ",".join(EXPECTED_FIELDS)
    row = "Goku,Saiyan,Male,over 9000,Kamehameha,Dragon Fist,Fast,Spirit Bomb,Super Saiyan"
    path = tmp_path / "bad_power.csv"
    path.write_text(f"{header}\n{row}\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid Power Level"):
        load_csv(path)


def test_malformed_csv_raises(tmp_path):
    # The csv module accepts a lot of messy input. An oversized field is one
    # case it actually rejects with csv.Error.
    header = ",".join(EXPECTED_FIELDS)
    oversized = "x" * (csv.field_size_limit() + 1)
    row = ",".join([oversized, *["ok"] * (len(EXPECTED_FIELDS) - 1)])
    path = tmp_path / "broken.csv"
    path.write_text(f"{header}\n{row}\n", encoding="utf-8")

    with pytest.raises(csv.Error, match="Malformed CSV"):
        load_csv(path)


def test_permission_error_raises(monkeypatch):
    def deny(*args, **kwargs):
        raise PermissionError("denied")

    monkeypatch.setattr("builtins.open", deny)

    with pytest.raises(PermissionError, match="Permission denied"):
        load_csv(SAMPLE_CSV)
