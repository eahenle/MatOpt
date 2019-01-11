<center>
<img src = logo.png></img>
<h1>InkOpt version 10</h1>

<h4><i>Written by Adrian Henle, based on InkOpt_lite_inter_v7.py</i></h4>

<h3>CONFIDENTIAL PROPERTY OF VOXTEL, INC.</h3>

************************ A program to generate ink formulations. ************************</center>

<strong> Description </strong><br>
Each formulation is based on inputs of two lists of matrices and two lists of dopants.  Potential
formulations are probed for calculated parameters relevant to GRIN optics, and material
combinations with acceptable values are returned to the user in CSV format for viewing in
spreadsheet software.

<strong> Program Usage </strong><br>
To open on the command line, use one of these:
<ul>
	<li> ./InkOpt_v10.py <i> (Unix) </i> </li>
	<li> ./runInkOpt.sh <i> (Unix) </i> </li>
	<li> python3 InkOpt_v10.py <i> (Unix and Windows)</i> </li>
	<li> ./runInkOpt.bat <i> (Windows) </i> </li>
</ul>
runInkOpt.sh may be usable as a double-clickable program launcher in Unix/Linux/Mac OS.
runInkOpt.bat is usable as a double-clickable program launcher in Windows.

Python must be installed on the system.  Required packages are installed automatically.

By default, the program attempts to open in GUI mode with Tkinter.  If this fails, the console mode will execute.
Console mode can be disabled by setting INTERCONSOLE = DISABLED in InkOptConf.py.

In GUI mode, load parameters and material data from file inputs in the appropriate windows.
The values will be filled in to text fields in the windows.
Future versions will include the ability to edit these fields and have the field values be read back in before permutation
algoithms are run.
After loading, press GO in the Permutation Window.

On the console, inputs may be specified interactively or by specifying a parameter input file at runtime.
Input files must specify parameters in the order shown above. List-type data are entered
as space-delimited lists on a single line.  Non-numeric inputs are rejected.
	
Dopant percentages are permuted with a density of DOPSTEP samples in each range.
I.e., each step iterates the tested percentage by (Max - Min)/DOPSTEP.
For testing of algorithms or for surveying many dopants and matrices, DOPSTEP may need to be reduced for the sake of
runtime.  DOPSTEP is defined in InkOptConf.py, but maybe this should be an input parameter.

<strong> Input Specifications </strong>
<br>
When taking input from the GUI, do it that way (<i>describe this better</i>).  When taking input interactively in the 
console, do it that way (<i>seriously</i>).  When passing input in a file, etc. (<i>seriously.</i>)  Numeric input only. 
Lists are space-delimited.  Volume % inputs in range [0, 100].
<ul>
<u> Input Variables </u>
	<li> Matrix1:		a list of matrix materials from the data table </li>
	<li> Matrix2:		a list of matrix materials from the data table </li>
	<li> Dopant1:		a list of potential dopants for Matrix1 </li>
	<li> Dopant2:		a list of potential co-dopants for Matrix1 </li>
	<li> Dopant3:		a list of potential dopants for Matrix2 </li>
	<li> Dopant4:		a list of potential co-dopants for Matrix2 </li>
	<li> MaxDeltaPdf:	the maximum allowable difference in Pd,f </li>
	<li> MaxPDeltadf:	the maximum allowable P(delta)d,f </li>
	<li> MinAvgDeltan:	the minimum average of (delta)n </li>
	<li> MinPercent1:	the minimum volume % loading of Dopant1 </li>
	<li> MaxPercent1:	the maximum volume % loading of Dopant1 </li>
	<li> MinPercent2:	the minimum volume % loading of Dopant2 </li>
	<li> MaxPercent2:	the maximum volume % loading of Dopant2 </li>
	<li> MinPercent3:	the minimum volume % loading of Dopant3 </li>
	<li> MaxPercent3:	the maximum volume % loading of Dopant3 </li>
	<li> MinPercent4:	the minimum volume % loading of Dopant4 </li>
	<li> MaxPercent4:	the maximum volume % loading of Dopant4 </li>
</ul>

<strong> Development </strong>


Version 10.19

<u> Bugs by Priority </u>
<ul>
<u> Priority 1 </u>
	<li> Algorithm has not been validated against previous full implementation! <br>
	Run v7 algorithm original implementation on inputs designed to take 2-5 minutes to complete.  Run v7 algorithm new
	implementation on same material data and input parameters, with sampling density chosen to match the number of samples
	between implementations.  3 input sets.  Time each run; calculate average permutations tested per minute, and verify that
	similar results are obtained.
	</li>
