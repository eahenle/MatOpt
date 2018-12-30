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
	
Inputs may be specified interactively, or by specifying a parameter input file at runtime.
Input files must specify parameters in the order shown above. List-type data are entered
as space-delimited lists on a single line.  Non-numeric inputs are rejected.
	
Dopant percentages are permuted with a density of DOPSTEP samples in each range.  I.e., each step
iterates the tested percentage by (Max - Min)/DOPSTEP

Future versions may include:
	GUI
	Generation of massive SQL databases (minimal end-user compute time for finding
		good formulations with complex requirements)
	Training and application of predictive modeling for ultra-fast screening



	
	
	
	
Dn486 = (n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1-Pct3-Pct4))
Dn587 = (n1_587*Pct1+n2_587*Pct2+np1_587*(1-Pct1-Pct2))-(n3_587*Pct3+n4_587*Pct4+np2_587*(1-Pct3-Pct4))                                 
Dn656 = (n1_656*Pct1+n2_656*Pct2+np1_656*(1-Pct1-Pct2))-(n3_656*Pct3+n4_656*Pct4+np2_656*(1-Pct3-Pct4))                                 





Pdf_hi = ((n1_587*Pct1+n2_587*Pct2+np1_587*(1-Pct1-Pct2))-(n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2)))
Pdf_hi = Pdf_hi/((n1_656*Pct1+n2_656*Pct2+np1_656*(1-Pct1-Pct2))-(n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2)))





Pdf_lo = ((n3_587*Pct3+n4_587*Pct4+np2_587*(1-Pct3-Pct4))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1-Pct3-Pct4)))
Pdf_lo = Pdf_lo/((n3_656*Pct3+n4_656*Pct4+np2_656*(1-Pct3-Pct4))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1- Pct3- Pct4)))                                  





if Dn656 == Dn486:
	PDf = 1e10
else:
	PDf = (Dn587-Dn486)/(Dn656 - Dn486)

	
	
	
if Dn486 == Dn656:
	Vgrin = 1e10
else: 
	Vgrin = Dn587/(Dn486 - Dn656)

	
	
	

Dnavg = (Dn486 + Dn587 + Dn656)/3


VALIDATION:
	Make dopant/co-dopant lists disjoint sets
	
	
	
ERROR CASE
	Empty string for co-dopants.  There is no way to leave this input blank, which may be
	inappropriate for some use cases.
	Possible fix: specify format for empty input.
	
ERROR CASE
	Cannot interrupt with Ctrl+C.
	Possible fix: SIG handler