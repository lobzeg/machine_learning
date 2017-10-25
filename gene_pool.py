from bisect import bisect_left
import numpy as np
from block_diagonal_matrix import BlockDiagonalMatrix
from neural_network import NeuralNetwork


SELECTION_SIZE = 10

# auxiliary class for insertion of neural networks
# with best results into gene pool
class BisectKeyWrapper:

    def __init__(self, iterable, key):
        self.it = iterable
        self.key = key

    def __getitem__(self, i):
        return self.key(self.it[i])

    def __len__(self):
        return len(self.it)


class GenePool:

    def __init__(self, population=None):
        if population == None:
            self.population = {
                'adjusted': [],
                'sell': [],
                'buy': [],
                'positive_bias': [],
                'negative_bias': [],
                'simple': [],
            }

            return

        self.population = population

    # compares results of a nn to results of networks currently in the gene pool
    # and inserts it into gene pool if it is good enough 
    def put(self, nn, result):
        #print(1)
        stagnation=0
        for attr, value in vars(result).items():
            #print(2)
            item = (-1 * value, nn)
            index = bisect_left(BisectKeyWrapper(
                self.population[attr], key=lambda c: c[0]), item[0])

            if index < SELECTION_SIZE:
                self.population[attr].insert(index, item)
            if len(self.population[attr]) > SELECTION_SIZE:
                self.population[attr].pop()
            if index == 0:
                stagnation -= 1

        return stagnation

    def clone(self):
        population = {}
        for k, l in self.population.items():
            population[k] = []
            for item in l:
                population[k].append((item[0], item[1].clone()))

        return GenePool(population)

    def get_population_list(self):
        population = []

        for _, l in self.population.items():
            for item in l:
                population.append(item[1])

        return PopulationList(population)

# the list of neural networks currently in the gene pool
class PopulationList:

    def __init__(self, population):
        self.population = population

    # selects random nn out of the gene pool
    def get_random_nn(self):
        index = np.random.randint(len(self.population))

        return self.population[index]

# function for random generation of pseudo block diagonal matrices
def random_block_diagonal_matrix(number_of_parameters, width, height):
    matrices = []

    is_empty = True
    for i in range(number_of_parameters):
        if np.random.randint(9) > 4:
            matrices.append(np.random.uniform(-1, 1, size=(int(width/number_of_parameters), int(height/number_of_parameters))))
            is_empty = False
        else:
            matrices.append(np.zeros([int(width/number_of_parameters), int(height/number_of_parameters)]))

    if is_empty:
        matrices[np.random.randint(
            number_of_parameters)] = np.random.uniform(-1, 1, size=(int(width/number_of_parameters), int(height/number_of_parameters)))

    return BlockDiagonalMatrix(width, height, matrices)

# generates gene pool by selecting the best out of randomly generating networks
def generate_gene_pool(data, check_data, start, length, inp, h1, h2, h3, o, number_of_iterations, number_of_parameters):
    gp = GenePool()
    
    for i in range(number_of_iterations):
        if i % 100 == 0:
            print(i)

        w1 = random_block_diagonal_matrix(number_of_parameters, inp, h1)
        w2 = random_block_diagonal_matrix(number_of_parameters, h1, h2)
        w3 = np.random.uniform(-1, 1, size=(h2, h3))
        w4 = np.random.uniform(-1, 1, size=(h3, o))

        b1 = np.random.normal(size=h1)
        b2 = np.random.normal(size=h2)
        b3 = np.random.normal(size=h3)
        b4 = np.random.normal(size=o)

        nn = NeuralNetwork(w1, w2, w3, w4, b1, b2, b3, b4)
        result = nn.evaluate(data, check_data, start, length)

        gp.put(nn, result)

    return gp
