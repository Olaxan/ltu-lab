class KeywordTokenizer:

	def __init__(self, input, *args, **kwargs):
		self.rest = []
		self.user = input.split()
		for arg in args:
			if arg[0] == "-":
				setattr(self, arg[1:], None)
			else:
				setattr(self, arg, [])
		self.__tokenize(input, *args)

	def __tokenize(self, input, *keywords):

		out = []
		inputs = self.user.copy()

		for key in keywords:

			if key[0] == "-":
				key = key[1:]
				single = True
			else:
				single = False

			if key in inputs:
				words = []
				pos = inputs.index(key)
				inputs.pop(pos)
				while True:
					if pos >= len(inputs) or inputs[pos] in keywords:
						setattr(self, key, words)
						break
					else:
						words.append(inputs[pos])
						inputs.pop(pos)
						if single:
							setattr(self, key, words[0])
							break
		self.tokens = out
		self.rest = inputs
