"""
InkOptParamWindow.py
"""


import tkinter as tk
from InkOptHelpers import *


# ## Future home of the code for the Parameter Window
# ## May need to pass in Tk node, return ParamWindow frame

def loadParams(log, inkopt, ParamWindow):
	"""
	Trigger the InkOpt engine to read input parameters from the input file indicated in the Parameter Window.
	Populate Parameter Window fields with values from input.
	"""
	
	log.debug("Entering loadParams()")
	
	# Get parameters from input file via InkOpt.setParams()
	log.debug("Getting parameters from {}".format(ParamWindow.loadframe.inputfile.get()))
	inkopt.setParams(ParamWindow.loadframe.inputfile.get())
	log.debug("Parameters:\n{}\n".format(*inkopt.params))
	
	# List of Parameter Window fields
	params = {
		"maxDiffPdfs" : ParamWindow.paramframe.maxDiffPdfs,
		"maxPDf" : ParamWindow.paramframe.maxPDf,
		"minVgrin" : ParamWindow.paramframe.minVgrin,
		"minDnAvg" : ParamWindow.paramframe.minDnAvg,
		"matrix1" : ParamWindow.paramframe.matrix1,
		"matrix2" : ParamWindow.paramframe.matrix2,
		"dopant1" : ParamWindow.paramframe.dopant1,
		"dopant2" : ParamWindow.paramframe.dopant2,
		"dopant3" : ParamWindow.paramframe.dopant3,
		"dopant4" : ParamWindow.paramframe.dopant4,
		"d1min" : ParamWindow.paramframe.d1min,
		"d1max" : ParamWindow.paramframe.d1max,
		"d2min" : ParamWindow.paramframe.d2min,
		"d2max" : ParamWindow.paramframe.d2max,
		"d3min" : ParamWindow.paramframe.d3min,
		"d3max" : ParamWindow.paramframe.d3max,
		"d4min" : ParamWindow.paramframe.d4min,
		"d4max" : ParamWindow.paramframe.d4max
	}
	
	log.debug("ParamWindow.params.items():\n{}\n".format(params.items()))
	
	# Copy parameters into window field stringvars and refresh field text
	for param in params.items():
		log.debug("Setting {} to *{}".format(param[0], [*inkopt.params["{}".format(param[0])]]))
		# Set value
		if len([*inkopt.params["{}".format(param[0])]]) == 1:
			param[1].var.set(*inkopt.params["{}".format(param[0])])
		else:
			# ## This could be done better to avoid weirdness in the UI
			param[1].var.set([*inkopt.params["{}".format(param[0])]])
		# Refresh field
		param[1].value.delete(0, tk.END)
		param[1].value.insert(0, param[1].var.get())
	
	log.debug("paramframe.*.var: {}\n".format([
		ParamWindow.paramframe.maxDiffPdfs.var.get(),
		ParamWindow.paramframe.maxPDf.var.get(),
		"...",
		ParamWindow.paramframe.d4max.var.get()
		]))
	log.debug("inkopt.params: {}\n".format([
		*inkopt.params["maxDiffPdfs"],
		*inkopt.params["maxDiffPdfs"],
		*inkopt.params["maxPDf"],
		"...",
		*inkopt.params["d4max"]
		]))
		
		
def PackLoadFrame(master, inkopt, log):
	"""
	
	"""
	loadframe = tk.Frame(master)
	loadframe.pack(side = tk.TOP)
	loadframe.loadbutton = tk.Button(loadframe, text = "Load", command = lambda: loadParams(log, inkopt, master))
	loadframe.loadbutton.pack(side = tk.LEFT)
	loadframe.inputfile = tk.StringVar()
	loadframe.inputfile.set("input.txt")
	loadframe.inputfield = tk.Entry(loadframe, text = loadframe.inputfile.get(), textvariable = loadframe.inputfile)
	loadframe.inputfield.pack(side = tk.RIGHT)
	return loadframe
	
	
	
