"""
"""
import sys
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
            for key, val in sorted(r.headers.items()):
                print('{}: {}'.format(key, val))
        else:
            print(r.text, end='')            
    else:
        print_error('{} {}'.format(r.status_code, r.reason))

main()
