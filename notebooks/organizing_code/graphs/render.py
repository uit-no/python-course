#!/usr/bin/env python3
import click
from click import BadParameter
from subprocess import check_call as run

@click.command()
@click.argument('dotfiles', nargs=-1, type=click.Path(exists=True))
def main(dotfiles):
    for dot in dotfiles:
        if not dot.endswith('.dot'):
            raise BadParameter('Not a .dot file: {!r}'.format(dot))

        svg = dot[:-4] + '.svg'
        run(['dot', '-Tsvg', '-o', svg, dot])

main()

