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
	
	
def RenderDataFrame(dataframe, inkopt, log):
	"""
	Render all the fields in the Data frame
	"""
	# ## Check for existing rowframes and delete them (or something).  Best behavior: write a function that deletes a rowframe based on its varkey.  Implement here, and in the case of adding a new row to the data table with the same name as an existing row (update/replace by name key)
	
	# ## Column names
	columnframe = TkFrame(dataframe)
	columnframe.columns = [column for column in inkopt.data.columns]
	log.debug("Data columns: {}, {}, {}, {}".format(*columnframe.columns))
	columnframe.labels = []
	for column in columnframe.columns:
		columnframe.labels.append(TkFrame(columnframe))
		columnframe.labels[-1].label = tk.Label(columnframe, text = column)
	for label in columnframe.labels:
		label.pack(side = tk.LEFT)
	
	log.debug("dataframe.data:\n{}\n".format(dataframe.data))
	
	# Take each data row and put it into a new rowframe
	for Material in dataframe.data["Material"]:
		
		# Create the rowframe
		rowframe = TkFrame(dataframe)
		
		# Material
		rowframe.keyvar = tk.StringVar() # This is a handle for anything else in rowframe's [local] tree
		rowframe.keyvar.set(Material)
		rowframe.key = tk.Entry(rowframe, text = rowframe.keyvar.get(), textvar = rowframe.keyvar)
		rowframe.key.pack(side = tk.LEFT)
		# ## Enforce uniqueness of rowframe.key.var values... but more elegantly than by clobbering other rows.
		
		# Continue the rowframe with a text field for the value in each column of the material table
		# Make a field for each variable
		# ## Make a function for whipping up variables and connecting them to entries
		
		Indices = dataframe.data.loc[dataframe.data["Material"] == Material]
		
		rowframe.n486var = tk.StringVar()
		rowframe.n486var.set(Indices["n(486 nm)"])
		rowframe.n486 = tk.Entry(rowframe, text = rowframe.n486var.get(), textvar = rowframe.n486var)
		rowframe.n486.pack(side = tk.LEFT)
		
		rowframe.n587var = tk.StringVar()
		rowframe.n587var.set(Indices["n(587 nm)"])
		rowframe.n587 = tk.Entry(rowframe, text = rowframe.n587var.get(), textvar = rowframe.n587var)
		rowframe.n587.pack(side = tk.LEFT)
		
		rowframe.n656var = tk.StringVar()
		rowframe.n656var.set(Indices["n(656 nm)"])
		rowframe.n656 = tk.Entry(rowframe, text = rowframe.n656var.get(), textvar = rowframe.n656var)
		rowframe.n656.pack(side = tk.LEFT)

	
	
def LoadButton(dataframe, inkopt, input, log):
	"""
	Wrapper for InkOpt.readData
	"""
	
	# Read data into InkOpt
	inkopt.readData(input)
	
	# Copy InkOpt data into window frame
	dataframe.data = inkopt.getData()
	log.debug("Data:\n{}\n".format(dataframe.data))
	
	RenderDataFrame(dataframe, inkopt, log)
	
	
def PackLoadFrame(master, inkopt, log):
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
	frame.button = tk.Button(frame, text = "Load", command = lambda : LoadButton(master.dataframe, inkopt, frame.var.get(), log))
	frame.button.pack()
	
	return frame
	
	
def PackDataFrame(master, inkopt, log):
	"""
	Pack the Data frame
	"""
	
	frame = TkFrame(master)
	frame.data = inkopt.getData()
	
	return frame


def PackCopyright(master):
	"""
	Pack the copyright
	"""
	
	frame = TkFrame(master)
	frame.text = tk.Label(frame, text = COPYRIGHT)
	frame.text.pack()
	
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
	frame.loadframe = PackLoadFrame(frame, inkopt, log)
	
	# Data frame
	frame.dataframe = PackDataFrame(frame, inkopt, log)
	
	# Copyright
	frame.copyright = PackCopyright(frame)
	
	return frame
