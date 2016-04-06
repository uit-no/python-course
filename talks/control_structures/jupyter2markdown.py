#!/usr/bin/env python3
import json
import click


def gen_markdown_cell(cell):
    yield
    yield '---'
    yield

    yield from cell['source']
    yield


def gen_code_cell(cell):
    yield "```python"
    yield from cell['source']
    yield "```"
    yield
    
@click.command()
@click.argument('markdown_file', type=click.Path(exists=True))
def main(markdown_file):
    notebook = json.load(open(markdown_file))
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            lines = gen_markdown_cell(cell)
        elif cell['cell_type'] == 'code':
            lines = gen_code_cell(cell)
        else:
            oakwoad
            
        for line in lines:
            print((line or '').rstrip())
            

main()
