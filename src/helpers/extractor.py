import os
import json

from src.helpers import logger as app_logger

FILE_TYPES_EXTENSIONS = (".jpg", ".png", ".json")


def fetch_files(folder_path: str) -> list:
    """ Returns files from a folder

    Parameters
    ----------
    folder_path
        path to the folder

    Returns
    -------
        list of found files
    """
    retrieved_files = []

    if not os.path.exists(folder_path):
        raise Exception("Provided data source folder does not exist")
    for subdir, dirs, files in os.walk(folder_path):
        if len(files) == 0:
            raise Exception("No files found")
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(FILE_TYPES_EXTENSIONS):
                retrieved_files.append(filepath)

    app_logger.info("Files retrieved from folder successfully")
    return retrieved_files


def to_json(file: str) -> dict:
    """ Decode json file

    Parameters
    ----------
    file

    Returns
    -------
        data in dictionary structure
    """
    try:
        return json.load(file)
    except ValueError:
        print('Unable to decode JSON file')


def read_file(file_path: str) -> dict:
    """Reads a JSON data file

    Parameters
    ----------
    file_path
        path to the file

    Returns
    -------
        file content as dictionary object
    """
    try:
        with open(file_path, "r") as farm_data_file:
            return farm_data_file
    except IOError:
        print("File not found")


def read_data_file(file_path: str) -> dict:
    """Reads a JSON data file

    Parameters
    ----------
    file_path
        path to the file

    Returns
    -------
        file content as dictionary object
    """
    try:
        with open(file_path, "r") as farm_data_file:
            return json.load(farm_data_file)
    except IOError:
        print("File not found")


def read_image_file(file_path: str) -> object:
    """Reads an image file

    Parameters
    ----------
    file_path
        path to the file

    Returns
    -------
        file content
    """
    try:
        with open(file_path, "r") as farm_data_file:
            if farm_data_file.endswith('.png') or farm_data_file.endswith('.jpeg') or farm_data_file.endswith('.jpg'):
                return farm_data_file
    except IOError:
        print("File not found")


def get_measurements_data(raw_data: dict) -> list:
    """Returns measurements of harvest data

    Parameters
    ----------
    raw_data
        raw data in dictionary format

    Returns
    -------
    list
        harvest measurements
    """
    return raw_data["harvest_measurements"]
