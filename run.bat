@echo off
cd /d "%~dp0"
title He Thong Thi Thu va Tao De DGNL

echo ======================================================================
echo    HE THONG KHAO THI VA TAO DE DANH GIA NANG LUC (DGNL DHQG)
echo    120 Cau - 150 Phut - Thang diem 1200 - LangGraph Multi-Agent
echo ======================================================================
echo.

set "PY="
if exist "%LOCALAPPDATA%\Programs\Python\Python314\python.exe" set "PY=%LOCALAPPDATA%\Programs\Python\Python314\python.exe"
if not defined PY if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set "PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not defined PY if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" set "PY=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
if not defined PY if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" set "PY=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
if not defined PY if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" set "PY=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
if not defined PY if exist "C:\ProgramData\miniconda3\python.exe" set "PY=C:\ProgramData\miniconda3\python.exe"
if not defined PY set "PY=python"

echo [OK] Su dung Python: %PY%
echo [OK] Dang khoi dong may chu tai http://localhost:8050 ...
echo [OK] Trinh duyet web se tu dong mo len sau vai giay.
echo [OK] De tat may chu, hay dong cua so nay hoac an Ctrl+C.
echo ======================================================================
echo.

"%PY%" run.py

if errorlevel 1 (
    echo.
    echo [LOI] May chu da dung lai.
    pause
)
