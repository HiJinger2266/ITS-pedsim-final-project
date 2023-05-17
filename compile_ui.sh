#!/bin/bash
# Compile all the .ui files in ./resources to .py files with pyuic5 and ouput to ./views

for file in ./resources/ui/*.ui
do
    pyuic5 $file -o ./views/$(basename $file .ui)_ui.py
done