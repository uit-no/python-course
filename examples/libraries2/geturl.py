"""
"""
import sys
import click
import requests


def print_error(msg):
    print('Error: ' + msg, file=sys.stderr)


@click.command()
@click.argument('url')
def main(url):
    r = requests.get(url)
    if r.ok:
        print(r.text, end='')            
    else:
        print_error('{} {}'.format(r.status_code, r.reason))

        
main()
