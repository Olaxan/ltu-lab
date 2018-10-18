class KeywordTokenizer:

	def __init__(self, input, *args, **kwargs):
		"""Initializes a keyword tokenizer instance. Looks for keywords in the input string, and applies arguments
		found after the keyword as list attributes. If a keyword is prefixed with a '-', only one argument is applied."""
		self.rest = []
		self.user = input.split()
		for arg in args:
			if arg[0] == "-":
				setattr(self, arg[1:], None)
			else:
				setattr(self, arg, [])
		self.__tokenize(input, *args)

	def __tokenize(self, input, *keywords):
		"""Tokenizes the input string into keywords and arguments (which are fed into instance attributes)."""
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
					if pos >= len(inputs) or inputs[pos] in keywords: #if we've reached EOL, or a new keyword...
						setattr(self, key, words) #set the instance attribute and break
						break
					else:
						words.append(inputs[pos]) 
						inputs.pop(pos)
						if single:
							setattr(self, key, words[0])
							break
		self.tokens = out
		self.rest = inputs
