@echo off
echo ======================================
echo   MAKTAB SAYTI YANGILASH DASTURI
echo ======================================
cd /d D:\maktab_sayti

echo.
echo >>> O'zgarishlar GitHub'ga tayyorlanmoqda...
git add .

echo.
set /p msg=Commit izohini kiriting (masalan: style.css yangilandi): 
git commit -m "%msg%"

echo.
echo >>> GitHub bilan sinxronlashmoqda...
git branch -M main
git push -u origin main

echo.
echo ✅ Sayt muvaffaqiyatli yangilandi!
pause
