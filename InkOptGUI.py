"""
InkOptGUI.py
Adrian Henle
Voxtel, Inc.

Provides GUI elements for InkOpt
"""

import tkinter as tk
from InkOptConf import *

class InkOptGUI:
	"""
	The root interface (main window) for InkOpt's GUI
	"""
	
	def __init__(self, master, inkopt):
		"""
		Set up logging, store InkOpt, and launch GUI Main Window
		"""
	
		# Start logging
		self.log = logging.getLogger(__name__)
		self.log.setLevel(LOGLEVEL)
		self.loghandle = logging.StreamHandler()
		self.loghandle.setLevel(LOGLEVEL)
		self.loghandle.setFormatter(logging.Formatter(LOGFORMAT))
		self.log.addHandler(self.loghandle)
		self.log.info("Begin log")
		
		# The InkOpt object passed in at instantiation is our engine for running data tasks
		self.inkopt = inkopt
	
		# [Tk root]
		self.tkroot = tk.Frame(master)
		self.tkroot.pack()
	
		# MainWindow
		# ## Functionalize
		self.log.debug("Building MainWindow")
		self.MainWindow = tk.Frame(self.tkroot)
		self.MainWindow.pack()
			
		# MainWindow >> ASCII Splash
		self.log.debug("Rendering Main Window >> ASCII splash")
		self.MainWindow.splash = tk.Frame(self.MainWindow)
		self.MainWindow.splash.pack(side = tk.TOP)
		self.MainWindow.splash.art = tk.Label(self.MainWindow.splash, text=SPLASH)
		self.MainWindow.splash.art.pack()
	
		# MainWindow >> Button Panel
		self.log.debug("Building MainWindow >> Button Panel")
		self.buttons = tk.Frame(self.MainWindow)
		self.buttons.pack()
		
		# MainWindow >> Button Panel >> Run Button
		self.buttons.runButton = tk.Button(self.buttons, text = RUNBUTTONTEXT, fg = RUNBUTTONCOLOR, command = self.Run)
		self.buttons.runButton.pack(side = tk.TOP)
		
		# MainWindow >> Button Panel >> Quit Button
		self.buttons.quitButton = tk.Button(self.buttons, text = EXITBUTTONTEXT, fg = EXITBUTTONCOLOR, command = master.quit)
		self.buttons.quitButton.pack(side = tk.BOTTOM)
		
		# MainWindow >> Button Panel >> About Button
		self.helloButton = tk.Button(self.buttons, text = ABOUTBUTTONTEXT, command = self.about)
		self.helloButton.pack()
		
		# MainWindow >> Copyright
		self.copyright = tk.Frame(self.MainWindow)
		self.copyright.pack(side = tk.BOTTOM)
		self.copyright.text = tk.Label(master, text = COPYRIGHT)
		self.copyright.text.pack(side = tk.LEFT)
		
		
	def Run(self):
		"""
		Launches the InkOpt dialog windows (Parameter, Data, Permutation)
		"""
		
		self.log.info("Launching GUI Controls")
		
		# [Re]open the Parameter Window
		# ## Change this to test for window (don't destroy)
		# ## Functionalize
		try:
			self.ParamWindow.destroy()
			self.log.debug("Closed ParmeterWindow")
		except AttributeError:
			self.log.debug("ParameterWindow not open")
		except:
			raise
		self.log.debug("Building ParameterWindow")
		self.ParamWindow = tk.Toplevel() # ## Change this to store the toplevel objects as a list of Tk nodes
		self.ParamWindow.title(PARAMWINDOWTITLE)
		self.ParamWindow.frame = tk.Frame(self.ParamWindow)
		self.ParamWindow.frame.pack()
		self.ParamWindow.frame.widthprop = tk.Frame(self.ParamWindow.frame, width = SMALLWINDOWX, height = 0)
		self.ParamWindow.frame.widthprop.pack(side = tk.TOP)
		
		# Define the frame for loading from file
		self.ParamWindow.frame.loadframe = tk.Frame(self.ParamWindow.frame)
		self.ParamWindow.frame.loadframe.pack()
		self.ParamWindow.frame.loadframe.loadbutton = tk.Button(self.ParamWindow.frame.loadframe, text = "Load", command = self.loadParams)
		self.ParamWindow.frame.loadframe.loadbutton.pack(side = tk.LEFT)
		self.ParamWindow.frame.loadframe.inputfile = tk.StringVar()
		self.ParamWindow.frame.loadframe.inputfile.set("input.txt")
		self.ParamWindow.frame.loadframe.inputfield = tk.Entry(self.ParamWindow.frame.loadframe,
			text = self.ParamWindow.frame.loadframe.inputfile.get(), textvariable = self.ParamWindow.frame.loadframe.inputfile)
		self.ParamWindow.frame.loadframe.inputfield.pack(side = tk.RIGHT)
		
		# Define the frame for viewing loaded parameters
		self.ParamWindow.frame.paramframe = tk.Frame(self.ParamWindow.frame)
		self.ParamWindow.frame.paramframe.pack(side = tk.BOTTOM)
		
		"""Populate the parameter frame with tk.Label/tk.Entry (key/value) pairs"""
		# ## Functionalize
		# maxDiffPdfs
		self.ParamWindow.frame.paramframe.maxDiffPdfs = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.maxDiffPdfs.pack()
		self.ParamWindow.frame.paramframe.maxDiffPdfs.label = tk.Label(self.ParamWindow.frame.paramframe.maxDiffPdfs, text = "maxDiffPdfs")
		self.ParamWindow.frame.paramframe.maxDiffPdfs.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.maxDiffPdfs.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.maxDiffPdfs.var.set("")
		self.ParamWindow.frame.paramframe.maxDiffPdfs.value = tk.Entry(self.ParamWindow.frame.paramframe.maxDiffPdfs, text = "")
		self.ParamWindow.frame.paramframe.maxDiffPdfs.value.pack(side = tk.RIGHT)
		# maxPDf
		self.ParamWindow.frame.paramframe.maxPDf = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.maxPDf.pack()
		self.ParamWindow.frame.paramframe.maxPDf.label = tk.Label(self.ParamWindow.frame.paramframe.maxPDf, text = "maxPDf")
		self.ParamWindow.frame.paramframe.maxPDf.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.maxPDf.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.maxPDf.var.set("")
		self.ParamWindow.frame.paramframe.maxPDf.value = tk.Entry(self.ParamWindow.frame.paramframe.maxPDf, text = "")
		self.ParamWindow.frame.paramframe.maxPDf.value.pack(side = tk.RIGHT)
		# minVgrin
		self.ParamWindow.frame.paramframe.minVgrin = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.minVgrin.pack()
		self.ParamWindow.frame.paramframe.minVgrin.label = tk.Label(self.ParamWindow.frame.paramframe.minVgrin, text = "minVgrin")
		self.ParamWindow.frame.paramframe.minVgrin.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.minVgrin.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.minVgrin.var.set("")
		self.ParamWindow.frame.paramframe.minVgrin.value = tk.Entry(self.ParamWindow.frame.paramframe.minVgrin, text = "")
		self.ParamWindow.frame.paramframe.minVgrin.value.pack(side = tk.RIGHT)
		# minDnAvg
		self.ParamWindow.frame.paramframe.minDnAvg = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.minDnAvg.pack()
		self.ParamWindow.frame.paramframe.minDnAvg.label = tk.Label(self.ParamWindow.frame.paramframe.minDnAvg, text = "minDnAvg")
		self.ParamWindow.frame.paramframe.minDnAvg.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.minDnAvg.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.minDnAvg.var.set("")
		self.ParamWindow.frame.paramframe.minDnAvg.value = tk.Entry(self.ParamWindow.frame.paramframe.minDnAvg, text = "")
		self.ParamWindow.frame.paramframe.minDnAvg.value.pack(side = tk.RIGHT)
		# matrix1
		self.ParamWindow.frame.paramframe.matrix1 = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.matrix1.pack()
		self.ParamWindow.frame.paramframe.matrix1.label = tk.Label(self.ParamWindow.frame.paramframe.matrix1, text = "matrix1")
		self.ParamWindow.frame.paramframe.matrix1.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.matrix1.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.matrix1.var.set("")
		self.ParamWindow.frame.paramframe.matrix1.value = tk.Entry(self.ParamWindow.frame.paramframe.matrix1, text = "")
		self.ParamWindow.frame.paramframe.matrix1.value.pack(side = tk.RIGHT)
		# matrix2
		self.ParamWindow.frame.paramframe.matrix2 = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.matrix2.pack()
		self.ParamWindow.frame.paramframe.matrix2.label = tk.Label(self.ParamWindow.frame.paramframe.matrix2, text = "matrix2")
		self.ParamWindow.frame.paramframe.matrix2.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.matrix2.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.matrix2.var.set("")
		self.ParamWindow.frame.paramframe.matrix2.value = tk.Entry(self.ParamWindow.frame.paramframe.matrix2, text = "")
		self.ParamWindow.frame.paramframe.matrix2.value.pack(side = tk.RIGHT)
		# dopant1
		self.ParamWindow.frame.paramframe.dopant1 = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.dopant1.pack()
		self.ParamWindow.frame.paramframe.dopant1.label = tk.Label(self.ParamWindow.frame.paramframe.dopant1, text = "dopant1")
		self.ParamWindow.frame.paramframe.dopant1.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.dopant1.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.dopant1.var.set("")
		self.ParamWindow.frame.paramframe.dopant1.value = tk.Entry(self.ParamWindow.frame.paramframe.dopant1, text = "")
		self.ParamWindow.frame.paramframe.dopant1.value.pack(side = tk.RIGHT)
		# dopant2
		self.ParamWindow.frame.paramframe.dopant2 = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.dopant2.pack()
		self.ParamWindow.frame.paramframe.dopant2.label = tk.Label(self.ParamWindow.frame.paramframe.dopant2, text = "dopant2")
		self.ParamWindow.frame.paramframe.dopant2.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.dopant2.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.dopant2.var.set("")
		self.ParamWindow.frame.paramframe.dopant2.value = tk.Entry(self.ParamWindow.frame.paramframe.dopant2, text = "")
		self.ParamWindow.frame.paramframe.dopant2.value.pack(side = tk.RIGHT)
		# dopant3
		self.ParamWindow.frame.paramframe.dopant3 = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.dopant3.pack()
		self.ParamWindow.frame.paramframe.dopant3.label = tk.Label(self.ParamWindow.frame.paramframe.dopant3, text = "dopant3")
		self.ParamWindow.frame.paramframe.dopant3.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.dopant3.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.dopant3.var.set("")
		self.ParamWindow.frame.paramframe.dopant3.value = tk.Entry(self.ParamWindow.frame.paramframe.dopant3, text = "")
		self.ParamWindow.frame.paramframe.dopant3.value.pack(side = tk.RIGHT)
		# dopant4
		self.ParamWindow.frame.paramframe.dopant4 = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.dopant4.pack()
		self.ParamWindow.frame.paramframe.dopant4.label = tk.Label(self.ParamWindow.frame.paramframe.dopant4, text = "dopant4")
		self.ParamWindow.frame.paramframe.dopant4.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.dopant4.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.dopant4.var.set("")
		self.ParamWindow.frame.paramframe.dopant4.value = tk.Entry(self.ParamWindow.frame.paramframe.dopant4, text = "")
		self.ParamWindow.frame.paramframe.dopant4.value.pack(side = tk.RIGHT)
		# d1min
		self.ParamWindow.frame.paramframe.d1min = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.d1min.pack()
		self.ParamWindow.frame.paramframe.d1min.label = tk.Label(self.ParamWindow.frame.paramframe.d1min, text = "d1min")
		self.ParamWindow.frame.paramframe.d1min.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.d1min.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.d1min.var.set("")
		self.ParamWindow.frame.paramframe.d1min.value = tk.Entry(self.ParamWindow.frame.paramframe.d1min, text = "")
		self.ParamWindow.frame.paramframe.d1min.value.pack(side = tk.RIGHT)
		# d1max
		self.ParamWindow.frame.paramframe.d1max = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.d1max.pack()
		self.ParamWindow.frame.paramframe.d1max.label = tk.Label(self.ParamWindow.frame.paramframe.d1max, text = "d1max")
		self.ParamWindow.frame.paramframe.d1max.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.d1max.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.d1max.var.set("")
		self.ParamWindow.frame.paramframe.d1max.value = tk.Entry(self.ParamWindow.frame.paramframe.d1max, text = "")
		self.ParamWindow.frame.paramframe.d1max.value.pack(side = tk.RIGHT)
		# d2min
		self.ParamWindow.frame.paramframe.d2min = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.d2min.pack()
		self.ParamWindow.frame.paramframe.d2min.label = tk.Label(self.ParamWindow.frame.paramframe.d2min, text = "d2min")
		self.ParamWindow.frame.paramframe.d2min.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.d2min.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.d2min.var.set("")
		self.ParamWindow.frame.paramframe.d2min.value = tk.Entry(self.ParamWindow.frame.paramframe.d2min, text = "")
		self.ParamWindow.frame.paramframe.d2min.value.pack(side = tk.RIGHT)
		# d2max
		self.ParamWindow.frame.paramframe.d2max = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.d2max.pack()
		self.ParamWindow.frame.paramframe.d2max.label = tk.Label(self.ParamWindow.frame.paramframe.d2max, text = "d2max")
		self.ParamWindow.frame.paramframe.d2max.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.d2max.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.d2max.var.set("")
		self.ParamWindow.frame.paramframe.d2max.value = tk.Entry(self.ParamWindow.frame.paramframe.d2max, text = "")
		self.ParamWindow.frame.paramframe.d2max.value.pack(side = tk.RIGHT)
		# d3min
		self.ParamWindow.frame.paramframe.d3min = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.d3min.pack()
		self.ParamWindow.frame.paramframe.d3min.label = tk.Label(self.ParamWindow.frame.paramframe.d3min, text = "d3min")
		self.ParamWindow.frame.paramframe.d3min.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.d3min.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.d3min.var.set("")
		self.ParamWindow.frame.paramframe.d3min.value = tk.Entry(self.ParamWindow.frame.paramframe.d3min, text = "")
		self.ParamWindow.frame.paramframe.d3min.value.pack(side = tk.RIGHT)
		# d3max
		self.ParamWindow.frame.paramframe.d3max = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.d3max.pack()
		self.ParamWindow.frame.paramframe.d3max.label = tk.Label(self.ParamWindow.frame.paramframe.d3max, text = "d3max")
		self.ParamWindow.frame.paramframe.d3max.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.d3max.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.d3max.var.set("")
		self.ParamWindow.frame.paramframe.d3max.value = tk.Entry(self.ParamWindow.frame.paramframe.d3max, text = "")
		self.ParamWindow.frame.paramframe.d3max.value.pack(side = tk.RIGHT)
		# d4min
		self.ParamWindow.frame.paramframe.d4min = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.d4min.pack()
		self.ParamWindow.frame.paramframe.d4min.label = tk.Label(self.ParamWindow.frame.paramframe.d4min, text = "d4min")
		self.ParamWindow.frame.paramframe.d4min.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.d4min.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.d4min.var.set("")
		self.ParamWindow.frame.paramframe.d4min.value = tk.Entry(self.ParamWindow.frame.paramframe.d4min, text = "")
		self.ParamWindow.frame.paramframe.d4min.value.pack(side = tk.RIGHT)
		# d4max
		self.ParamWindow.frame.paramframe.d4max = tk.Frame(self.ParamWindow.frame.paramframe)
		self.ParamWindow.frame.paramframe.d4max.pack()
		self.ParamWindow.frame.paramframe.d4max.label = tk.Label(self.ParamWindow.frame.paramframe.d4max, text = "d4max")
		self.ParamWindow.frame.paramframe.d4max.label.pack(side = tk.LEFT)
		self.ParamWindow.frame.paramframe.d4max.var = tk.StringVar()
		self.ParamWindow.frame.paramframe.d4max.var.set("")
		self.ParamWindow.frame.paramframe.d4max.value = tk.Entry(self.ParamWindow.frame.paramframe.d4max, text = "")
		self.ParamWindow.frame.paramframe.d4max.value.pack(side = tk.RIGHT)
		
		# Copyright
		self.ParamWindow.copyright = tk.Frame(self.ParamWindow)
		self.ParamWindow.copyright.pack(side = tk.BOTTOM)
		self.ParamWindow.copyright.text = tk.Label(self.ParamWindow, text = COPYRIGHT)
		self.ParamWindow.copyright.text.pack(side = tk.LEFT)
		
		# [Re]open the Data Window
		# ## Change this to test for window (don't destroy)
		# ## Functionalize
		try:
			self.DataWindow.destroy()
		except AttributeError:
			pass
		except:
			raise
		self.DataWindow = tk.Toplevel() # ## Change this to store the toplevel objects as a list of Tk nodes
		self.DataWindow.title("Data Table Window")
		self.DataWindow.frame = tk.Frame(self.DataWindow, width = SMALLWINDOWX, height = SMALLWINDOWY)
		self.DataWindow.frame.pack()
		
		# [Re]open the Permutation Window
		# ## Change this to test for window (don't destroy)
		# ## Functionalize
		try:
			self.PermuteWindow.destroy()
		except AttributeError:
			pass
		except:
			raise
		self.PermuteWindow = tk.Toplevel() # ## Change this to store the toplevel objects as a list of Tk nodes
		self.PermuteWindow.title("Permutation Window")
		self.PermuteWindow.frame = tk.Frame(self.PermuteWindow, width = LARGEWINDOWX, height = LARGEWINDOWY)
		self.PermuteWindow.frame.pack()
		# ## Permutation Window should update InkOpt data and params with Data and Permutation Window field values before run
		
		
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
		
	def about(self):
		"""
		Window that shows an "about" message with a button to close it.
		"""
		tknode = tk.Toplevel()
		tknode.title = "About"
		AboutWindow = tk.Frame(tknode)
		AboutWindow.pack()
		message = tk.Message(AboutWindow, text = ABOUT)
		message.pack()
		self.log.info("About this software:\n{}".format(ABOUT))
		closeButton = tk.Button(AboutWindow, text = "Close", command = AboutWindow.destroy)
		closeButton.pack()
				
