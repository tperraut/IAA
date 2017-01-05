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
    dico = {}
    for line in file_name.fp:
        #ID|TITLE|GRADE
        temp = line.split("|")
        #TITLE (DATE)
        data = temp[1].split("(")
        date = int(data[1][0:4])
        grade = int(temp[2][0:1])
        print temp
        print data
        print date
        print grade
        if dico.has_key(data[0]):
            dico[data[0]] = dico[data[0]].append((temp[0], grade, date))
        else:
            dico[data[0]] = [(temp[0], grade, date)]
        if recent is 0:
            recent = date
        if old is 0:
            old = date
        old = min(old, date)
        recent = max(recent, date)
    return (dico, old, recent)

def main():
    """
        main function
    """
    #1
    print count_jugment(parse())
    #2
    (dico, old, recent) = treat_film(parse())
    print "films: {3}\noldest: {1}\nmost recent: {2}\n".format(old,
                                                               recent,
                                                               len(dico.keys()))

main()
