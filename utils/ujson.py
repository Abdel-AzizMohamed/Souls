"""Contains tools to work with json files"""

import json


def read_json(file_path: str) -> dict:
    """
    Read Json file data

    Arguments:
        file_path: Given json file path

    Returns:
        Given file data
    """
    with open(file_path, encoding="utf-8") as file:
        json_data = json.load(file)

    return json_data


def write_json(file_path: str, json_data: dict) -> None:
    """
    Write data to json file (overwrite the current data!!)

    Arguments:
        file_path: Given json file path
        json_data: data to write into json file
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2)


def append_json(file_path: str, new_data: dict) -> None:
    """
    Append data to json file

    Arguments:
        file_path: Given json file path
        new_data: data to append it
    """
    json_data = read_json(file_path)
    for key, value in new_data.items():
        json_data[key] = value
    write_json(file_path, json_data)
