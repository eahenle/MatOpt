InkOpt version 10

Written by Adrian Henle, based on InkOpt_lite_inter_v7.py

CONFIDENTIAL PROPERTY OF VOXTEL, INC.

************************ A program to generate ink formulations. ************************

Each formulation is based on inputs of two lists of matrices and two lists of dopants.  Potential
formulations are probed for calculated parameters relevant to GRIN optics, and material
combinations with acceptable values are returned to the user in CSV format for viewing in
spreadsheet software.

Input specifications:
	Matrix1:		a list of matrix materials from the data table
	Matrix2:		a list of matrix materials from the data table
	Dopant1:		a list of potential dopants for Matrix1
	Dopant2:		a list of potential co-dopants for Matrix1
	Dopant3:		a list of potential dopants for Matrix2
	Dopant4:		a list of potential co-dopants for Matrix2
	MaxDeltaPdf:	the maximum allowable difference in Pd,f
	MaxPDeltadf:	the maximum allowable P(delta)d,f
	MinAvgDeltan:	the minimum average of (delta)n
	MinPercent1:	the minimum volume % loading of Dopant1
	MaxPercent1:	the maximum volume % loading of Dopant1
	MinPercent2:	the minimum volume % loading of Dopant2
	MaxPercent2:	the maximum volume % loading of Dopant2
	MinPercent3:	the minimum volume % loading of Dopant3
	MaxPercent3:	the maximum volume % loading of Dopant3
	MinPercent4:	the minimum volume % loading of Dopant4
	MaxPercent4:	the maximum volume % loading of Dopant4

By default, the program attempts to open in GUI mode with Tkinter.  If this fails, the console mode will execute.
Console mode can be disabled by setting ENABLECONSOLE = False in InkOptConf.py

On the console, inputs may be specified interactively or by specifying a parameter input file at runtime.
Input files must specify parameters in the order shown above. List-type data are entered
as space-delimited lists on a single line.  Non-numeric inputs are rejected.
	
Dopant percentages are permuted with a density of DOPSTEP samples in each range.  I.e., each step
iterates the tested percentage by (Max - Min)/DOPSTEP

Future versions may include:
	Generation of massive CSV or SQL databases (minimal end-user compute time for finding
		good formulations with complex requirements)
	Training and application of predictive modeling for ultra-fast screening
	Handling of empty string for co-dopants.  There is no way to leave this input blank, which may be
		inappropriate for some use cases.
	Parallelization
	Execution time estimation
	Background processing (safe UI exit w/ background conclusion of data task)
