#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
    This is a module docstring !
"""
import argparse
import math
import matplotlib.pyplot as plt

def parse():
    """
        Parse file
    """
    parser = argparse.ArgumentParser(description="Extract info from file")
    parser.add_argument("fp", metavar="FILE_NAME", type=open,
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

def extract_data(jug_per_user):
    """
        Extract min, max, average and standard deviation from user dictionnary
    """
    nb_min = 1
    nb_max = 0
    nb_users = 0
    nb_sum = 0
    avg = 0.0
    std_dev = 0.0

    for _, value in jug_per_user.items():
        nb_min = min(nb_min, value)
        nb_max = max(nb_max, value)
        nb_sum += value
        nb_users += 1
    avg = float(nb_sum) / float(nb_users)
    for _, value in jug_per_user.items():
        std_dev += (float(value) - avg) ** 2
    return (avg, math.sqrt(std_dev), nb_min, nb_max, nb_users)


def treat_data(file_name):
    """
        Transfer file to usable data stuctures
    """
    mark = 0
    marks = [0, 0, 0, 0, 0, 0]
    recent = 0
    old = 0
    films = {}
    jug_per_user = {}
    jugment = 0
    date = 0
    user_id = ""

    for line in file_name.fp:
        #Number of jugment
        jugment += 1
        #ID|TITLE|GRADE
        tmp = line.split("|")
        #User ID
        user_id = tmp[0]
        #TITLE (DATE)
        title = tmp[1]
        #Cut the date
        try:
            date = int(tmp[1][-5:-1])
        except ValueError:
            date = old
        #Mark with \n cuted
        mark = int(tmp[2][0:1])
        #Number of marks
        marks[mark] += 1
        #Films dictionnary
        if films.has_key(title):
            films[title] += user_id
        else:
            films[title] = list(user_id)
        #Find the date of the most recent and the oldest films
        if recent is 0:
            recent = date
        if old is 0:
            old = date
        old = min(old, date)
        recent = max(recent, date)
        #Count jugment per user
        if jug_per_user.has_key(user_id):
            jug_per_user[user_id] += 1
        else:
            jug_per_user[user_id] = 1
    return (jugment, films, old, recent, marks, extract_data(jug_per_user))

def main():
    """
        main function
    """
    index = 0
    (jugment, films, old, recent, marks, user_info) = treat_data(parse())
    (avg, std_dev, nb_min, nb_max, nb_users) = user_info

    #Q1
    print("Nombre de jugments : " + str(jugment)
          + "\nNombre d'utilisateurs : " + str(nb_users))
    #Q2
    print("Nombre de films différents : " + str(len(films))
          + "\nLe plus recent date de " + str(recent)
          + "\nLe plus vieux date de " + str(old))
    #Q4
    print("Moyenne : " + str(avg)
          + "\nEcart type : " + str(std_dev)
          + "\nPlus petit nombre de jugements : " + str(nb_min)
          + "\nPlus grand nombre de jugements : " + str(nb_max))
    #Q3
    for nb_note in marks:
        plt.bar(index, nb_note)
        index += 1
    plt.title("Distribution des notes")
    plt.ylabel("Nombre de notes")
    plt.xlabel("Notes")
    plt.grid(True)
    plt.show()

main()
