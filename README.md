<center><h1>InkOpt version 10</h1>

<h4><i>Written by Adrian Henle, based on InkOpt_lite_inter_v7.py</i></h4>

<h3>CONFIDENTIAL PROPERTY OF VOXTEL, INC.</h3>

************************ A program to generate ink formulations. ************************</center>

<strong>Description</strong><br>
Each formulation is based on inputs of two lists of matrices and two lists of dopants.  Potential
formulations are probed for calculated parameters relevant to GRIN optics, and material
combinations with acceptable values are returned to the user in CSV format for viewing in
spreadsheet software.

<strong>Program Usage</strong><br>
By default, the program attempts to open in GUI mode with Tkinter.  If this fails, the console mode will execute.
Console mode can be disabled by setting INTERCONSOLE = DISABLED in InkOptConf.py.

On the console, inputs may be specified interactively or by specifying a parameter input file at runtime.
Input files must specify parameters in the order shown above. List-type data are entered
as space-delimited lists on a single line.  Non-numeric inputs are rejected.
	
Dopant percentages are permuted with a density of DOPSTEP samples in each range.  I.e., each step iterates the tested percentage
by (Max - Min)/DOPSTEP.  For testing of algorithms or for surveying many dopants and matrices, DOPSTEP may need to be reduced for
the sake of runtime.  DOPSTEP is defined in InkOptConf.py, but maybe this should be an input parameter.

<strong>Input Specifications</strong><br>
When taking input from the GUI, do it that way (<i>describe this better</i>).  When taking input interactively in the console, do
it that way (<i>seriously</i>).  When passing input in a file, etc. (<i>seriously.</i>)  No non-numeric input.  Lists are space-
delimited.  Volume % inputs in range [0, 100].
<ul>
<u>Input Variables</u>
	<li>Matrix1:		a list of matrix materials from the data table</li>
	<li>Matrix2:		a list of matrix materials from the data table</li>
	<li>Dopant1:		a list of potential dopants for Matrix1</li>
	<li>Dopant2:		a list of potential co-dopants for Matrix1</li>
	<li>Dopant3:		a list of potential dopants for Matrix2</li>
	<li>Dopant4:		a list of potential co-dopants for Matrix2</li>
	<li>MaxDeltaPdf:	the maximum allowable difference in Pd,f</li>
	<li>MaxPDeltadf:	the maximum allowable P(delta)d,f</li>
	<li>MinAvgDeltan:	the minimum average of (delta)n</li>
	<li>MinPercent1:	the minimum volume % loading of Dopant1</li>
	<li>MaxPercent1:	the maximum volume % loading of Dopant1</li>
	<li>MinPercent2:	the minimum volume % loading of Dopant2</li>
	<li>MaxPercent2:	the maximum volume % loading of Dopant2</li>
	<li>MinPercent3:	the minimum volume % loading of Dopant3</li>
	<li>MaxPercent3:	the maximum volume % loading of Dopant3</li>
	<li>MinPercent4:	the minimum volume % loading of Dopant4</li>
	<li>MaxPercent4:	the maximum volume % loading of Dopant4</li>
</ul>

<strong>Future Features (maybe</strong>)
<ul>
	<li>Generation of massive CSV or SQL databases (less user CPU time for finding good, complex, precise formulations)</li>
	<li>Training and application of predictive modeling for ultra-fast screening</li>
	<li>Handling of empty string for co-dopants.  Input cannot be blank, which may be inappropriate for some use cases.</li>
	<li>Parallelization (Priority. Do with the threading package, 'cause at least I know it's compatible with logging)</li>
	<li>Execution time estimation</li>
	<li>Background processing (safe UI exit w/ background conclusion of data task)</li>
	<li>Better documentation!</li>
	<li>Distributables for Unix, Windows, and Mac OS</li>
	<li>Web interface</li>
	<li>Android and iOS app integration ('cause... ok, no, probably not)</li>
	<li>Pickle storage of logs, outputs, data and parameter states, etc.</li>
</ul>
