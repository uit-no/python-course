import click
from click import ClickException, BadParameter
import requests


def get_name(num):
    """Get name of character.

    Returns None if the character was not found.
    """
    r = requests.get('https://swapi.co/api/people/{:d}'.format(num))
    if r.status_code == 404:
        return None
    else:
        r.raise_for_status()
        return r.json()['name']       


@click.command()  # description='Get character names from Star Wars API')
@click.argument('num', type=int, required=True)
def main(num):
    """Get character names from Star Wars API. (https://swapi.co/)"""
    if num <= 0:
        raise BadParameter('Numbers start at 0')
    
    name = get_name(num)
    if name is None:
        raise ClickException('No person {}'.format(num))
    else:
        print(name)


main()
