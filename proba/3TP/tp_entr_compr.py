import numpy as np

# taille de la sequence
N = 1000
# proba d'avoir un 1 dans la sequence (loi de Bernouilli)
p = 0.25
# ensemble de lettre
a = ['a', 'b', 'c', 'd']


# coef binomial
def coef_bin(k, n):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


# proba d'avoir k 1
def binom(k, n, p1):
    return coef_bin(k, n) * p1 ** k * (1 - p1) ** (n - k)


# plot de la binomial
def plot_bin(n, p1):
    x = []
    y = []
    for i in range(n):
        x.append(i)
        y.append(binom(i, n, p1))

    f = open("data.d", "w")
    for i in range(n):
        f.write(str(x[i]) + " " + str(y[i]) + "\n")
    f.close()


def plot_code_compress(n, p1):
    cumul_x = 0
    cumul_y = 2 ** n
    x = [0]
    y = [2 ** n]
    for i in range(0, n + 1):
        # on calcul :
        # 1) quel est le coût en proba de retirer toutes les sequences avec i 1
        cout_pr = binom(n - i, n, p1)
        # 2) combien de seq on retire
        nb_seq = coef_bin(n - i, n)

        cumul_x += cout_pr
        cumul_y -= nb_seq

        x.append(cumul_x)
        y.append(cumul_y)

    f = open("data" + str(n) + ".d", "w")
    for i in range(0, n + 1):
        f.write(str(x[i]) + " " + str(np.math.log2(y[i]) / n) + "\n")
    f.close()


def generateseq(p, n):
    msg = ""
    t = np.random.multinomial(1, p, n)
    for line in t:
        i = 0
        for col in line:
            if col > 0:
                msg += a[i]
            i += 1
    return msg

def countfreq(s):
    freq = [0] * len(a)
    for c in s:
        freq[ord(c) % len(a)] += 1
    return(freq)


msg = generateseq([p] * len(a), 10)
print(msg)
print(countfreq(msg))
# plot_bin(100,0.1)
# plot_code_compress(N, p)


