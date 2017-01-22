import numpy as np
import people as pp

class Government(object):
	"""docstring for Government"""
	def __init__(self, config, param):
		super(Government, self).__init__()
		self.config = config
		self.param = param
		self.month = 0
		self.stage = 0
		self.residents = []

	def predict_salary(params):
		return params.dot(self.param)

	def migrate(num):
		

	def count():
		ret = 0
		for people in self.residents:
			if people.isdead:
				ret += 1

		if 2 * ret < len(residents):
			alive_residents = [people for people in self.residents if not people.isdead]
			self.residents = alive_residents

		return ret

	def forward():
		if self.month == self.config['migrants'][0][self.stage]:
			migrate(self.config['migrants'][1][self.stage])
			self.stage += 1

		for people in self.residents:
			people.forward()

		self.month += 1

	@property
	def stat():
		pass
