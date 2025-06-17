@echo off
echo Setting up Python virtual environment...

rem 1. Check if Python is installed and is Python 3
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not found in PATH. Please install Python 3.8+ and try again.
    goto :eof
)
rem Basic check for Python 3, improve if needed for specific version checks
for /f "tokens=*" %%i in ('python -c "import sys; print(sys.version_info.major)"') do set PYTHON_MAJOR_VERSION=%%i
if not "%PYTHON_MAJOR_VERSION%"=="3" (
    echo Found Python version %PYTHON_MAJOR_VERSION%. This script requires Python 3.
    goto :eof
)


rem 2. Create the virtual environment if it doesn't exist
if not exist ".venv" (
    echo Creating new virtual environment at .\.venv
    python -m venv .venv
) else (
    echo Virtual environment already exists at .\.venv. Skipping creation.
)

rem 3. Activate the virtual environment
rem This uses 'call' so that the batch script continues after activation
call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment. Exiting.
    goto :eof
)
echo Virtual environment activated.

rem 4. Install/Update pip (optional but good practice to ensure pip is up-to-date within the venv)
echo Updating pip and setuptools...
pip install --upgrade pip setuptools wheel
if %errorlevel% neq 0 (
    echo Failed to update pip. Check network connection or permissions.
    goto :eof
)

rem 5. Install requirements from requirements.txt
if exist "requirements.txt" (
    echo Installing/updating Python packages from requirements.txt...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install packages from requirements.txt. Check the file or your internet connection.
        goto :eof
    )
    echo All packages installed successfully.
) else (
    echo WARNING: requirements.txt not found. No Python packages installed.
    echo If this is a new project, you might need to create it by running "pip freeze > requirements.txt"
)

echo.
echo =========================================================
echo Environment setup complete!
echo To run your scripts, ensure this terminal session is active
echo or open a new terminal and run: .venv\Scripts\activate
echo
echo IF YOU ADD NEW LIBRARIES:
echo   1. Activate environment: .venv\Scripts\activate
echo   2. Install library: pip install new-lib
echo   3. UPDATE requirements.txt: pip freeze > requirements.txt
echo   4. Commit and push requirements.txt to GitHub.
echo =========================================================
echo.
pause