"""
"""
import sys
import pprint
import click
import requests


def print_error(msg):
    print('Error: ' + msg, file=sys.stderr)


@click.command()
@click.argument('url')
@click.option('--head', is_flag=True)
def main(url, head):
    r = requests.get(url)
    if r.ok:
        if head:
            print(dir(r.raw_headers))
        else:
            print(r.text, end='')            
    else:
        print_error('{} {}'.format(r.status_code, r.reason))

main()
