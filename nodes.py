import time
class nodes(object):
	"""general nodes"""

	def __init__(self, threshold):
		self.activation = 0
		self.threshold = threshold
		self.links = []
		self.weights = []
		self.Glinks = []

	def addLink(self, link, weight, Glink):
		self.links.append(link)
		self.weights.append(weight)
		self.Glinks.append(Glink)

	def addActivation(self, potential):
		self.activation = self.activation + potential

	def resetActivation(self, Gnode):
		self.activation = 0
		Gnode.setFill("")


	def propagate(self):
		for node, weight, Glink in zip(self.links, self.weights, self.Glinks):
			node.addActivation(weight)
			if weight>0:
				Glink.setOutline('red')
			else:
				Glink.setOutline('blue')
			time.sleep(1)
			Glink.setOutline('black')


	def thresholdCheck(self, Gnode):
		if self.activation >= self.threshold:
			Gnode.setFill('red')
			self.propagate()
			self.resetActivation(Gnode)

class inputNode(nodes):
	"""inputs nodes"""
	def __init__(self, threshold):
		nodes.__init__(self, threshold)

	def setActivation(self, activation):
		self.activation = activation

class outputNode(nodes):
	"""output nodes"""
	def __init__(self, threshold):
		nodes.__init__(self, threshold)
		
	def outputcheck(self, Gnode):
		if self.activation >= self.threshold:
			Gnode.setFill('red')
			return "Output activated"
		else:
			return "Output not activated"
		

		
