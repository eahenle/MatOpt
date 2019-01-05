"""
InkOptGUI.py
Adrian Henle
Voxtel, Inc.

Provides GUI elements for InkOpt
"""


import tkinter as tk
from InkOptConf import *
from InkOptHelpers import *
import InkOptParamWindow
import InkOptDataWindow
import InkOptPermuteWindow


class InkOptGUI:
	"""
	The root interface (main window) for InkOpt's GUI
	"""
	

	def Quit(self):
		"""
		Callback wrapper for InkOptHelpers.Quit()
		"""
		
		Quit(self.log)
	
	
	def __init__(self, master, inkopt):
		"""
		Set up logging, store InkOpt, and launch GUI Main Window
		"""
	
		# Start logging
		self.log = startLog(__name__)
		
		# The InkOpt object passed in at instantiation is our engine for running data tasks
		self.inkopt = inkopt
	
		# [Tk root]
		self.tkroot = tk.Frame(master)
		self.tkroot.pack()
	
		# Launch MainWindow
		self.MainWindow = self.MainWindow(self.tkroot, self.log)
		
	
	# ## Functionalize
	def MainWindow(self, tkroot = None, log = None):
		"""
		The Main Window GUI launcher
		"""
		
		# ## Add clever input plasticizer
		
		# Frame the Main Window
		log.debug("Building MainWindow")
		MainWindow = tk.Frame(tkroot)
		MainWindow.pack()
			
		# MainWindow >> ASCII Splash
		log.debug("Rendering Main Window >> ASCII splash")
		MainWindow.splash = tk.Frame(MainWindow, relief = FRAMERELIEF)
		MainWindow.splash.pack(side = tk.TOP)
		MainWindow.splash.art = tk.Label(MainWindow.splash, text=SPLASH)
		MainWindow.splash.art.pack()
	
		# MainWindow >> Button Panel
		log.debug("Building MainWindow >> Button Panel")
		MainWindow.buttons = tk.Frame(MainWindow, relief = FRAMERELIEF)
		MainWindow.buttons.pack()
		
		# MainWindow >> Button Panel >> Run Button
		MainWindow.buttons.runButton = tk.Button(MainWindow.buttons, text = RUNBUTTONTEXT, fg = RUNBUTTONCOLOR, command = self.Run)
		MainWindow.buttons.runButton.pack(side = tk.TOP)
		
		# MainWindow >> Button Panel >> Quit Button
		MainWindow.buttons.quitButton = tk.Button(MainWindow.buttons, text = EXITBUTTONTEXT, fg = EXITBUTTONCOLOR, command = self.Quit)
		MainWindow.buttons.quitButton.pack(side = tk.BOTTOM)
		
		# MainWindow >> Button Panel >> About Button
		MainWindow.buttons.helloButton = tk.Button(MainWindow.buttons, text = ABOUTBUTTONTEXT, command = self.about)
		MainWindow.buttons.helloButton.pack()
		
		# MainWindow >> Copyright
		MainWindow.copyright = tk.Frame(MainWindow)
		MainWindow.copyright.pack(side = tk.BOTTOM)
		MainWindow.copyright.text = tk.Label(MainWindow.copyright, text = COPYRIGHT)
		MainWindow.copyright.text.pack(side = tk.LEFT)
		
		return MainWindow
		
		
	def LoadParamWindow(self):
		"""
		Wrapper for launching the Parameter Window
		"""
		ParamWindow = tk.Toplevel()
		ParamWindow.title("Parameter Window")
		ParamWindow.frame = InkOptParamWindow.LoadParamWindow(ParamWindow, self.inkopt)
		ParamWindow.frame.pack()
		
		return ParamWindow
		
		
	# ## Fix the return
	def LoadDataWindow(self):
		"""
		Launches the Data Window
		"""
		
		DataWindow = tk.Toplevel() # ## Change this to store the toplevel objects as a list of Tk nodes
		DataWindow.title("Data Table Window")
		DataWindow.frame = InkOptDataWindow.LoadDataWindow(DataWindow, self.inkopt)
		DataWindow.frame.pack()
		
		# ## Are these being assigned somewhere?
		return DataWindow
		
		
	# ## Error: closing the windows doesn't destroy their top level Tk nodes!
		
		
	# ## Fix the return
	def LoadPermuteWindow(self):
		"""
		Launches the Permutation Window
		"""
		
		PermuteWindow = tk.Toplevel() # ## Change this to store the toplevel objects as a list of Tk nodes
		PermuteWindow.title("Permutation Window")
		PermuteWindow.frame = InkOptPermuteWindow.LoadPermuteWindow(PermuteWindow, self.inkopt)
		PermuteWindow.frame.pack()
		
		# ## Permutation Window should update InkOpt data and params with Data and Permutation Window field values before run
		return PermuteWindow
		
		
	def Run(self):
		"""
		Launches the InkOpt dialog windows (Parameter, Data, Permutation)
		"""
		
		log = self.log
		
		log.info("Launching GUI Controls")
		
		# ## Think these bits can be lambdalized
		# ## ...what does the "with" keyword do?
		
		# Open the Parameter Window
		try:
			if hasattr(self, "ParamWindow"):
				self.log.debug("Parameter Window already open.")
			else:
				self.ParamWindow = self.LoadParamWindow()
		except:
			raise
		
		# Open the Data Window
		try:
			if hasattr(self, "DataWindow"):
				log.debug("Data Window already open.")
				pass
			else:
				self.DataWindow = self.LoadDataWindow()
		except:
			raise
		
		# Open the Permutation Window
		try:
			if hasattr(self, "PermuteWindow"):
				log.debug("Permutation Window already open.")
				pass
			else:
				self.PermuteWindow = self.LoadPermuteWindow()
		except:
			raise
		
		
	# ## This has a glitch where the close button destroys the message frame but not the About Window
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
