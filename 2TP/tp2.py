#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
    Recognize number
"""
import pickle
import gzip
import numpy as np
import matplotlib.pyplot as plt

# Charge le dataset
with gzip.open("mnist.pkl.gz", "rb") as ifile:
    train_set, valid_set, test_set = pickle.load(ifile, encoding="latin-1")

# Affiche l'image
"""
im = train_set[0][0].reshape(28, 28)
print (len(train_set[0][0]))
plt.imshow(im, plt.cm.gray)
plt.show()
"""
def to_bmp(img, seuil):
    """
    Transforme une image en bitmap
    :param img: image en format standard (float numpy array)
    :param seuil: seuil sur le niveau de gris
    :return: image en bitmap (int numpy array)
    """
    img_dst = np.zeros((len(img),), dtype=np.int)
    cpt = 0

    if seuil < 0.0 or seuil > 1.0:
        raise ValueError("Le seuil doit être un nombre entre 0 et 1")
    for i in img:
        if i > seuil:
            img_dst[cpt] = 1
        cpt += 1
    return (img_dst)

def count_one(t):
    """
    Compte le nombre de 1 dans un tableau
    :param t: un tableau (int numpy array)
    :return: le nombre de 1 contenu dans le tableau
    """
    cpt = 0
    for i in t:
        if i is 1:
            cpt += 1
    return (cpt)

def to_histo(img):
    """
    Transforme une image en son histogramme
    :param img: image reshape en format bitmap (int numpy array)
    :return: histogramme au format standard (int numpy array)
    """
    cpt = 0
    histo = np.empty(len(img), dtype=np.int)
    for l in img:
        histo[cpt] = count_one(l)
        cpt += 1
    return (histo)

#Q1 : La taille de l'image représenté par les niveau de gris
im = to_bmp(train_set[0][0], 0.5)
im = im.reshape(28, 28)
histo = to_histo(im)
for i in range(0, len(histo) - 1):
    plt.bar(i, histo[i])
#plt.imshow(im.reshape(28, 28), plt.cm.gray)
plt.show()