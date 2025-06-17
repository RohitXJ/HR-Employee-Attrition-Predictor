@echo off
echo Updating requirements.txt...

rem Check if virtual environment is active
if not exist ".venv\Scripts\activate.bat" (
    echo Error: Virtual environment not found. Please run setup_env.bat first.
    goto :eof
)

rem Activate the virtual environment
call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment. Exiting.
    goto :eof
)

echo Running pip freeze to update requirements.txt...
pip freeze > requirements.txt
if %errorlevel% neq 0 (
    echo Failed to generate requirements.txt.
    goto :eof
)

echo requirements.txt updated successfully.
echo Remember to commit and push requirements.txt to GitHub Desktop!
pause