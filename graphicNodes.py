from graphics import *
import time



class nodeWin(object):
	def __init__(self, x = 200, y = 200):
		self.win = GraphWin(width = x, height = y)
		self.ninput = 0
		self.nhidden = 0
		self.noutput = 0

	def addinputnode(self):
		Gnode = Circle(Point(25, (self.ninput*75+50)), 15)
		Gnode.draw(self.win)
		self.ninput += 1
		return Gnode

	def addhiddennode(self):
		Gnode = Circle(Point(100, (self.nhidden*75+50)), 15)
		Gnode.draw(self.win)
		self.nhidden += 1
		return Gnode

	def addoutputnode(self):
		Gnode = Circle(Point(175, (self.noutput*75+50)), 15)
		Gnode.draw(self.win)
		self.noutput += 1
		return Gnode

	def addlink(self, node1, node2):
		line = Line(node1.getRight(),node2.getLeft())
		line.setArrow("last")
		line.draw(self.win)
		return line

class nodes(object):
	"""general nodes"""

	def __init__(self, threshold, win):
		self.activation = 0
		self.threshold = threshold
		self.win = win
		self.links = []
		self.weights = []
		self.Glinks = []

	def addLink(self, link, weight):
		self.links.append(link)
		self.weights.append(weight)
		Glink = self.win.addlink(self.Gnode, link.Gnode)
		self.Glinks.append(Glink)

	def addActivation(self, potential):
		self.activation = self.activation + potential

	def resetActivation(self):
		self.activation = 0
		self.Gnode.setFill("")


	def propagate(self):
		for node, weight, Glink in zip(self.links, self.weights, self.Glinks):
			node.addActivation(weight)
			if weight>0:
				Glink.setOutline('red')
			else:
				Glink.setOutline('blue')
			time.sleep(1)
			Glink.setOutline('black')


	def thresholdCheck(self):
		if self.activation >= self.threshold:
			self.Gnode.setFill('red')
			self.propagate()
			self.resetActivation()

class inputNode(nodes):
	"""inputs nodes"""
	def __init__(self, threshold, win):
		nodes.__init__(self, threshold, win)
		self.Gnode = win.addinputnode()
		Label = Text(self.Gnode.getCenter(), '')
		Label.draw(win.win)
		self.Label = Label

	def setActivation(self, activation):
		self.activation = activation
		self.Label.setText(str(activation))

class hiddenNode(nodes):
	"""inputs nodes"""
	def __init__(self, threshold, win):
		nodes.__init__(self, threshold, win)
		self.Gnode = self.win.addhiddennode()

class outputNode(nodes):
	"""output nodes"""
	def __init__(self, threshold, win):
		nodes.__init__(self, threshold, win)
		self.Gnode = self.win.addoutputnode()
		
	def outputcheck(self):
		if self.activation >= self.threshold:
			self.Gnode.setFill('red')
			return "Output activated"
		else:
			return "Output not activated"
		