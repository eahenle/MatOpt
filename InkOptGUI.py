"""
InkOptGUI.py
Adrian Henle
Voxtel, Inc.

Provides GUI elements for InkOpt
"""

import tkinter as tk
from InkOptConf import *

class MainWindow:
	"""
	The root interface (main window) for InkOpt's GUI
	"""
	def __init__(self, master, inkopt):
	
		self.log = logging.getLogger(__name__)
		self.log.setLevel(LOGLEVEL)
		self.loghandle = logging.StreamHandler()
		self.loghandle.setLevel(LOGLEVEL)
		self.loghandle.setFormatter(logging.Formatter(LOGFORMAT))
		self.log.addHandler(self.loghandle)
		self.log.info("Begin log")
		
		self.inkopt = inkopt
	
		self.frame = tk.Frame(master)
			
		self.textLabel = tk.Label(master, text=SPLASH) # ASCII logo element for main window
		self.textLabel.pack(side = tk.TOP) # Format for display
	
		self.buttons = tk.Frame(self.frame)
		self.buttons.runButton = tk.Button(self.buttons, text = "Run", fg = "green", command = self.Run)
		self.buttons.runButton.pack()
		self.buttons.quitButton = tk.Button(self.buttons, text = "Exit", fg = "red", command = master.quit)
		self.buttons.quitButton.pack(side = tk.BOTTOM)
		self.helloButton = tk.Button(self.buttons, text = "About", command = self.about)
		self.helloButton.pack(side = tk.BOTTOM)
		self.buttons.pack()
		self.frame.pack()
		
		self.copyright = tk.Label(master, text = "©2018 Voxtel, Inc.")
		self.copyright.pack(side = tk.LEFT)		
		
	def Run(self):
		self.log.info("Launching GUI Controls")
		
		# [Re]open the Parameter Window
		try:
			self.ParamWindow.destroy()
		except AttributeError:
			pass
		except:
			raise
		self.ParamWindow = tk.Toplevel()
		self.ParamWindow.title("Parameter Window")
		self.ParamWindow.frame = tk.Frame(self.ParamWindow)
		self.ParamWindow.frame.pack()
		
		# Define the frame for loading from file
		self.ParamWindow.frame.loadframe = tk.Frame(self.ParamWindow.frame)
		self.ParamWindow.frame.loadframe.pack()
		self.ParamWindow.frame.loadframe.loadbutton = tk.Button(self.ParamWindow.frame.loadframe, text = "Load", command = self.loadParams)
		self.ParamWindow.frame.loadframe.loadbutton.pack(side = tk.LEFT)
		self.ParamWindow.frame.loadframe.inputfile = tk.StringVar()
		self.ParamWindow.frame.loadframe.inputfile.set("material_data.csv")
		self.ParamWindow.frame.loadframe.inputfield = tk.Entry(self.ParamWindow.frame.loadframe,
			text = self.ParamWindow.frame.loadframe.inputfile.get(), textvariable = self.ParamWindow.frame.loadframe.inputfile)
		self.ParamWindow.frame.loadframe.inputfield.pack(side = tk.RIGHT)
		
		# Define the frame for viewing loaded parameters
		self.ParamWindow.frame.paramframe = tk.Frame(self.ParamWindow.frame)
		self.ParamWindow.frame.paramframe.pack(side = tk.BOTTOM)
		
		# Copyright
		self.ParamWindow.copyright = tk.Label(self.ParamWindow, text = "©2018 Voxtel, Inc.")
		self.ParamWindow.copyright.pack(side = tk.LEFT)
		
		# [Re]open the Data Window
		try:
			self.DataWindow.destroy()
		except AttributeError:
			pass
		except:
			raise
		self.DataWindow = tk.Toplevel()
		self.DataWindow.title("Data Table Window")
		self.DataWindow.frame = tk.Frame(self.DataWindow)
		self.DataWindow.frame.pack()
		
		# [Re]open the Permutation Window
		try:
			self.PermuteWindow.destroy()
		except AttributeError:
			pass
		except:
			raise
		self.PermuteWindow = tk.Toplevel()
		self.PermuteWindow.title("Permutation Window")
		self.PermuteWindow.frame = tk.Frame(self.PermuteWindow)
		self.PermuteWindow.frame.pack()
		
	def loadParams(self):
		self.inkopt.readData(self.ParamWindow.frame.loadframe.inputfile.get())
		
	def about(self):
		"""
		Window that shows an "about" message with a button to close it.
		"""
		AboutWindow = tk.Toplevel()
		AboutWindow.title = "About"
		message = tk.Message(AboutWindow, text = ABOUT)
		message.pack()
		self.log.info("About this software:\n{}".format(ABOUT))
		closeButton = tk.Button(AboutWindow, text = "Close", command = AboutWindow.destroy)
		closeButton.pack()
				
