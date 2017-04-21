from nodes import *


input1 = inputNode(1)
input2 = inputNode(1)
output = outputNode(1)

input1.addLink(output, 0.5)
input2.addLink(output, 0.5)

firstinput = [0, 1, 0, 1]
secondinput = [0, 0, 1, 1]




for a, b in zip(firstinput, secondinput):

	input1.setActivation(a)
	input2.setActivation(b)
	
	input1.thresholdCheck()
	input2.thresholdCheck()

	print("inputs %d and %d give %s" % (a, b, output.outputcheck()))
	output.resetActivation()

