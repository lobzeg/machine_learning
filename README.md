# machine_learning
This is an ongoing project for designing a neural network for stock market trading, which is able to train efficiently on limited data.
The neural network uses certain data on USD-RUB futures contracts as input: minimums, maximums, closing prices, volumes and four sets based on exponential moving averages; all eight sets are provided for the last 20 bars. extended_mew_si.txt is the file containing the input vectors.
The output of the network is a normalized vector with three values. The greatest one detrmines what action is taken at the moment: buy stock, sell stock or do nothing. The file sl_200_si.txt contains the calculated results of buying and seliing at any point, which is used for calculating the evaluation functions.

The files containing the neural networks are placed in the root of the repository.

The /data/ directory contains the data files for training the network. si.txt is the original data file.

The scripts for data processing are placed in the /auxiliary_scripts/ directory.
