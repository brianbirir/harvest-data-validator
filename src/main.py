import pprint

import click

from src.validator import Validator
from src.helpers.extractor import fetch_files, read_data_file, get_measurements_data


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo("Hello %s!" % name)


@click.command()
@click.option(
    "--folder", required=True, help="Folder path containing harvest data", type=str
)
def validate_harvest(folder):
    """Validates harvest data"""
    fetched_files = fetch_files(folder_path=folder)

    for f in fetched_files:
        if f.endswith(".json"):
            raw_harvest_data = read_data_file(f)
            harvest_data = get_measurements_data(raw_harvest_data)

            validator_obj = Validator(data=harvest_data)

            print(validator_obj.multiple_crop_measurements())
            print(validator_obj.validate_dry_weight())
            print(validator_obj.validate_weight())
