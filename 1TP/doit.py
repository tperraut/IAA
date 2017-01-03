#!/usr/bin/python
"""
    This is a module docstring !
"""
import argparse
def parse():
    """
        Parse file
    """
    parser = argparse.ArgumentParser(description="Extract info from file")
    parser.add_argument("fp", metavar="FILE_NAME", type=file,
                        help="file in csv")
    return parser.parse_args()

def count_jugment(file_name):
    """
        Count jugment in a file
    """
    jugment = 0
    for _ in file_name.fp:
        jugment += 1
    return jugment

def treat_film(file_name):
    """
        Count different film and give the most recent and the oldest
    """
    recent = 0
    old = 0
    film_dico = {}
    #TODO: extract id films date note
    for l in file_name.fp:
        temp = l.split("|")
        

#1
print count_jugment(parse())
