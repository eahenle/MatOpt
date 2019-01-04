"""
InkOptPermuteWindow.py
"""

import tkinter as tk
from InkOptHelpers import *


def PackPermuteWindowFrame(master):
	"""
	
	"""
	
	frame = tk.Frame(master, relief = FRAMERELIEF)
	frame.pack()
	# ## Write helper functions for throwing a frame prop of given width or height
	frame.widthprop = tk.Frame(frame, width = SMALLWINDOWX, height = 5, relief = FRAMERELIEF)
	frame.widthprop.pack(side = tk.TOP)
	
	return frame


def LoadPermuteWindow(master, inkopt):
	"""
	
	"""
	
	log = startLog(__name__)
	log.debug("Building PermuteWindow")
	
	frame = PackPermuteWindowFrame(master)
	
	return frame

