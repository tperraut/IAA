# coding=utf-8
import random


class QLearn:
    def __init__(self, actions, epsilon=0.1, alpha=0.2, gamma=0.9):
        self.q = {}  #  dictionnaire : (état, action) -> reward

        self.epsilon = epsilon  # paramètre pour espilon-greedy
        self.alpha = alpha  #  poids des actions nouvelles
        self.gamma = gamma  # paramètre pour la propagation des gains
        self.actions = actions  # possibles actions (8 mvts)

    def chooseAction(self, state):
        imax = []
        if random.random() < self.epsilon:
            return random.randint(0, 7)
        else:
            max = self.q.get((state, random.randint(0, 7)), 0)
            for a in self.actions:
                tmp = self.q.get((state, a), 0)
                if tmp > max:
                    max = tmp
                    imax = [a]
                elif tmp == max:
                    imax.append(a)
        return (imax[random.randint(0, len(imax) - 1)])

    def updateLearn(self, last_state, last_action, state, reward):
        max = self.q.get((state, random.randint(0, 7)), 0)
        for a in self.actions:
            tmp = self.q.get((state, a), 0)
            if tmp > max:
                max = tmp
        self.q[(last_state, last_action)] = self.q.get((last_state, last_action), 0) + self.alpha * (
        reward + max - self.q.get((last_state, last_action), 0))
