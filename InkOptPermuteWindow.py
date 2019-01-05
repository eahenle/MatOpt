"""
InkOptPermuteWindow.py
"""

import tkinter as tk
from InkOptHelpers import *


def PackPermuteWindowFrame(master):
	"""
	Pack and prop Permutation Window
	"""
	
	frame = TkFrame(master)
	# ## Write helper functions for throwing a frame prop of given width or height
	frame.widthprop = WidthProp(master)
	
	return frame
	
	
def GOButton(inkopt):
	"""
	
	"""
	
	inkopt.permuteV7()
	inkopt.getOutput(inkopt.outputfile)
	
	
def PackControlFrame(master, inkopt):
	"""
	
	"""
	
	# Pack frame
	frame = TkFrame(master)
	
	# Output file entry field
	frame.outfile = TkFrame(frame)
	frame.outfile.var = tk.StringVar()
	frame.outfile.var.set(inkopt.outputfile)
	frame.outfile.field = tk.Entry(frame.outfile, text = frame.outfile.var.get(), textvar = frame.outfile.var)
	frame.outfile.field.pack(side = tk.LEFT)
	
	# GO button
	frame.gobutton = tk.Button(frame, text = "GO", command = lambda : GOButton(inkopt))
	frame.gobutton.pack(side = tk.RIGHT)
	
	return frame
	
	
def PackStatusFrame(master, inkopt):
	"""
	
	"""
	
	# Pack frame
	frame = TkFrame(master)
	
	# Do... other stuff?
	
	return frame


def LoadPermuteWindow(master, inkopt):
	"""
	
	"""
	
	# Start logging
	log = startLog(__name__)
	log.debug("Building PermuteWindow")
	
	# Pack window frame
	frame = PackPermuteWindowFrame(master)
	
	# Pack control frame
	frame.controlframe = PackControlFrame(frame, inkopt)
	
	# Pack status frame
	frame.statusframe = PackStatusFrame(frame, inkopt)
	
	# Pack copyright frame
	frame.copyright = TkFrame(frame)
	frame.copyright.text = tk.Label(frame.copyright, text = COPYRIGHT)
	frame.copyright.text.pack(side = tk.LEFT)
	
	return frame

