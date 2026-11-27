@echo off
chcp 65001 >nul
echo ========================================================
echo   DANG DAY TOAN BO DU AN LEN GITHUB (NVY941162-BLIP/DGNL)
echo ========================================================
echo.
set "PATH=C:\Program Files\Git\cmd;%PATH%"
cd /d "%~dp0"

echo 1. Kiem tra va cap nhat dia chi kho luu tru GitHub...
git remote set-url origin https://github.com/nvy941162-blip/dgnl.git

echo.
echo 2. Them cac tep thay doi...
git add -A

echo.
echo 3. Luu commit...
git commit -m "Deploy DGNL Platform to GitHub"

echo.
echo 4. Day code len GitHub (origin main)...
echo [i] Neu co cua so GitHub hien len, ban chi can bam 'Sign in with your browser'.
echo.
git push -u origin main

echo.
if %errorlevel% equ 0 (
    echo ========================================================
    echo   THANH CONG! TOAN BO CODE DA DUOC DUA LEN GITHUB!
    echo   Dia chi repo: https://github.com/nvy941162-blip/dgnl
    echo ========================================================
) else (
    echo [!] Co loi xay ra. Vui long kiem tra ket noi mang va quyen truy cap.
)
echo.
pause
