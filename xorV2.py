from graphicNodes import *
from graphics import *
import time



###### starting graphics section
win = nodeWin(x = 200, y =300)



########code is started

input1 = inputNode(1, win)
input2 = inputNode(1, win)
hid1 = hiddenNode(1, win)
hid2 = hiddenNode(1, win)
hid3 = hiddenNode(1, win)
output = outputNode(1, win)

input1.addLink(hid1, 1)
input2.addLink(hid2, 1)
input1.addLink(hid3, 0.5)
hid1.addLink(output, 1)
hid2.addLink(output, 1)
input2.addLink(hid3, 0.5)
hid3.addLink(output, -2)


firstinput = [0, 1, 0, 1]
secondinput = [0, 0, 1, 1]




for a, b in zip(firstinput, secondinput):
	win.win.getMouse()
	input1.setActivation(a)
	input2.setActivation(b)
	
	input1.thresholdCheck()
	input2.thresholdCheck()
	hid1.thresholdCheck()
	hid2.thresholdCheck()
	hid3.thresholdCheck()
	

	print("inputs %d and %d give %s" % (a, b, output.outputcheck()))
	time.sleep(1)
	hid1.resetActivation()
	hid2.resetActivation()
	hid3.resetActivation()
	output.resetActivation()

win.win.getMouse()
win.win.close()
