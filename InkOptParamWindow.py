"""
InkOptParamWindow.py
"""


import tkinter as tk
from InkOptHelpers import *


# ## Future home of the code for the Parameter Window
# ## May need to pass in Tk node, return ParamWindow frame

class ParamWindow:
	"""
	Launches the Parameter Window
	"""
		
		
	def loadParams(self):
		"""
		Trigger the InkOpt engine to read input parameters from the input file indicated in the Parameter Window.
		Populate Parameter Window fields with values from input.
		"""
		
		self.log.debug("Entering loadParams()")
		
		# Get parameters from input file via InkOpt.setParams()
		self.log.debug("Getting parameters from {}".format(self.ParamWindow.frame.loadframe.inputfile.get()))
		self.inkopt.setParams(self.ParamWindow.frame.loadframe.inputfile.get())
		self.log.debug("Parameters:\n{}\n".format(*self.inkopt.params))
		
		# List of Parameter Window fields
		self.ParamWindow.params = {
			"maxDiffPdfs" : self.ParamWindow.frame.paramframe.maxDiffPdfs,
			"maxPDf" : self.ParamWindow.frame.paramframe.maxPDf,
			"minVgrin" : self.ParamWindow.frame.paramframe.minVgrin,
			"minDnAvg" : self.ParamWindow.frame.paramframe.minDnAvg,
			"matrix1" : self.ParamWindow.frame.paramframe.matrix1,
			"matrix2" : self.ParamWindow.frame.paramframe.matrix2,
			"dopant1" : self.ParamWindow.frame.paramframe.dopant1,
			"dopant2" : self.ParamWindow.frame.paramframe.dopant2,
			"dopant3" : self.ParamWindow.frame.paramframe.dopant3,
			"dopant4" : self.ParamWindow.frame.paramframe.dopant4,
			"d1min" : self.ParamWindow.frame.paramframe.d1min,
			"d1max" : self.ParamWindow.frame.paramframe.d1max,
			"d2min" : self.ParamWindow.frame.paramframe.d2min,
			"d2max" : self.ParamWindow.frame.paramframe.d2max,
			"d3min" : self.ParamWindow.frame.paramframe.d3min,
			"d3max" : self.ParamWindow.frame.paramframe.d3max,
			"d4min" : self.ParamWindow.frame.paramframe.d4min,
			"d4max" : self.ParamWindow.frame.paramframe.d4max
		}
		
		self.log.debug("ParamWindow.params.items():\n{}\n".format(self.ParamWindow.params.items()))
		
		# Copy parameters into window field stringvars and refresh field text
		for param in self.ParamWindow.params.items():
			self.log.debug("Setting {} to *{}".format(param[0], [*self.inkopt.params["{}".format(param[0])]]))
			# Set value
			if len([*self.inkopt.params["{}".format(param[0])]]) == 1:
				param[1].var.set(*self.inkopt.params["{}".format(param[0])])
			else:
				param[1].var.set([*self.inkopt.params["{}".format(param[0])]]) # ## This could be done better to avoid weirdness in the UI
			# Refresh field
			param[1].value.delete(0, tk.END)
			param[1].value.insert(0, param[1].var.get())
		
		self.log.debug("paramframe.*.var: {}\n".format([
			self.ParamWindow.frame.paramframe.maxDiffPdfs.var.get(),
			self.ParamWindow.frame.paramframe.maxPDf.var.get(),
			"...",
			self.ParamWindow.frame.paramframe.d4max.var.get()
			]))
		self.log.debug("inkopt.params: {}\n".format([
			*self.inkopt.params["maxDiffPdfs"],
			*self.inkopt.params["maxDiffPdfs"],
			*self.inkopt.params["maxPDf"],
			"...",
			*self.inkopt.params["d4max"]
			]))
		
		
		def __init__(self):
		
		# Build the window frame
			self.log = startLog(__name__)
			self.log.debug("Building ParameterWindow")
			ParamWindow = tk.Toplevel() # ## Change this to store the toplevel objects as a list of Tk nodes
			ParamWindow.title(PARAMWINDOWTITLE)
			ParamWindow.frame = tk.Frame(ParamWindow)
			ParamWindow.frame.pack()
			ParamWindow.frame.widthprop = tk.Frame(ParamWindow.frame, width = SMALLWINDOWX, height = 0)
			ParamWindow.frame.widthprop.pack(side = tk.TOP)
			
			# Define the frame for loading from file
			ParamWindow.frame.loadframe = tk.Frame(ParamWindow.frame)
			ParamWindow.frame.loadframe.pack()
			ParamWindow.frame.loadframe.loadbutton = tk.Button(ParamWindow.frame.loadframe, text = "Load", command = self.loadParams)
			ParamWindow.frame.loadframe.loadbutton.pack(side = tk.LEFT)
			ParamWindow.frame.loadframe.inputfile = tk.StringVar()
			ParamWindow.frame.loadframe.inputfile.set("input.txt")
			ParamWindow.frame.loadframe.inputfield = tk.Entry(ParamWindow.frame.loadframe,
				text = ParamWindow.frame.loadframe.inputfile.get(), textvariable = ParamWindow.frame.loadframe.inputfile)
			ParamWindow.frame.loadframe.inputfield.pack(side = tk.RIGHT)
			
			# Define the frame for viewing loaded parameters
			ParamWindow.frame.paramframe = tk.Frame(ParamWindow.frame)
			ParamWindow.frame.paramframe.pack(side = tk.BOTTOM)
			
			"""Populate the parameter frame with tk.Label/tk.Entry (key/value) pairs"""
			# ## Functionalize
			# maxDiffPdfs
			ParamWindow.frame.paramframe.maxDiffPdfs = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.maxDiffPdfs.pack()
			ParamWindow.frame.paramframe.maxDiffPdfs.label = tk.Label(ParamWindow.frame.paramframe.maxDiffPdfs, text = "maxDiffPdfs")
			ParamWindow.frame.paramframe.maxDiffPdfs.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.maxDiffPdfs.var = tk.StringVar()
			ParamWindow.frame.paramframe.maxDiffPdfs.var.set("")
			ParamWindow.frame.paramframe.maxDiffPdfs.value = tk.Entry(ParamWindow.frame.paramframe.maxDiffPdfs, text = "")
			ParamWindow.frame.paramframe.maxDiffPdfs.value.pack(side = tk.RIGHT)
			# maxPDf
			ParamWindow.frame.paramframe.maxPDf = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.maxPDf.pack()
			ParamWindow.frame.paramframe.maxPDf.label = tk.Label(ParamWindow.frame.paramframe.maxPDf, text = "maxPDf")
			ParamWindow.frame.paramframe.maxPDf.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.maxPDf.var = tk.StringVar()
			ParamWindow.frame.paramframe.maxPDf.var.set("")
			ParamWindow.frame.paramframe.maxPDf.value = tk.Entry(ParamWindow.frame.paramframe.maxPDf, text = "")
			ParamWindow.frame.paramframe.maxPDf.value.pack(side = tk.RIGHT)
			# minVgrin
			ParamWindow.frame.paramframe.minVgrin = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.minVgrin.pack()
			ParamWindow.frame.paramframe.minVgrin.label = tk.Label(ParamWindow.frame.paramframe.minVgrin, text = "minVgrin")
			ParamWindow.frame.paramframe.minVgrin.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.minVgrin.var = tk.StringVar()
			ParamWindow.frame.paramframe.minVgrin.var.set("")
			ParamWindow.frame.paramframe.minVgrin.value = tk.Entry(ParamWindow.frame.paramframe.minVgrin, text = "")
			ParamWindow.frame.paramframe.minVgrin.value.pack(side = tk.RIGHT)
			# minDnAvg
			ParamWindow.frame.paramframe.minDnAvg = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.minDnAvg.pack()
			ParamWindow.frame.paramframe.minDnAvg.label = tk.Label(ParamWindow.frame.paramframe.minDnAvg, text = "minDnAvg")
			ParamWindow.frame.paramframe.minDnAvg.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.minDnAvg.var = tk.StringVar()
			ParamWindow.frame.paramframe.minDnAvg.var.set("")
			ParamWindow.frame.paramframe.minDnAvg.value = tk.Entry(ParamWindow.frame.paramframe.minDnAvg, text = "")
			ParamWindow.frame.paramframe.minDnAvg.value.pack(side = tk.RIGHT)
			# matrix1
			ParamWindow.frame.paramframe.matrix1 = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.matrix1.pack()
			ParamWindow.frame.paramframe.matrix1.label = tk.Label(ParamWindow.frame.paramframe.matrix1, text = "matrix1")
			ParamWindow.frame.paramframe.matrix1.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.matrix1.var = tk.StringVar()
			ParamWindow.frame.paramframe.matrix1.var.set("")
			ParamWindow.frame.paramframe.matrix1.value = tk.Entry(ParamWindow.frame.paramframe.matrix1, text = "")
			ParamWindow.frame.paramframe.matrix1.value.pack(side = tk.RIGHT)
			# matrix2
			ParamWindow.frame.paramframe.matrix2 = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.matrix2.pack()
			ParamWindow.frame.paramframe.matrix2.label = tk.Label(ParamWindow.frame.paramframe.matrix2, text = "matrix2")
			ParamWindow.frame.paramframe.matrix2.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.matrix2.var = tk.StringVar()
			ParamWindow.frame.paramframe.matrix2.var.set("")
			ParamWindow.frame.paramframe.matrix2.value = tk.Entry(ParamWindow.frame.paramframe.matrix2, text = "")
			ParamWindow.frame.paramframe.matrix2.value.pack(side = tk.RIGHT)
			# dopant1
			ParamWindow.frame.paramframe.dopant1 = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.dopant1.pack()
			ParamWindow.frame.paramframe.dopant1.label = tk.Label(ParamWindow.frame.paramframe.dopant1, text = "dopant1")
			ParamWindow.frame.paramframe.dopant1.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.dopant1.var = tk.StringVar()
			ParamWindow.frame.paramframe.dopant1.var.set("")
			ParamWindow.frame.paramframe.dopant1.value = tk.Entry(ParamWindow.frame.paramframe.dopant1, text = "")
			ParamWindow.frame.paramframe.dopant1.value.pack(side = tk.RIGHT)
			# dopant2
			ParamWindow.frame.paramframe.dopant2 = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.dopant2.pack()
			ParamWindow.frame.paramframe.dopant2.label = tk.Label(ParamWindow.frame.paramframe.dopant2, text = "dopant2")
			ParamWindow.frame.paramframe.dopant2.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.dopant2.var = tk.StringVar()
			ParamWindow.frame.paramframe.dopant2.var.set("")
			ParamWindow.frame.paramframe.dopant2.value = tk.Entry(ParamWindow.frame.paramframe.dopant2, text = "")
			ParamWindow.frame.paramframe.dopant2.value.pack(side = tk.RIGHT)
			# dopant3
			ParamWindow.frame.paramframe.dopant3 = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.dopant3.pack()
			ParamWindow.frame.paramframe.dopant3.label = tk.Label(ParamWindow.frame.paramframe.dopant3, text = "dopant3")
			ParamWindow.frame.paramframe.dopant3.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.dopant3.var = tk.StringVar()
			ParamWindow.frame.paramframe.dopant3.var.set("")
			ParamWindow.frame.paramframe.dopant3.value = tk.Entry(ParamWindow.frame.paramframe.dopant3, text = "")
			ParamWindow.frame.paramframe.dopant3.value.pack(side = tk.RIGHT)
			# dopant4
			ParamWindow.frame.paramframe.dopant4 = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.dopant4.pack()
			ParamWindow.frame.paramframe.dopant4.label = tk.Label(ParamWindow.frame.paramframe.dopant4, text = "dopant4")
			ParamWindow.frame.paramframe.dopant4.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.dopant4.var = tk.StringVar()
			ParamWindow.frame.paramframe.dopant4.var.set("")
			ParamWindow.frame.paramframe.dopant4.value = tk.Entry(ParamWindow.frame.paramframe.dopant4, text = "")
			ParamWindow.frame.paramframe.dopant4.value.pack(side = tk.RIGHT)
			# d1min
			ParamWindow.frame.paramframe.d1min = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.d1min.pack()
			ParamWindow.frame.paramframe.d1min.label = tk.Label(ParamWindow.frame.paramframe.d1min, text = "d1min")
			ParamWindow.frame.paramframe.d1min.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.d1min.var = tk.StringVar()
			ParamWindow.frame.paramframe.d1min.var.set("")
			ParamWindow.frame.paramframe.d1min.value = tk.Entry(ParamWindow.frame.paramframe.d1min, text = "")
			ParamWindow.frame.paramframe.d1min.value.pack(side = tk.RIGHT)
			# d1max
			ParamWindow.frame.paramframe.d1max = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.d1max.pack()
			ParamWindow.frame.paramframe.d1max.label = tk.Label(ParamWindow.frame.paramframe.d1max, text = "d1max")
			ParamWindow.frame.paramframe.d1max.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.d1max.var = tk.StringVar()
			ParamWindow.frame.paramframe.d1max.var.set("")
			ParamWindow.frame.paramframe.d1max.value = tk.Entry(ParamWindow.frame.paramframe.d1max, text = "")
			ParamWindow.frame.paramframe.d1max.value.pack(side = tk.RIGHT)
			# d2min
			ParamWindow.frame.paramframe.d2min = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.d2min.pack()
			ParamWindow.frame.paramframe.d2min.label = tk.Label(ParamWindow.frame.paramframe.d2min, text = "d2min")
			ParamWindow.frame.paramframe.d2min.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.d2min.var = tk.StringVar()
			ParamWindow.frame.paramframe.d2min.var.set("")
			ParamWindow.frame.paramframe.d2min.value = tk.Entry(ParamWindow.frame.paramframe.d2min, text = "")
			ParamWindow.frame.paramframe.d2min.value.pack(side = tk.RIGHT)
			# d2max
			ParamWindow.frame.paramframe.d2max = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.d2max.pack()
			ParamWindow.frame.paramframe.d2max.label = tk.Label(ParamWindow.frame.paramframe.d2max, text = "d2max")
			ParamWindow.frame.paramframe.d2max.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.d2max.var = tk.StringVar()
			ParamWindow.frame.paramframe.d2max.var.set("")
			ParamWindow.frame.paramframe.d2max.value = tk.Entry(ParamWindow.frame.paramframe.d2max, text = "")
			ParamWindow.frame.paramframe.d2max.value.pack(side = tk.RIGHT)
			# d3min
			ParamWindow.frame.paramframe.d3min = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.d3min.pack()
			ParamWindow.frame.paramframe.d3min.label = tk.Label(ParamWindow.frame.paramframe.d3min, text = "d3min")
			ParamWindow.frame.paramframe.d3min.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.d3min.var = tk.StringVar()
			ParamWindow.frame.paramframe.d3min.var.set("")
			ParamWindow.frame.paramframe.d3min.value = tk.Entry(ParamWindow.frame.paramframe.d3min, text = "")
			ParamWindow.frame.paramframe.d3min.value.pack(side = tk.RIGHT)
			# d3max
			ParamWindow.frame.paramframe.d3max = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.d3max.pack()
			ParamWindow.frame.paramframe.d3max.label = tk.Label(ParamWindow.frame.paramframe.d3max, text = "d3max")
			ParamWindow.frame.paramframe.d3max.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.d3max.var = tk.StringVar()
			ParamWindow.frame.paramframe.d3max.var.set("")
			ParamWindow.frame.paramframe.d3max.value = tk.Entry(ParamWindow.frame.paramframe.d3max, text = "")
			ParamWindow.frame.paramframe.d3max.value.pack(side = tk.RIGHT)
			# d4min
			ParamWindow.frame.paramframe.d4min = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.d4min.pack()
			ParamWindow.frame.paramframe.d4min.label = tk.Label(ParamWindow.frame.paramframe.d4min, text = "d4min")
			ParamWindow.frame.paramframe.d4min.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.d4min.var = tk.StringVar()
			ParamWindow.frame.paramframe.d4min.var.set("")
			ParamWindow.frame.paramframe.d4min.value = tk.Entry(ParamWindow.frame.paramframe.d4min, text = "")
			ParamWindow.frame.paramframe.d4min.value.pack(side = tk.RIGHT)
			# d4max
			ParamWindow.frame.paramframe.d4max = tk.Frame(ParamWindow.frame.paramframe)
			ParamWindow.frame.paramframe.d4max.pack()
			ParamWindow.frame.paramframe.d4max.label = tk.Label(ParamWindow.frame.paramframe.d4max, text = "d4max")
			ParamWindow.frame.paramframe.d4max.label.pack(side = tk.LEFT)
			ParamWindow.frame.paramframe.d4max.var = tk.StringVar()
			ParamWindow.frame.paramframe.d4max.var.set("")
			ParamWindow.frame.paramframe.d4max.value = tk.Entry(ParamWindow.frame.paramframe.d4max, text = "")
			ParamWindow.frame.paramframe.d4max.value.pack(side = tk.RIGHT)
			
			# Copyright
			ParamWindow.copyright = tk.Frame(ParamWindow)
			ParamWindow.copyright.pack(side = tk.BOTTOM)
			ParamWindow.copyright.text = tk.Label(ParamWindow, text = COPYRIGHT)
			ParamWindow.copyright.text.pack(side = tk.LEFT)
