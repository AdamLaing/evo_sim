import random
from collections import Counter

multipliers = {
    'red':    {'purple': 3, 'orange': 3, 'green': 1},
    'yellow': {'purple': 1, 'orange': 3, 'green': 3},
    'blue':   {'purple': 3, 'orange': 1, 'green': 3},
    'purple': {'purple': 4, 'orange': 2, 'green': 2},
    'orange': {'purple': 2, 'orange': 4, 'green': 2},
    'green':  {'purple': 2, 'orange': 2, 'green': 4}
}

num_gens = 1000
carrying_cap = 1000


class Animal:
    def __init__(self, color):
        self.c = color
    def __repr__(self):
        return "A(n) {} animal".format(self.c)
    def __str__(self):
        return "A(n) {} animal".format(self.c)
    def __eq__(self, other):
        return self.c == other.c
    def __hash__(self):
        return hash((self.c))
    def mutate(self):
        new_c = self.c
        colors = {
            1: 'red',
            2: 'yellow',
            3: 'blue',
            4: 'purple',
            5: 'orange',
            6: 'green'
        }
        while new_c == self.c:
            new_c = colors[random.randint(1,6)]
        return new_c
    def next_gen(self, env_color, new_pop):
        num_dice = multipliers[self.c][env_color]
        i = 0
        while i < num_dice:
            roll = random.randint(1,6)
            if roll == 1:
                break
            elif roll > 1 and roll < 4:
                new_pop.append(Animal(self.c))
            elif roll > 3 and roll < 6:
                new_pop.append(Animal(self.c))
                new_pop.append(Animal(self.c))
            else:
                new_pop.append(Animal(self.mutate()))
            i += 1

first_gen = [
    Animal('red'),
    Animal('red'),
    Animal('red'),
    Animal('red'),
    Animal('yellow'),
    Animal('yellow'),
    Animal('yellow'),
    Animal('yellow'),
    Animal('blue'),
    Animal('blue'),
    Animal('blue'),
    Animal('blue'),
    ]

env_history = []

def new_generation(prev_gen):
    next_gen = []
    
    environment_states = {
        1: 'purple',
        2: 'orange',
        3: 'green'
    }
    
    environment = environment_states[random.randint(1,3)]
    # environment = 'purple'
    env_history.append(environment)
    
    # print(environment)
    
    for member in prev_gen:
        member.next_gen(environment, next_gen)
        if len(next_gen) >= carrying_cap:
            break
    
    # print(Counter(next_gen))
    random.shuffle(next_gen)
    return next_gen


generations = []
generations.append(first_gen)

while len(generations) < num_gens:
    generations.append(new_generation(generations[-1]))

print(Counter(generations[-1]))
print(Counter(env_history))
