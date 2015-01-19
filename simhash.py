#--*- encoding: utf-8 -*--
import mmh3
import jieba
import jieba.analyse

#--------------------------------
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#python 2.7 默认字符集问题

class SimHash(object):
	"""docstring for SimHash"""
	def __init__(self, object, topK = 25, bitslength = 64):
		#super(SimHash, self).__init__()
		self.topK = topK
		self.bitslength = bitslength
		self.hash = self.simhash(object)

	def __str__(self):
		return str(self.hash)

	def toBinString(self):
		binstr = bin(self.hash)[2:]
		if len(binstr) < self.bitslength:
			binstr = '0' * (self.bitslength - len(binstr)) + binstr
		return binstr

	def simhash(self, object):
		array = [0] * self.bitslength
		feature_weights = self.extract(object)
		hash_weights = list()
		for feature, weight in feature_weights:
			hashOFfeature = self.prehash(feature)
			for i in range(self.bitslength):
				bitmask = 1 << i
				if hashOFfeature & bitmask:
					array[i] += weight
					#array[i] += 1
				else:
					array[i] -= weight
					#array[i] -= 1
		fingerprint = 0
		for i in range(self.bitslength):
			if array[i] > 0:
				fingerprint += 1 << i
		return fingerprint


	def prehash(self, string):
		return mmh3.hash64(string)[0]

	def extract(self, object):
		content = object
		feature_weights = jieba.analyse.extract_tags(content, topK=self.topK, withWeight=True)
		return feature_weights

	def hammingDistance(self, other):
		x = (self.hash ^ other.hash) & ((1 << self.bitslength) - 1)
		distance = 0
		while(x):
			x &= x - 1
			distance += 1
		return distance

	def similarity(self,other):
		a = float(self.hash)
		b = float(other.hash)
		if a > b : 
			return b / a
		else: 
			return a / b


if __name__ == '__main__':
	jieba.initialize()
	s0 = open("news0.txt",'rb').read()
	s1 = open("news1.txt",'rb').read()
	s2 = open("news2.txt",'rb').read()
	s3 = open("news3.txt",'rb').read()

	sh0 = SimHash(s0)
	sh1 = SimHash(s1)
	sh2 = SimHash(s2)
	sh3 = SimHash(s3)

	print "s0:",sh0.toBinString(), sh0
	print "s1:",sh1.toBinString(), sh1
	print "s2:",sh2.toBinString(), sh2
	print "s3:",sh3.toBinString(), sh3

	print "distance of s0 and s1 is", sh0.hammingDistance(sh1), ", similarity:", sh0.similarity(sh1)
	print "distance of s0 and s2 is", sh0.hammingDistance(sh2), ", similarity:", sh0.similarity(sh2)
	print "distance of s0 and s3 is", sh0.hammingDistance(sh3), ", similarity:", sh0.similarity(sh3)

	print "distance of s1 and s2 is", sh1.hammingDistance(sh2), ", similarity:", sh1.similarity(sh2)
	print "distance of s1 and s3 is", sh1.hammingDistance(sh3), ", similarity:", sh1.similarity(sh3)

	print "distance of s2 and s3 is", sh2.hammingDistance(sh3), ", similarity:", sh2.similarity(sh3)
