REM runInkOpt.bat
REM Adrian Henle
REM Voxtel, Inc.
REM 
REM Double-clickable entry point for InkOpt on Windows
echo off
cls
REM ## This should have abstraction for input file
python InkOpt_v10.py input.txt
