from nodes import *
from graphics import *
import time



###### starting graphics section
win = GraphWin()

Ginput1 = Circle(Point(25, 50), 15)
Ginput2 = Circle(Point(25, 125), 15)
Ghidden1 = Circle(Point(100, 50), 15)
Goutput = Circle(Point(175, 125), 15)

Ginput1.draw(win)
Ginput2.draw(win)
Ghidden1.draw(win)
Goutput.draw(win)


weighti11 = Line(Ginput1.getRight(),Ghidden1.getLeft())
weighti1o = Line(Ginput1.getRight(),Goutput.getLeft())
weighti21 = Line(Ginput2.getRight(),Ghidden1.getLeft())
weighti2o = Line(Ginput2.getRight(),Goutput.getLeft())
weight1o = Line(Ghidden1.getRight(),Goutput.getLeft())

weighti11.setArrow("last")
weighti1o.setArrow("last")
weighti21.setArrow("last")
weighti2o.setArrow("last")
weight1o.setArrow("last")


weighti11.draw(win)
weighti1o.draw(win)
weighti21.draw(win)
weighti2o.draw(win)
weight1o.draw(win)

########code is started

input1 = inputNode(1)
input2 = inputNode(1)
hid1 = nodes(1)
output = outputNode(1)

input1.addLink(output, 1, weighti1o)
input2.addLink(output, 1, weighti2o)
input1.addLink(hid1, 0.5, weighti11)
input2.addLink(hid1, 0.5, weighti21)
hid1.addLink(output, -2, weight1o)


firstinput = [0, 1, 0, 1]
secondinput = [0, 0, 1, 1]




for a, b in zip(firstinput, secondinput):
	win.getMouse()
	input1.setActivation(a)
	input2.setActivation(b)
	
	input1.thresholdCheck(Ginput1)
	input2.thresholdCheck(Ginput2)
	hid1.thresholdCheck(Ghidden1)
	

	print("inputs %d and %d give %s" % (a, b, output.outputcheck(Goutput)))
	time.sleep(1)
	hid1.resetActivation(Ghidden1)
	output.resetActivation(Goutput)

