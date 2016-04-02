import sys
import click
from click import ClickException
import requests


def print_headers(response):
    for name, value in sorted(response.headers.items()):
        print('{}: {}'.format(name, value))


@click.command()
@click.argument('url')
@click.option('--head', is_flag=True, help='Print headers instead of content')
def main(url, head):
    """A very basic version of curl.

    Examples:

        python geturl.py https://google.com/o
        python geturl.py https://swapi.co/api/people/1 | python -m json.tool

    Example: 
"""
    r = requests.get(url)
    if r.ok:
        if head:
            print_headers(r)
        else:
            print(r.text, end='')
    else:
        raise ClickException('{} {}'.format(r.status_code, r.reason))
        
main()
