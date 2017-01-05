#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Code de répétition
"""
import random
import pbm

def duplic(pattern, rep):
    """
        Renvoie le message répété.
    """
    msg = ""
    for char in pattern:
        for _ in range(0, rep):
            msg = msg + str(char)
    return msg

def inverse(char):
    """
        Inverse un booléen
    """
    if char is '0':
        return '1'
    else:
        return '0'

def canal(msg, proba):
    """
        Renvoie le message une fois passé par le canal bruité.
    """
    random.seed(42)
    new_msg = ""

    for char in msg:
        if random.random() > proba:
            new_msg = new_msg + char
        else:
            new_msg = new_msg + inverse(char)
    return new_msg

def decod(msg, rep):
    """
        Décode le message bruité
    """
    msg_decod = ""
    cpt = 0
    choice = 0

    for char in msg:
        cpt += 1
        if char is '1':
            choice += 1
        else:
            choice -= 1
        if cpt is rep:
            if choice is 0:
                msg_decod += str(int(random.uniform(0.0, 2.0)) % 2)
            if choice < 0:
                msg_decod += '0'
            else:
                msg_decod += '1'
            choice = 0
            cpt = 0
    return msg_decod

def main():
    """
        Main function
    """
    #Q1
    msg = duplic([1, 1, 1], 1)
    print msg
    #Q2
    msg_new = canal(msg, 0.8)
    print msg_new
    #Q3
    print decod(msg_new, 1)
    #Q4
    im, x, y, t = pbm.readpbm("calvin.pbm")
    msg = duplic(im, 11)
    msg_new = canal(msg, 0.2)
    msg_decod = decod(msg_new, 11)
    pbm.writepbm("out.pbm", x, y, msg_decod)

main()
