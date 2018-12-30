VERSION = 10.04 # Version number ## Consider scraping from filename?
INPUTFILE = "material_table.csv" # Default input file for material properties
MINMATPCT = 20 # Minimum volume percentage of the matrix in a composite
DOPSTEP = 4 # Number of points to sample in dopant percentage ranges
"""
	### WARNING! ###
	Complexity for v7 algorithm is O(k^DOPSTEP).
	Don't increase sampling density unless you have all day to run permutations.
"""
