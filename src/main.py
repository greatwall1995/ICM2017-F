from government import *

import argparse
import os.path
import sys
import matplotlib.pyplot as plt
import numpy as np
import salary as salary

stat = []

def draw_curve():
	pass

def main(dict_args):
	with open('../config/' + dict_args['config'] + '.json', 'r') as f:
		config = json.load(f)

	if not os.path.exists('../param/' + dict_args['param'] + '.json'):
		salary.fit(dict_args['param'], dump_file = True)

	with open('../param/' + dict_args['param'] + '.json', 'r') as f:
		param = np.array(json.load(f))

	total_round = dict_args["round"]
	gov = Government(config, param)
	for month in total_round:
		gov.forward()
		stat.append(gov.stat)

	draw_curve(stat)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Main loop of Mars Migration')
	parser.add_argument('--config', default = 'default')
	parser.add_argument('--round', type = int, default = 360)
	parser.add_argument('--param', default = 'lstsq')
	main(vars(parser.parse_args()))
	pass