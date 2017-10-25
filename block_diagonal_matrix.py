import numpy as np

#class of pseudo block diagonal matrices
#provides separate processing of inputs of different types
#at the first 2 layers of neural network
class BlockDiagonalMatrix:

    def __init__(self, width, height, matrices):
        self.width = width
        self.height = height
        self.matrices = matrices

    def clone(self):
        matrices = []

        for matrix in self.matrices:
            matrices.append(np.copy(matrix))

        return BlockDiagonalMatrix(self.width, self.height, matrices)
    
    #composes the weight matrix out of the smaller ones (blocks) 
    def compose(self):
        w = np.zeros([self.width, self.height])

        x = 0
        y = 0
        
        for matrix in self.matrices:
            w[x:x+matrix.shape[0], y:y+matrix.shape[1]] = matrix
            x += matrix.shape[0]
            y += matrix.shape[1]
        return w
