#--*- encoding: utf-8 -*--

class SimHash(object):
	"""docstring for SimHash"""
	def __init__(self, object, hashbits):
		#super(SimHash, self).__init__()
		self.hashbits = hashbits
		self.hash = self.simhash(object)

	def __str__(self):
		return str(self.hash)

	def toBinString(self):
		pass

	def simhash(self):
		pass

	def prehash(self):
		pass

	def hammingD(self):
		pass

	def similarity(self):
		pass
