import numpy as np
from gene_pool import generate_gene_pool
from nn_evolution import new_generation


def main():
    inp = 160
    h1 = 240
    h2 = 80
    h3 = 20
    o = 3

    number_of_generations = 20
    number_of_iterations = 500
    number_of_parameters = 8

    start = 30000
    length = 5000
    rand_runs = 2

    # load data
    f1 = open('./data/extended_new_si.txt', 'r')
    data = np.loadtxt(f1, dtype='f', delimiter=',')

    f2 = open('./data/sl_200_si.txt', 'r')
    check_data = np.loadtxt(f2, dtype='f', delimiter=',')

    # generate original gene pool
    gp = generate_gene_pool(data, check_data, start, length,
                            inp, h1, h2, h3, o, rand_runs * number_of_iterations, number_of_parameters)

    # GA iterations
    stagnation = 0
    for i in range(number_of_generations):
        gp, stagnation = new_generation(
            gp, data, check_data, start, length, stagnation, number_of_iterations)
    
    save_nn(gp.population['adjusted'][0][1],'adjusted')
    save_nn(gp.population['buy'][0][1],'buy')
    save_nn(gp.population['sell'][0][1],'sell')

def save_nn(nn, name):
    np.savetxt('./result/' + name + '.w1.txt', nn.w1.compose(),
               fmt='%f', delimiter=',', newline='\r\n')

    np.savetxt('./result/' + name + '.w2.txt', nn.w2.compose(),
               fmt='%f', delimiter=',', newline='\r\n')

    np.savetxt('./result/' + name + '.w3.txt', nn.w3,
               fmt='%f', delimiter=',', newline='\r\n')

    np.savetxt('./result/' + name + '.w4.txt', nn.w4,
               fmt='%f', delimiter=',', newline='\r\n')

    np.savetxt('./result/' + name + '.b1.txt', nn.b1,
               fmt='%f', delimiter=',', newline='\r\n')

    np.savetxt('./result/' + name + '.b2.txt', nn.b2,
               fmt='%f', delimiter=',', newline='\r\n')

    np.savetxt('./result/' + name + '.b3.txt', nn.b3,
               fmt='%f', delimiter=',', newline='\r\n')

    np.savetxt('./result/' + name + '.b4.txt', nn.b4,
               fmt='%f', delimiter=',', newline='\r\n')

if __name__ == "__main__":
    main()
