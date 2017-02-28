import random


# help http://blog.yhat.com/posts/the-beer-bandit.html
class BernoulliArm:
    def __init__(self, p):
        self.p = p

    def draw(self):
        return 0.0 if random.random() > self.p else 1


class EpsilonGreedy:
    # constructor
    # epsilon (float): tradeoff exploration/exploitation
    def __init__(self, epsilon):
        self.epsilon = epsilon

    # re-initialize the algorithm in order to run a new simulation
    # n_arms (int): number of arms
    def initialize(self, n_arms):
        self.iter = 0
        self.n_arms = n_arms
        self.gain = [0.0] * n_arms

    # return a index of the chosen decision
    def select_arm(self):
        if random.random() > self.epsilon:
            return self.gain.index(max(self.gain))
        else:
            return random.randint(self.n_arms)

    # update knowledge
    # chosen_arm (int): the decision that has been made
    def update(self, chosen_arm, reward):
        if self.iter == 1:
            self.gain[chosen_arm] = reward * self.epsilon
        self.iter += 1


def test_algorithm(algo, means, num_sims, horizon):
    # init. all decisions
    arms = [BernoulliArm(mu) for mu in means]
    rewards = []

    for sim in range(num_sims):
        algo.initialize(len(arms))
        for t in range(horizon):
            chosen_arm = algo.select_arm()
            reward = arms[chosen_arm].draw()
            algo.update(chosen_arm, reward)
            rewards.append(reward)
