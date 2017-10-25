import numpy as np

# class of results of different evaluation functions
# best networks for each function are kept in the gene pool
class Result:

    def __init__(self):
        self.adjusted = 0
        self.sell = 0
        self.buy = 0
        self.positive_bias = 0
        self.negative_bias = 0
        self.simple = 0


class NeuralNetwork:

    def __init__(self, w1, w2, w3, w4, b1, b2, b3, b4):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4

        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4

    def clone(self):
        w1 = self.w1.clone()
        w2 = self.w2.clone()
        w3 = np.copy(self.w3)
        w4 = np.copy(self.w4)

        b1 = np.copy(self.b1)
        b2 = np.copy(self.b2)
        b3 = np.copy(self.b3)
        b4 = np.copy(self.b4)

        return NeuralNetwork(w1, w2, w3, w4, b1, b2, b3, b4)
    
    # evaluates performance of neural network 
    # by checking how well it would trade on the testing period
    def evaluate(self, data, check_data, start, length):
        result = Result()

        max_profit = 0
        drawdown = 0
        for i in range(start, start + length):
            # run neural network
            y1 = np.matmul(data[i], self.w1.compose()) + self.b1
            y2 = np.matmul(y1, self.w2.compose()) + self.b2
            y3 = np.matmul(y2, self.w3) + self.b3
            y4 = np.matmul(y3, self.w4) + self.b4

            # normalize output
            d = max(y4)
            y4[0] -= d
            y4[1] -= d
            y4[2] -= d
            score_mat_exp = np.exp(np.asarray(y4))
            y4 = score_mat_exp / score_mat_exp.sum(0)

            mult = 4

            # buy the stock
            if y4[0] > y4[1] and y4[0] > y4[2]:
                deal_outcome = check_data[i + 19, 0]
                result.simple = result.simple + deal_outcome
                if deal_outcome > 0:
                    result.adjusted = result.adjusted + deal_outcome
                    result.buy = result.buy + deal_outcome
                    result.positive_bias = result.positive_bias + mult * deal_outcome
                    result.negative_bias = result.negative_bias + deal_outcome
                else:
                    result.adjusted = result.adjusted + deal_outcome
                    result.positive_bias = result.positive_bias + deal_outcome
                    result.negative_bias = result.negative_bias + mult * deal_outcome
                    result.buy = result.buy + deal_outcome

                if max_profit - result.adjusted > drawdown:
                    drawdown = max_profit - result.adjusted
                if result.adjusted > max_profit:
                    max_profit = result.adjusted

            # sell the stock
            if y4[1] > y4[0] and y4[1] > y4[2]:
                deal_outcome = check_data[i + 19, 0]
                result.simple = result.simple + deal_outcome
                if deal_outcome > 0:
                    result.adjusted = result.adjusted + deal_outcome
                    result.sell = result.sell + deal_outcome
                    result.positive_bias = result.positive_bias + mult * deal_outcome
                    result.negative_bias = result.negative_bias + deal_outcome
                else:
                    result.adjusted = result.adjusted + deal_outcome
                    result.positive_bias = result.positive_bias + deal_outcome
                    result.negative_bias = result.negative_bias + mult * deal_outcome
                    result.sell = result.sell + deal_outcome

                if max_profit - result.adjusted > drawdown:
                    drawdown = max_profit - result.adjusted
                if result.adjusted > max_profit:
                    max_profit = result.adjusted

        # adjusts result to drawdown
        if drawdown > 0:
            result.adjusted = result.adjusted / max([1, drawdown / 1000])

        return result
