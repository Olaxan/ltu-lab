class User:

	def __init__(self, name, number = None, *args, **kwargs):
		self._name = name
		self.numbers = []
		return super().__init__(*args, **kwargs)

	@property
	def name(self):
		return self._name

	@name.getter
	def name(self, value):
		self._name = value

	@name.deleter
	def name(self):
		del self._name


