# -*- coding: utf-8 -*-
import numpy as np

# Nombre de valeurs
Nv = 400
# Nombre de voisin pour chaque valeur
K = 3
L = 6
Nf = int(Nv * L / K)
M = int(Nv * L)
f_canal = 0.1

RATE = Nv / (Nv + Nf)

print("Graph size", Nv + Nf)
print("Variable nodes", Nv)
print("Fonction nodes", Nf)

np.random.seed(3)

''' Generate the parity matrix
        I have N nodes and M constrains M
        NL == MK
'''


def generate_h(nv, nf, l, k):
    """
    Génère une matrice H pour une message de Nv bits, Nf facteurs de parité.
    Chaque bit sera représenté dans L facteur de parité et chaque facteur de
    parité regardera la somme de K bits.
    :param nv:
    :param nf:
    :param l:
    :param k:
    :return:
    """
    h = np.zeros((nv, nf))
    vnodes = l * np.ones(nv)
    fnodes = k * np.ones(nf)

    lookupv = list(range(0, nv))
    lookupf = list(range(0, nf))

    for v in range(M):
        match = False
        while not match:
            i = np.random.randint(len(lookupv))
            node = lookupv[i]
            a = np.random.randint(len(lookupf))
            fct = lookupf[a]

            if h[node, fct] == 0:
                h[node, fct] = 1
                vnodes[node] -= 1
                fnodes[fct] -= 1
                if vnodes[node] == 0:
                    lookupv.pop(i)
                if fnodes[fct] == 0:
                    lookupf.pop(a)
                match = True
            else:
                match = False

    return h


H = generate_h(Nv, Nf, L, K)

#  Encode a message
f_msg = 0.5
my_msg = np.array((np.random.random(Nv) < f_msg) * 1)
print(len(my_msg))


def encode(msg, h, nv):
    """
    Encode le message à l'aide H et renvoie un message encodé
    :param msg: Message
    :param h: Matrice
    :param nv: Nombre de bit
    :return: Message encodé
    """
    par_msg = msg.dot(h)
    par_msg %= 2
    enc_msg = msg.copy()
    enc_msg.resize(nv + len(par_msg))
    enc_msg[nv:] = par_msg.astype(int)
    return enc_msg.astype(int)


def noisy_canal(enc_msg, f):
    """
    :param enc_msg: Message encodé
    :param f: Facteur de bruit
    :return: Message encodé bruité
    """
    noise = (np.random.random(enc_msg.shape) < f) * 1
    noisy_msg = enc_msg + noise
    noisy_msg %= 2
    return noisy_msg.astype(int)


my_enc_msg = encode(my_msg, H, Nv)
print(len(my_enc_msg))
my_noisy_msg = noisy_canal(my_enc_msg, f_canal)
print("Error encoded=", np.mean((my_enc_msg - my_noisy_msg) ** 2))


def construct_neighbors(h):
    """
    Construit la matrice des voisins pour chaque bits et chaque facteur
    pour la matrice H
    :param h: Marice
    :return: Matrice des voisins
    """
    n_v = []
    n_f = []
    for i in range(Nv):
        n_v.append([a for a in range(Nf) if h[i, a] == 1])
    for a in range(Nf):
        n_f.append([i for i in range(Nv) if h[i, a] == 1])
        n_f[-1].append(Nv + a)  # we add the parity node
    return n_v, n_f


neigh_v, neigh_f = construct_neighbors(H)


def getstates(l):
    """
    Renvoie une liste énumérant tous les 2^L énumérations possibles de L bits
    :param l: Nombre de bits
    :return: Liste des 2^l énumérations
    """
    st = []
    for i in range(2 ** l):
        st.append(list(np.binary_repr(i, l)))
    return np.array(st).astype(int)


def init_biais(noisy_msg, f):
    """

    :return:
    """
    b = []
    for i in noisy_msg:
        if i < 1:
            b += (f, 1 - f)
        else:
            b += (1 - f, f)
    return np.array(b).astype((float, float))


my_biais = init_biais(my_noisy_msg, f_canal)


def init_msg():
    """

    :return:
    """


def update_rmn(src, dst, neigh_src, value_dst):
    """

    :return:
    """
    for i in neigh_src:
        if i != dst:
            return 0


def update_qmn():
    """

    :return:
    """
