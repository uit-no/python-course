#!/usr/bin/env python
import click
from click import BadParameter
import networkx as nx
import matplotlib.pyplot as plt

# make_graph(text)
def parse_graph(text):
    graph = nx.DiGraph()
    title = None
    edge_labels = {}

    for lineno, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if line == '':
            continue

        if line.startswith('##'):
            label = line.lstrip('#').strip()
        else:
            if '#' in line:
                edge, label = line.split('#', 1)
            else:
                edge = line
                label = None

            a, b = edge.split(':')
            graph.add_node(a)
            graph.add_node(b)
            graph.add_edge(a, b)
            if label:
                edge_labels[(a, b)] = label

    return graph, title, edge_labels


def plot_graph(text):
    graph, title, edge_labels = parse_graph(text)

    if title:
        plt.title(title)
    plt.xkcd()
    plt.axis('off')

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=7000, node_color="white")
    nx.draw_networkx_edges(graph, pos, width=6,alpha=0.5,edge_color='black')
    nx.draw_networkx_labels(graph, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)


@click.command()
@click.argument('files', nargs=-1, type=click.File('rt'))
@click.option('--show', is_flag=True)
def main(files, show):
    for file in files:
        if not file.name.endswith('.graph'):
            raise BadParameter('Input must be .graph file')

        plot_graph(file.read())
        if show:
            plt.show()

        imgfile = file.name.rsplit('.', 1)[0] + '.svg'
        plt.savefig(imgfile)

main()
