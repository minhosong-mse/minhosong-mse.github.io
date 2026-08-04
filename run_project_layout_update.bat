@echo off
setlocal
cd /d "%~dp0"

echo ============================================================
echo Portfolio Project Layout Update
echo ============================================================
echo.

if not exist "index.html" (
  echo ERROR: index.html was not found.
  echo.
  echo Copy all package files into the cloned repository folder
  echo that contains index.html, then run this BAT file again.
  echo.
  pause
  exit /b 1
)

if not exist "apply_project_layout_update.py" (
  echo ERROR: apply_project_layout_update.py was not found.
  pause
  exit /b 1
)

where py >nul 2>&1
if errorlevel 1 (
  echo ERROR: Python launcher "py" was not found.
  pause
  exit /b 1
)

echo Applying the approved project layout...
py apply_project_layout_update.py
if errorlevel 1 (
  echo.
  echo ERROR: The update failed.
  pause
  exit /b 1
)

echo.
echo Starting preview at http://localhost:8010
start "Portfolio Preview" cmd /k "cd /d ""%CD%"" && py -m http.server 8010"
timeout /t 2 /nobreak >nul
start "" "http://localhost:8010"

echo.
echo Update completed.
echo Review full desktop, half-width window, and mobile layouts.
echo Then use GitHub Desktop to Commit and Push.
echo.
pause
