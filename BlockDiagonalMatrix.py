import numpy as np


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

    def compose(self):
        w = np.zeros([self.width, self.height])

        x = 0
        y = 0
        
        for matrix in self.matrices:
            w[x:x+matrix.shape[0], y:y+matrix.shape[1]] = matrix
            x += matrix.shape[0]
            y += matrix.shape[1]
        return w
