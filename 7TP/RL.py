import random
import cellular
# reload(cellular)
# import qlearn_mod_random as qlearn # to use the alternative exploration method
import qlearn

# reload(qlearn)

directions = 8

lookdist = 2
lookcells = []
for i in range(-lookdist, lookdist + 1):
    for j in range(-lookdist, lookdist + 1):
        if (abs(i) + abs(j) <= lookdist) and (i != 0 or j != 0):
            lookcells.append((i, j))


def pickRandomLocation():
    while 1:
        x = random.randrange(world.width)
        y = random.randrange(world.height)
        cell = world.getCell(x, y)
        if not (cell.wall or len(cell.agents) > 0):
            return cell


class Cell(cellular.Cell):
    wall = False

    def colour(self):
        if self.wall:
            return 'black'
        else:
            return 'white'

    def load(self, data):
        if data == 'X':
            self.wall = True
        else:
            self.wall = False


class Cat(cellular.Agent):
    cell = None
    score = 0
    colour = 'orange'

    def __init__(self, aggressivity=0):
        self.aggressivity = aggressivity

    def update(self):
        cell = self.cell
        if cell != mouse.cell:
            if random.random() < self.aggressivity:
                # the cat goes toward the mouse !!
                self.goTowards(mouse.cell)
                while cell == self.cell:
                    self.goInDirection(random.randrange(directions))
            else:
                # the cat goes randomly
                self.goInDirection(random.randrange(directions))


class Cheese(cellular.Agent):
    colour = 'yellow'

    def update(self):
        pass


class Mouse_random(cellular.Agent):
    colour = 'gray'

    def __init__(self):
        self.ai = None
        self.eaten = 0
        self.fed = 0
        self.lastState = None
        self.lastAction = None

    def update(self):
        state = self.calcState()
        reward = -1

        for c in cat:
            if self.cell == c.cell:
                self.eaten += 1
                reward = -100
                if self.lastState is not None:
                    self.lastState = None
                    self.cell = pickRandomLocation()
                    return

        if self.cell == cheese.cell:
            self.fed += 1
            reward = 50
            cheese.cell = pickRandomLocation()

        state = self.calcState()
        action = random.randrange(directions)
        self.lastState = state
        self.lastAction = action

        self.goInDirection(action)

    def calcState(self):
        def cellvalue(cell):
            for c in cat:
                if c.cell is not None and (cell.x == c.cell.x and
                                                   cell.y == c.cell.y):
                    return 3
            if cheese.cell is not None and (cell.x == cheese.cell.x and
                                                    cell.y == cheese.cell.y):
                return 2
            else:
                return 1 if cell.wall else 0

        return tuple([cellvalue(self.world.getWrappedCell(self.cell.x + j, self.cell.y + i))
                      for i, j in lookcells])


class Mouse(cellular.Agent):
    colour = 'gray'

    def __init__(self):
        self.ai = qlearn.QLearn([0, 1, 2, 3, 4, 5, 6, 7])
        self.eaten = 0
        self.fed = 0
        self.lastState = None
        self.lastAction = None

    ## implementation of the Qlearning !
    def update(self):
        state = self.calcState()
        reward = -1

        for c in cat:
            if self.cell == c.cell:
                self.eaten += 1
                reward = -100
                if self.lastState is not None:
                    self.lastState = None

                    self.cell = pickRandomLocation()
                    return

        if self.cell == cheese.cell:
            self.fed += 1
            reward = 150
            cheese.cell = pickRandomLocation()

        self.ai.updateLearn(self.lastState, self.lastAction, state, reward)
        # usefull if a cheese appears nearby
        state = self.calcState()
        # votre IA doit choisir une action
        action = self.ai.chooseAction(state)
        self.lastState = state
        self.lastAction = action

        self.goInDirection(action)

    def calcState(self):
        def cellvalue(cell):
            for c in cat:
                if c.cell is not None and (cell.x == c.cell.x and
                                                   cell.y == c.cell.y):
                    return 3
            if cheese.cell is not None and (cell.x == cheese.cell.x and
                                                    cell.y == cheese.cell.y):
                return 2
            else:
                return 1 if cell.wall else 0

        return tuple([cellvalue(self.world.getWrappedCell(self.cell.x + j, self.cell.y + i))
                      for i, j in lookcells])


# define an agent controlled by the algorithm
mouse = Mouse()
# mouse = Mouse_random()

# define the bad agents
cat = []
cat.append(Cat(0))

# define the food
cheese = Cheese()

world = cellular.World(Cell, directions=directions, filename='level.txt')
world.age = 0
world.addAgent(cheese, cell=pickRandomLocation())
for c in cat:
    world.addAgent(c)
world.addAgent(mouse)
endAge = world.age + 150000

# activate display
world.display.activate(size=40)
world.display.delay = 2

# main loop
while world.age < endAge:
    world.update()

    # average quantities
    if world.age % 10000 == 0:
        print("{:d}, W: {:d}, L: {:d}" \
              .format(world.age, mouse.fed, mouse.eaten))
        mouse.eaten = 0
        mouse.fed = 0

# end of monitoring
world.display.activate(size=40)
world.display.delay = 1
while 1:
    world.update()
