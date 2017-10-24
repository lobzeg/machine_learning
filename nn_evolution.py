import numpy as np
from BlockDiagonalMatrix import BlockDiagonalMatrix
from NeuralNetwork import NeuralNetwork

NUMP=8

# Creates and evaluate a generation of GA
def new_generation(gp, data, check_data, start, length, stagnation, number_of_iterations):
    k1 = max([5 + stagnation * 2, 200])
    k2 = max([1 + stagnation * 3, 200])
    stagnation = stagnation + 3
    

    pl = gp.get_population_list()
    new_gp = gp.clone()


    for i in range(number_of_iterations):
        if i % 100 == 0:
            print(i)

        w1 = crossover_block_diagonal_matrix(pl, 'w1', k1, k2)
        w2 = crossover_block_diagonal_matrix(pl, 'w2', k1, k2)
        w3 = crossover_matrix(pl, 'w3', k1, k2)
        w4 = crossover_matrix(pl, 'w4', k1, k2)

        b1 = crossover_bias_vector(pl, 'b1', k1, k2)
        b2 = crossover_bias_vector(pl, 'b2', k1, k2)
        b3 = crossover_bias_vector(pl, 'b3', k1, k2)
        b4 = crossover_bias_vector(pl, 'b4', k1, k2)

        nn = NeuralNetwork(w1, w2, w3, w4, b1, b2, b3, b4)
        result = nn.evaluate(data, check_data, start, length)

        stagnation += new_gp.put(nn, result)

    return new_gp, stagnation

# mutation function for matrices
def mutate_matrix(main_matrix, mutation_source_matrix, k1, k2):
    main_matrix = np.copy(main_matrix)

    for i in range(max(0, int(main_matrix.shape[1] * np.random.normal(k1, k1/5) / 500))):
        a = np.random.randint(main_matrix.shape[1])
        for j in range(main_matrix.shape[0]):
            main_matrix[j, a] = mutation_source_matrix[j, a]

    for i in range(max(0, int(main_matrix.shape[0] * np.random.normal(k1, k1/5) / 500))):
        a = np.random.randint(main_matrix.shape[0])
        for j in range(main_matrix.shape[1]):
            main_matrix[a, j] = mutation_source_matrix[a, j]

    for i in range(max(0, int(np.prod(main_matrix.shape) * np.random.normal(k2, k2/5) / 500))):
        main_matrix[np.random.randint(main_matrix.shape[0]), np.random.randint(
            main_matrix.shape[1])] = np.random.uniform(-1, 1)

    return main_matrix

# mutation function for vectors
def mutate_vector(main_vector, mutation_source_vector, k1, k2):
    main_vector = np.copy(main_vector)

    for i in range(max(0, int(main_vector.shape[0] * np.random.normal(k1, k1/5) / 500))):
        a = np.random.randint(main_vector.shape[0])
        main_vector[a] = mutation_source_vector[a]

    for i in range(max(0, int(main_vector.shape[0] * np.random.normal(k2, k2/5) / 500))):
        main_vector[np.random.randint(main_vector.shape[0])] = np.random.normal()

    return main_vector

# breeding function for block diagonal matrices (w1 and w2)
def crossover_block_diagonal_matrix(pl, name, k1, k2):
    matrices = []

    for i in range(NUMP):
        nn1 = pl.get_random_nn()
        nn2 = pl.get_random_nn()
        matrix = mutate_matrix(getattr(nn1, name).matrices[i],
                               getattr(nn2, name).matrices[i], k1, k2)
        matrices.append(matrix)

    return BlockDiagonalMatrix(getattr(nn1, name).width, getattr(nn1, name).height, matrices)

# breeding function for regular matrices
def crossover_matrix(pl, name, k1, k2):
    nn1 = pl.get_random_nn()
    nn2 = pl.get_random_nn()

    return mutate_matrix(getattr(nn1, name), getattr(nn2, name), k1, k2)

# breeding function for vectors
def crossover_bias_vector(pl, name, k1, k2):
    nn1 = pl.get_random_nn()
    nn2 = pl.get_random_nn()

    return mutate_vector(getattr(nn1, name), getattr(nn2, name), k1, k2)
