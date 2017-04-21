from graphicNodes import *
from graphics import *
import time

win = nodeWin()

input1 = inputNode(1, win)
input2 = inputNode(1, win)
output = outputNode(1, win)

input1.addLink(output, 1)
input2.addLink(output, 1)

firstinput = [0, 1, 0, 1]
secondinput = [0, 0, 1, 1]




for a, b in zip(firstinput, secondinput):
	
	input1.setActivation(a)
	input2.setActivation(b)
	win.win.getMouse()
	
	input1.thresholdCheck()
	input2.thresholdCheck()

	print("inputs %d and %d give %s" % (a, b, output.outputcheck()))
	time.sleep(1)
	output.resetActivation()

win.win.getMouse()
win.win.close()