def PackParamWindowFrame(master):
	"""
	
	"""
	
	frame = tk.Frame(master, relief = FRAMERELIEF)
	frame.pack()
	frame.widthprop = tk.Frame(frame, width = SMALLWINDOWX, height = 0, relief = FRAMERELIEF)
	frame.widthprop.pack(side = tk.TOP)
	return frame
	
	
def LoadParamWindow(master, inkopt):
	"""
	
	"""
	
	log = startLog(__name__)
	log.debug("Building ParameterWindow")
	
	# Build the window frame
	frame = PackParamWindowFrame(master)
	
	# Define the frame for loading from file
	frame.loadframe = PackLoadFrame(frame, inkopt, log)
	
	
	
	# Define the frame for viewing loaded parameters
	frame.paramframe = tk.Frame(frame)
	frame.paramframe.pack(side = tk.BOTTOM)
	
	"""Populate the parameter frame with tk.Label/tk.Entry (key/value) pairs"""
	# ## Functionalize
	# maxDiffPdfs
	frame.paramframe.maxDiffPdfs = tk.Frame(frame.paramframe)
	frame.paramframe.maxDiffPdfs.pack()
	frame.paramframe.maxDiffPdfs.label = tk.Label(frame.paramframe.maxDiffPdfs, text = "maxDiffPdfs")
	frame.paramframe.maxDiffPdfs.label.pack(side = tk.LEFT)
	frame.paramframe.maxDiffPdfs.var = tk.StringVar()
	frame.paramframe.maxDiffPdfs.var.set("")
	frame.paramframe.maxDiffPdfs.value = tk.Entry(frame.paramframe.maxDiffPdfs, text = "")
	frame.paramframe.maxDiffPdfs.value.pack(side = tk.RIGHT)
	# maxPDf
	frame.paramframe.maxPDf = tk.Frame(frame.paramframe)
	frame.paramframe.maxPDf.pack()
	frame.paramframe.maxPDf.label = tk.Label(frame.paramframe.maxPDf, text = "maxPDf")
	frame.paramframe.maxPDf.label.pack(side = tk.LEFT)
	frame.paramframe.maxPDf.var = tk.StringVar()
	frame.paramframe.maxPDf.var.set("")
	frame.paramframe.maxPDf.value = tk.Entry(frame.paramframe.maxPDf, text = "")
	frame.paramframe.maxPDf.value.pack(side = tk.RIGHT)
	# minVgrin
	frame.paramframe.minVgrin = tk.Frame(frame.paramframe)
	frame.paramframe.minVgrin.pack()
	frame.paramframe.minVgrin.label = tk.Label(frame.paramframe.minVgrin, text = "minVgrin")
	frame.paramframe.minVgrin.label.pack(side = tk.LEFT)
	frame.paramframe.minVgrin.var = tk.StringVar()
	frame.paramframe.minVgrin.var.set("")
	frame.paramframe.minVgrin.value = tk.Entry(frame.paramframe.minVgrin, text = "")
	frame.paramframe.minVgrin.value.pack(side = tk.RIGHT)
	# minDnAvg
	frame.paramframe.minDnAvg = tk.Frame(frame.paramframe)
	frame.paramframe.minDnAvg.pack()
	frame.paramframe.minDnAvg.label = tk.Label(frame.paramframe.minDnAvg, text = "minDnAvg")
	frame.paramframe.minDnAvg.label.pack(side = tk.LEFT)
	frame.paramframe.minDnAvg.var = tk.StringVar()
	frame.paramframe.minDnAvg.var.set("")
	frame.paramframe.minDnAvg.value = tk.Entry(frame.paramframe.minDnAvg, text = "")
	frame.paramframe.minDnAvg.value.pack(side = tk.RIGHT)
	# matrix1
	frame.paramframe.matrix1 = tk.Frame(frame.paramframe)
	frame.paramframe.matrix1.pack()
	frame.paramframe.matrix1.label = tk.Label(frame.paramframe.matrix1, text = "matrix1")
	frame.paramframe.matrix1.label.pack(side = tk.LEFT)
	frame.paramframe.matrix1.var = tk.StringVar()
	frame.paramframe.matrix1.var.set("")
	frame.paramframe.matrix1.value = tk.Entry(frame.paramframe.matrix1, text = "")
	frame.paramframe.matrix1.value.pack(side = tk.RIGHT)
	# matrix2
	frame.paramframe.matrix2 = tk.Frame(frame.paramframe)
	frame.paramframe.matrix2.pack()
	frame.paramframe.matrix2.label = tk.Label(frame.paramframe.matrix2, text = "matrix2")
	frame.paramframe.matrix2.label.pack(side = tk.LEFT)
	frame.paramframe.matrix2.var = tk.StringVar()
	frame.paramframe.matrix2.var.set("")
	frame.paramframe.matrix2.value = tk.Entry(frame.paramframe.matrix2, text = "")
	frame.paramframe.matrix2.value.pack(side = tk.RIGHT)
	# dopant1
	frame.paramframe.dopant1 = tk.Frame(frame.paramframe)
	frame.paramframe.dopant1.pack()
	frame.paramframe.dopant1.label = tk.Label(frame.paramframe.dopant1, text = "dopant1")
	frame.paramframe.dopant1.label.pack(side = tk.LEFT)
	frame.paramframe.dopant1.var = tk.StringVar()
	frame.paramframe.dopant1.var.set("")
	frame.paramframe.dopant1.value = tk.Entry(frame.paramframe.dopant1, text = "")
	frame.paramframe.dopant1.value.pack(side = tk.RIGHT)
	# dopant2
	frame.paramframe.dopant2 = tk.Frame(frame.paramframe)
	frame.paramframe.dopant2.pack()
	frame.paramframe.dopant2.label = tk.Label(frame.paramframe.dopant2, text = "dopant2")
	frame.paramframe.dopant2.label.pack(side = tk.LEFT)
	frame.paramframe.dopant2.var = tk.StringVar()
	frame.paramframe.dopant2.var.set("")
	frame.paramframe.dopant2.value = tk.Entry(frame.paramframe.dopant2, text = "")
	frame.paramframe.dopant2.value.pack(side = tk.RIGHT)
	# dopant3
	frame.paramframe.dopant3 = tk.Frame(frame.paramframe)
	frame.paramframe.dopant3.pack()
	frame.paramframe.dopant3.label = tk.Label(frame.paramframe.dopant3, text = "dopant3")
	frame.paramframe.dopant3.label.pack(side = tk.LEFT)
	frame.paramframe.dopant3.var = tk.StringVar()
	frame.paramframe.dopant3.var.set("")
	frame.paramframe.dopant3.value = tk.Entry(frame.paramframe.dopant3, text = "")
	frame.paramframe.dopant3.value.pack(side = tk.RIGHT)
	# dopant4
	frame.paramframe.dopant4 = tk.Frame(frame.paramframe)
	frame.paramframe.dopant4.pack()
	frame.paramframe.dopant4.label = tk.Label(frame.paramframe.dopant4, text = "dopant4")
	frame.paramframe.dopant4.label.pack(side = tk.LEFT)
	frame.paramframe.dopant4.var = tk.StringVar()
	frame.paramframe.dopant4.var.set("")
	frame.paramframe.dopant4.value = tk.Entry(frame.paramframe.dopant4, text = "")
	frame.paramframe.dopant4.value.pack(side = tk.RIGHT)
	# d1min
	frame.paramframe.d1min = tk.Frame(frame.paramframe)
	frame.paramframe.d1min.pack()
	frame.paramframe.d1min.label = tk.Label(frame.paramframe.d1min, text = "d1min")
	frame.paramframe.d1min.label.pack(side = tk.LEFT)
	frame.paramframe.d1min.var = tk.StringVar()
	frame.paramframe.d1min.var.set("")
	frame.paramframe.d1min.value = tk.Entry(frame.paramframe.d1min, text = "")
	frame.paramframe.d1min.value.pack(side = tk.RIGHT)
	# d1max
	frame.paramframe.d1max = tk.Frame(frame.paramframe)
	frame.paramframe.d1max.pack()
	frame.paramframe.d1max.label = tk.Label(frame.paramframe.d1max, text = "d1max")
	frame.paramframe.d1max.label.pack(side = tk.LEFT)
	frame.paramframe.d1max.var = tk.StringVar()
	frame.paramframe.d1max.var.set("")
	frame.paramframe.d1max.value = tk.Entry(frame.paramframe.d1max, text = "")
	frame.paramframe.d1max.value.pack(side = tk.RIGHT)
	# d2min
	frame.paramframe.d2min = tk.Frame(frame.paramframe)
	frame.paramframe.d2min.pack()
	frame.paramframe.d2min.label = tk.Label(frame.paramframe.d2min, text = "d2min")
	frame.paramframe.d2min.label.pack(side = tk.LEFT)
	frame.paramframe.d2min.var = tk.StringVar()
	frame.paramframe.d2min.var.set("")
	frame.paramframe.d2min.value = tk.Entry(frame.paramframe.d2min, text = "")
	frame.paramframe.d2min.value.pack(side = tk.RIGHT)
	# d2max
	frame.paramframe.d2max = tk.Frame(frame.paramframe)
	frame.paramframe.d2max.pack()
	frame.paramframe.d2max.label = tk.Label(frame.paramframe.d2max, text = "d2max")
	frame.paramframe.d2max.label.pack(side = tk.LEFT)
	frame.paramframe.d2max.var = tk.StringVar()
	frame.paramframe.d2max.var.set("")
	frame.paramframe.d2max.value = tk.Entry(frame.paramframe.d2max, text = "")
	frame.paramframe.d2max.value.pack(side = tk.RIGHT)
	# d3min
	frame.paramframe.d3min = tk.Frame(frame.paramframe)
	frame.paramframe.d3min.pack()
	frame.paramframe.d3min.label = tk.Label(frame.paramframe.d3min, text = "d3min")
	frame.paramframe.d3min.label.pack(side = tk.LEFT)
	frame.paramframe.d3min.var = tk.StringVar()
	frame.paramframe.d3min.var.set("")
	frame.paramframe.d3min.value = tk.Entry(frame.paramframe.d3min, text = "")
	frame.paramframe.d3min.value.pack(side = tk.RIGHT)
	# d3max
	frame.paramframe.d3max = tk.Frame(frame.paramframe)
	frame.paramframe.d3max.pack()
	frame.paramframe.d3max.label = tk.Label(frame.paramframe.d3max, text = "d3max")
	frame.paramframe.d3max.label.pack(side = tk.LEFT)
	frame.paramframe.d3max.var = tk.StringVar()
	frame.paramframe.d3max.var.set("")
	frame.paramframe.d3max.value = tk.Entry(frame.paramframe.d3max, text = "")
	frame.paramframe.d3max.value.pack(side = tk.RIGHT)
	# d4min
	frame.paramframe.d4min = tk.Frame(frame.paramframe)
	frame.paramframe.d4min.pack()
	frame.paramframe.d4min.label = tk.Label(frame.paramframe.d4min, text = "d4min")
	frame.paramframe.d4min.label.pack(side = tk.LEFT)
	frame.paramframe.d4min.var = tk.StringVar()
	frame.paramframe.d4min.var.set("")
	frame.paramframe.d4min.value = tk.Entry(frame.paramframe.d4min, text = "")
	frame.paramframe.d4min.value.pack(side = tk.RIGHT)
	# d4max
	frame.paramframe.d4max = tk.Frame(frame.paramframe)
	frame.paramframe.d4max.pack()
	frame.paramframe.d4max.label = tk.Label(frame.paramframe.d4max, text = "d4max")
	frame.paramframe.d4max.label.pack(side = tk.LEFT)
	frame.paramframe.d4max.var = tk.StringVar()
	frame.paramframe.d4max.var.set("")
	frame.paramframe.d4max.value = tk.Entry(frame.paramframe.d4max, text = "")
	frame.paramframe.d4max.value.pack(side = tk.RIGHT)
	
	# Copyright
	frame.copyright = tk.Frame(frame)
	frame.copyright.pack(side = tk.BOTTOM)
	frame.copyright.text = tk.Label(frame.copyright, text = COPYRIGHT)
	frame.copyright.text.pack(side = tk.LEFT)
	
	return frame
