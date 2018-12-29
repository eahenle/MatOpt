#!/bin/bash

# BASH script to run InkOpt
# Adrian Henle
# Voxtel, Inc.
#
# This version is intended for development purposes.

# Input parameter file for InkOpt
INPUT="input.txt"

# Clean up old output files
rm -f output*_*.csv

# Look for most recent program version by filename
for script in $(ls InkOpt_v*.py)
do
	NEWEST=$script
done

# Record InkOpt start time
date > .t1

# Clear the console and execute InkOpt w/ input file
clear
./$NEWEST $INPUT

# Display start and end time
echo "STARTED: $(cat .t1)"
echo "STOPPED: $(date)"

# Clean up starting timestamp file
rm -f .t1
