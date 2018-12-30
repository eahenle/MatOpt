#!/bin/bash

# BASH script to run InkOpt
# Adrian Henle
# Voxtel, Inc.
#
# This version is intended for development purposes.

# Input parameter file for InkOpt
INPUT="input.txt"
OUTPUT=output.txt

# Clean up old output files
rm -f output*_*.csv

# Clear the console and execute InkOpt w/ input file
clear
echo ...
./InkOpt_v10.py $INPUT > $OUTPUT 2>&1
tail $OUTPUT
