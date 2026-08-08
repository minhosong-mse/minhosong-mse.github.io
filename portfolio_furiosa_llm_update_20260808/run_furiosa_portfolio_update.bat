@echo off
setlocal
cd /d "%~dp0"

echo ============================================================
echo FuriosaAI + LLM Portfolio Update
echo ============================================================
echo.

if not exist "index.html" (
  echo ERROR: index.html was not found.
  echo Copy this package into the cloned minhosong-mse.github.io root.
  pause
  exit /b 1
)

where py >nul 2>&1
if errorlevel 1 (
  echo ERROR: Python launcher "py" was not found.
  pause
  exit /b 1
)

py apply_furiosa_portfolio_update.py
if errorlevel 1 (
  echo.
  echo ERROR: Update failed.
  pause
  exit /b 1
)

echo.
echo Starting preview at http://localhost:8030
start "Portfolio Preview" cmd /k "cd /d ""%CD%"" && py -m http.server 8030"
timeout /t 2 /nobreak >nul
start "" "http://localhost:8030/#experience"

echo.
echo Preview ready.
echo.
pause
