#!/bin/bash

# runInkOpt.sh
# Adrian Henle
# Voxtel, Inc.

# A quick, hacky way to launch InkOpt_v10 for dev work

INPUT="input.txt"
OUTPUT="inkoptlog"
PROGRAM="./InkOpt_v10.py"

clear
$PROGRAM $INPUT
