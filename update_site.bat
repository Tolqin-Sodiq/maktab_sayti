@echo off
REM ==========================================
REM  MAKTAB SAYTI UPDATE SCRIPT (Render bilan)
REM ==========================================

echo ==========================================
echo   MAKTAB SAYTI — UPDATE VA DEPLOY BOSHLANDI
echo ==========================================
echo.

REM --- 1. Git repositoryni yangilash ---
git add .
git commit -m "Auto update from update_site.bat"
git push origin main

if %errorlevel% neq 0 (
    echo ❌ Git pushda xato yuz berdi. Iltimos, tarmoqni tekshiring.
    pause
    exit /b
)

echo.
echo ✅ GitHub’ga o‘zgarishlar muvaffaqiyatli push qilindi.
echo.

REM --- 2. Render API orqali majburiy rebuild ---
REM Quyidagi joyga Render loyihangizga mos API token va service ID ni yozing
set RENDER_API_KEY=rnd_nqgSyGHTxTTVTlt983Gctdd2YLz0
set RENDER_SERVICE_ID=srv-d3p6s5re5dus738hfll0

echo 🔄 Render’da yangi build ishga tushirilmoqda...
curl -X POST "https://api.render.com/v1/services/%RENDER_SERVICE_ID%/deploys" ^
     -H "Accept: application/json" ^
     -H "Authorization: Bearer %RENDER_API_KEY%" ^
     -H "Content-Type: application/json" ^
     -d "{}"

if %errorlevel% neq 0 (
    echo ❌ Render buildni chaqirishda xato.
    pause
    exit /b
)

echo ✅ Render’da yangi build muvaffaqiyatli ishga tushirildi.
echo.

REM --- 3. So‘nggi loglarni olish ---
echo 🕓 Loglar yuklanmoqda (so‘nggi 20 qatordan)...
curl -s -H "Authorization: Bearer %RENDER_API_KEY%" ^
     "https://api.render.com/v1/services/%RENDER_SERVICE_ID%/logs?tail=true&limit=20"

echo.
echo ✅ Tugadi. Saytingiz bir necha daqiqa ichida yangilanadi.
echo.

pause
