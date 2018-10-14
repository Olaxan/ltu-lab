class KeywordTokenizer:

	def __init__(self, input, *args, **kwargs):
		self.rest = []
		self.user = input.split()
		for arg in args:
			setattr(self, arg, [])
		self.__tokenize(input, *args)

	def __tokenize(self, input, *keywords):

		out = []
		inputs = self.user.copy()

		for key in keywords:
			if key in inputs:
				words = []
				pos = inputs.index(key)
				inputs.pop(pos)
				while True:

					if pos >= len(inputs) or inputs[pos] in keywords:
						#out.append((key, words))
						setattr(self, key, words)
						break
					else:
						words.append(inputs[pos])
						inputs.pop(pos)
		self.tokens = out
		self.rest = inputs
