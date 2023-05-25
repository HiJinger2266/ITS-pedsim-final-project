@echo off
REM Compile all the .ui files in .\resources to .py files with pyuic5 and output to .\views
CALL conda activate ITS_final
for %%F in (.\resources\ui\*.ui) do (
    pyuic5 "%%F" -o .\views\%%~nF_ui.py
)
REM pip install from requirements.txt
pip install -r requirements.txt
