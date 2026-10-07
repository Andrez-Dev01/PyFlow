import json

import pytest

from src.json_handler import load_json, write_json
from src.reader import EXPECTED_FIELDS


def character(**overrides):
    record = {
        "Name": "Goku",
        "Race": "Saiyan",
        "Gender": "Male",
        "Power Level": 9000,
        "Ki Blast": "Kamehameha",
        "Melee Combat": "Dragon Fist",
        "Speed": "Fast",
        "Special Attack": "Spirit Bomb",
        "Transformation": "Super Saiyan",
    }
    record.update(overrides)
    return record


def test_write_then_load_round_trip(tmp_path):
    path = tmp_path / "characters.json"
    records = [character(), character(Name="Vegeta", **{"Power Level": "8500"})]

    write_json(path, records)
    loaded = load_json(path)

    assert loaded == records
    assert set(EXPECTED_FIELDS).issubset(loaded[0])


def test_missing_json_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError, match="File not found"):
        load_json(tmp_path / "missing.json")


def test_malformed_json_raises(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{not json", encoding="utf-8")

    with pytest.raises(ValueError, match="Malformed JSON"):
        load_json(path)


def test_json_object_instead_of_list_raises(tmp_path):
    path = tmp_path / "object.json"
    path.write_text(json.dumps(character()), encoding="utf-8")

    with pytest.raises(ValueError, match="Expected a list of records"):
        load_json(path)


def test_empty_json_list_raises(tmp_path):
    path = tmp_path / "empty.json"
    path.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError, match="No characters found"):
        load_json(path)


def test_missing_field_raises(tmp_path):
    path = tmp_path / "partial.json"
    record = character()
    del record["Race"]
    path.write_text(json.dumps([record]), encoding="utf-8")

    with pytest.raises(ValueError, match="missing fields: Race"):
        load_json(path)


def test_invalid_power_level_raises(tmp_path):
    path = tmp_path / "bad_power.json"
    path.write_text(json.dumps([character(**{"Power Level": "over 9000"})]), encoding="utf-8")

    with pytest.raises(ValueError, match="invalid Power Level"):
        load_json(path)


def test_boolean_power_level_is_rejected(tmp_path):
    path = tmp_path / "bool_power.json"
    path.write_text(json.dumps([character(**{"Power Level": True})]), encoding="utf-8")

    with pytest.raises(ValueError, match="invalid Power Level"):
        load_json(path)


def test_write_rejects_invalid_records_without_creating_a_file(tmp_path):
    path = tmp_path / "rejected.json"

    with pytest.raises(ValueError, match="missing fields"):
        write_json(path, [{"Name": "Goku"}])

    assert not path.exists()


def test_permission_error_raises(monkeypatch):
    def deny(*args, **kwargs):
        raise PermissionError("denied")

    monkeypatch.setattr("builtins.open", deny)

    with pytest.raises(PermissionError, match="Permission denied"):
        load_json("characters.json")
