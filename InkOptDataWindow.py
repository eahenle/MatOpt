"""
InkOptDataWindow.py
Adrian Henle
Voxtel, Inc.

Code for the Data Window GUI
"""


import tkinter as tk
from InkOptHelpers import *


def PackDataWindowFrame(master):
	"""
	Pack and prop the primary frame for the Data Window
	"""
	
	# ## Implement this everywhere
	frame = TkFrame(master)
	
	# ## Implement this everywhere
	frame.widthprop = WidthProp(master)
	
	return frame
	
	
def LoadData(inkopt, input):
	"""
	Wrapper for InkOpt.readData
	"""
	
	inkopt.readData(input)
	
	
def PackLoadFrame(master, inkopt):
	"""
	Pack and populate the data loading frame
	"""
	
	# Pack the data frame
	frame = TkFrame(master)
	
	# Material data file variable
	frame.var = tk.StringVar()
	frame.var.set("material_table.csv")
	
	# Material data file field
	frame.value = tk.Entry(frame, text = frame.var.get(), textvar = frame.var)
	frame.value.pack(side = tk.RIGHT)
	
	# Pack file button
	frame.button = tk.Button(frame, text = "Load", command = lambda : LoadData(inkopt, frame.var.get()))
	frame.button.pack()
	
	return frame


def LoadDataWindow(master, inkopt):
	"""
	Build the Data Window
	"""
	
	# Window's log
	log = startLog(__name__)
	log.debug("Building DataWindow")
	
	# Window frame
	frame = PackDataWindowFrame(master)
	
	# Data loading frame
	frame.loadframe = PackLoadFrame(frame, inkopt)
	
	return frame
