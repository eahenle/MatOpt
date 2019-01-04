"""
InkOptParamWindow.py
"""


import tkinter as tk
from InkOptHelpers import *


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
		
	return
		
		
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
	
	# Copyright
	frame.copyright = tk.Frame(frame)
	frame.copyright.pack(side = tk.BOTTOM)
	frame.copyright.text = tk.Label(frame.copyright, text = COPYRIGHT)
	frame.copyright.text.pack(side = tk.LEFT)
	
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
	
	frame.paramframe.maxDiffPdfs = tk.Frame(frame.paramframe)
	frame.paramframe.maxPDf = tk.Frame(frame.paramframe)
	frame.paramframe.minVgrin = tk.Frame(frame.paramframe)
	frame.paramframe.minDnAvg = tk.Frame(frame.paramframe)
	frame.paramframe.matrix1 = tk.Frame(frame.paramframe)
	frame.paramframe.matrix2 = tk.Frame(frame.paramframe)
	frame.paramframe.dopant1 = tk.Frame(frame.paramframe)
	frame.paramframe.dopant2 = tk.Frame(frame.paramframe)
	frame.paramframe.dopant3 = tk.Frame(frame.paramframe)
	frame.paramframe.dopant4 = tk.Frame(frame.paramframe)
	frame.paramframe.d1min = tk.Frame(frame.paramframe)
	frame.paramframe.d1max = tk.Frame(frame.paramframe)
	frame.paramframe.d2min = tk.Frame(frame.paramframe)
	frame.paramframe.d2max = tk.Frame(frame.paramframe)
	frame.paramframe.d3min = tk.Frame(frame.paramframe)
	frame.paramframe.d3max = tk.Frame(frame.paramframe)
	frame.paramframe.d4min = tk.Frame(frame.paramframe)
	frame.paramframe.d4max = tk.Frame(frame.paramframe)
	
	varframes = {# ## Lambdalize
		"maxDiffPdfs" : frame.paramframe.maxDiffPdfs,
		"maxPDf" : frame.paramframe.maxPDf,
		"minVgrin" : frame.paramframe.minVgrin,
		"minDnAvg" : frame.paramframe.minDnAvg,
		"matrix1" : frame.paramframe.matrix1,
		"matrix2" : frame.paramframe.matrix2,
		"dopant1" : frame.paramframe.dopant1,
		"dopant2" : frame.paramframe.dopant2,
		"dopant3" : frame.paramframe.dopant3,
		"dopant4" : frame.paramframe.dopant4,
		"d1min" : frame.paramframe.d1min,
		"d1max" : frame.paramframe.d1max,
		"d2min" : frame.paramframe.d2min,
		"d2max" : frame.paramframe.d2max,
		"d3min" : frame.paramframe.d3min,
		"d3max" : frame.paramframe.d3max,
		"d4min" : frame.paramframe.d4min,
		"d4max" : frame.paramframe.d4max
	}
	
	for label, varframe in varframes.items():
		varframe.pack()
		varframe.label = tk.Label(varframe, text = label)
		varframe.label.pack(side = tk.LEFT)
		varframe.var = tk.StringVar()
		varframe.var.set("")
		varframe.value = tk.Entry(varframe, text = "")
		varframe.value.pack(side = tk.RIGHT)
	
	return frame
