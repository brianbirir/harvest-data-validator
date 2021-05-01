import json


def read_file(file_path: str) -> dict:
    """Reads a file

    Parameters
    ----------
    file_path : str
        path to the file

    Returns
    -------
    dict
        file content as dictionary object
    """
    try:
        with open(file_path, "r") as farm_data_file:
            return json.load(farm_data_file)
    except IOError:
        print("File not found")


def get_measurements_data(file_path: str) -> list:
    """Returns measurements of harvest data

    Parameters
    ----------
    file_path : str
        path to the file

    Returns
    -------
    list
        harvest measurements
    """
    file_content = read_file(file_path)
    measurements_data = file_content["harvest_measurements"]
    return measurements_data
