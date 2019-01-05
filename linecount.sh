#!/bin/bash

# linecount.sh
# Adrian Henle
# Counts the lines of code in the project

# Extensions of project code files
CODE_FILE_TYPES="*.py *.sh *.md *.bat"

# Make list of project file lengths
touch .tmp
for FILE in $(ls $CODE_FILE_TYPES)
do
	wc -l $FILE | cut -d" " -f 1 >> .tmp
done

# Sum .tmp
paste -sd+ .tmp | bc

# Clean up
rm -f .tmp