</ul>
<ul>
<u> Priority 2 </u>
	<li> Permutation window GO button needs to trigger update of InkOpt data and parameters before running permutations. </li>
</ul>
<ul>
<u> Priority 3 </u>
	<li> InkOpt_v10.py: No signal handling </li>
	<li> InkOptParamWindow.py: <br>
	List-type data in text fields has extra characters.
	Structure is strongly hard-coded for current InkOpt data types.  Should be made more flexible.
	</li>
	<li> Closing windows doesn't kill tk.Toplevel objects, so re-clicking LAUNCH OPTIMIZER doesn't re-open closed windows.<br>
	Possible fix: re-factor button command to run pack() on window contents to render it up again.<br>
	Other possible fix: (try first; are the windows' frames destroyed?) set event handlers on destruction of window frames for destruction of Toplevel parents.
	</li>
	<li> InkOpt_v10.py: <br> 
	in interConsole, hacky <br>
	in interConsole, output formatting issue
	</li>
	<li> Overuse of "self." and excessive object name chaining thoughout the code </li>
	<li> Large-scale try/except/finally block encapsulation for most robust/stable program </li>
	<li> InkOptGUI.py: <br>
	MainWindow() should be chunked up <br>
	Check out the return situation on LoadDataWindow() and LoadPermuteWindow() <br>
	Run() logic can be functionalized <br>
	</li>
	<li> Creation of connected tk.StringVar and tk.Entry objects should be handled by a helper function. </li>
	<li> runkInkOpt.bat: <br>
	No abstraction for input file
	</li>
	<li> Figure out how to use packages effectively </li>
	<li> INFO and ERROR logging should be done via StreamHandler, and DEBUG done via FileHandler </li>
	<li> InkOptHelpers.py: <br>
	Quit() needs some more intelligent message handling <br>
	Quit() should be integrated into signal and error handlers program-wide
	</li>
	<li> Program launch has become VERY slow! ...this might be because of OneDrive moving files to non-local storage.</li>
	<li> Under Windows, Tk renders a crisp sans-serif font.  Under Unix, it renders a blurry serif font. </li>
</ul>
<br>

<u> Future Features by Priority </u>

<ul>
	<u> Priority 1 </u>
	<li> Upgrade all .txt and .csv operations to .xlsx </li>
	<li> Parallelization (Priority. Do with the threading package, 'cause at least I know it's compatible with logging) </li>
	<li> More controls on the Permute Window (e.g. sampling density), and better status output </li>
	<li> Background processing (safe UI exit w/ background conclusion of data task) </li>
	<li> Distributables for Unix, Windows, and Mac OS </li>
	<li> Better input validation </li>
	<li> Window management by tracking and destroying tk.Toplevel objects (list in InkOptGUI) </li>
	<li> InkOptDataWindow.py: <br>
	In RenderDataFrame(), check for exisiting rowframes before making new ones.  Update existing rowframes by varkey. Enforce uniqueness. <br>
	In RenderDataFrame(), attempts at labeling the columns are failing
	</li>
</ul>
<ul>
	<u> Priority 2 </u>
	
	<li> Better documentation! </li>
	<li> Handling of empty string for co-dopants.  Input cannot be blank, which may be inappropriate for some use cases. </li>
	<li> Training and application of predictive modeling for ultra-fast screening </li>
	<li> Pickle storage of logs, outputs, data and parameter states, etc. </li>
</ul>
<ul>
	<u> Priority 3 </u>
	
	<li> Execution time estimation </li>
	<li> Web interface </li>
	<li> Generation of massive CSV or SQL databases (less user CPU time for finding good, complex, precise formulations) </li>
	<li> Console stays visible in GUI operation.  Can the window be suppressed, with STDOUT redirected via tk.Message? </li>
	<li> Android and iOS app integration ('cause... ok, no, probably not) </li>
	<li> Config file specification of InkOpt variables and GUI configurations </li>
	<li> GUI input parameter validation update to non-crashing version </li>
	<li> Optimize library imports to avoid memory bloat and long load time (only import what you need) </li>
</ul>
<br>

<u>Curiosities (Not Necessarily Related)</u>
<ul>
	<li> Write a lambda to leave something alone unless it's None; if None, set to a new value </li>
	<li> Use try/except on only the definition expression of a function (flexible function defs) </li>
	<li> What is the power of the "with" keyword? </li>
	<li> Compile as much of the code as possible to .pyc bytecode for shorter startup time (plus some anti-human-eye obfuscation) </li>
	<li> .pyw files execute headlessly with pythonw
	<li> What's the point of .pyd? </li>
</ul>
<br>

<br>
