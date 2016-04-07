"""
Unfinished code of refactored version.

As is, this is an example of how to you can read a CSV file as dictionaries.
"""
import csv


def read_animals(filename):  
    """Read animals from CSV file and return as a list of dictionaries."""
    with open(filename) as csvfile:
        yield from csv.DictReader(csvfile, delimiter=';')


def main():
    """Read animal list from CSV file and print report for farm inspector."""
    # Todo: file name should come from command line.
    # Just print animals for now.
    for animal in read_animals('animals.csv'):
        print(animal)

    

if __name__ == '__main__':
    main()
