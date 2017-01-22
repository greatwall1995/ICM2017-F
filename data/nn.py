import mxnet as mx
import csv
import numpy as np
import logging
logging.basicConfig(level=logging.INFO)

X = []
Y = []
with open('work.csv', 'r') as f:
	data = csv.reader(f, delimiter = ' ')
	for row in data:
		X.append([int(row[i]) for i in range(len(row) - 1)])
		Y.append(int(row[-1]))

train_X = np.array(X[: 1000000])
train_Y = np.array(Y[: 1000000])

val_X = np.array(X[1000000: ])
val_Y = np.array(Y[1000000: ])

batch_size = 256

train_iter = mx.io.NDArrayIter(train_X, train_Y.reshape((-1, 1)), batch_size = batch_size)
val_iter = mx.io.NDArrayIter(val_X, val_Y.reshape((-1, 1)), batch_size = batch_size)

devs = [mx.cpu(i) for i in range(4)]

net = mx.sym.Variable('data')
salary = mx.sym.Variable('label')
net = mx.sym.FullyConnected(data = net, name = 'fc1', num_hidden = 128)
net = mx.sym.Activation(data = net, name = 'relu1', act_type = "relu")
net = mx.sym.FullyConnected(data = net, name = 'fc2', num_hidden = 10)
net = mx.sym.Activation(data = net, name = 'relu2', act_type = "relu")
net = mx.sym.FullyConnected(data = net, name = 'fc3', num_hidden = 1)
net = mx.sym.LinearRegressionOutput(data = net, name = 'softmax')

model = mx.model.FeedForward(
	    ctx = devs,
	    symbol = net,
	    num_epoch = 10,
	    optimizer = 'adam',
	    initializer = mx.init.Uniform(0.1),
	    learning_rate = 1e-4
	)

model.fit(
	    X = train_iter,
	    eval_data = val_iter,
	    eval_metric = 'rmse',
	    epoch_end_callback = mx.callback.do_checkpoint('../param/param-nn')
	)