class People(object):
	"""docstring for People"""
	def __init__(self, parent, dict_args):
		super(People, self).__init__()
		self.parent = parent
		self.gender = dict_args['gender']
		self.edu_lvl = dict_args['education']
		self.preg = dict_args['pregnant']
		self.age = dict_args['age']
		self.atwork = 1

	