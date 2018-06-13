# machine_learning
This was a naive attempt to design a neural network from scratch for stock market trading. This was done primarily for learning purpoces, at the time when my understanding of machine learning was very limited. Though methods used were far from the most efficient/modern ones (for example, I strongly underestimated the power of backpropagation), I've still learned a lot about neural networks training process from this experience.

The neural network uses certain data on USD-RUB futures contracts as input: minimums, maximums, closing prices, volumes and four sets based on exponential moving averages; all eight sets are provided for the last 20 bars. extended_mew_si.txt is the file containing the input vectors.
The output of the network is a normalized vector with three values. The greatest one detrmines what action is taken at the moment: buy stock, sell stock or do nothing. The file sl_200_si.txt contains the calculated results of buying and seliing at any point, which is used for calculating the evaluation functions.

The files containing the neural networks are placed in the root of the repository.

The /data/ directory contains the data files for training the network. si.txt is the original data file.

The scripts for data processing are placed in the /auxiliary_scripts/ directory.
