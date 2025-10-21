@echo off
echo ==========================================
echo   🚀 Saytni Render'ga yuklash jarayoni
echo ==========================================
echo.

:: 1. Loyiha fayllarini qo'shish
git add .
echo ✅ Fayllar qo'shildi.

:: 2. Commit yozuvi (sana va vaqt bilan)
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do set DATE=%%a-%%b-%%c
for /f "tokens=1-2 delims=: " %%a in ('time /t') do set TIME=%%a-%%b
git commit -m "Avtomatik yangilanish: %DATE% %TIME%"
echo ✅ Commit yaratildi.

:: 3. O'zgarishlarni GitHub'ga yuborish
git push origin main
if %errorlevel% neq 0 (
    echo ❌ Xatolik: Git push bajarilmadi.
    pause
    exit /b
)
echo ✅ Render yangilanishni boshladi.

:: 4. Render loglarini kuzatish
echo.
echo ==========================================
echo   🔍 Render loglarini ko'rish uchun:
echo   https://render.com/dashboard
echo ==========================================
echo.
pause
