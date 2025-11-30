@echo off
REM ===============================
REM   MAKTAB SAYTI AUTO DEPLOY
REM   GitHub → Render (API bilan)
REM ===============================

echo.
echo ========================================
echo     MAKTAB SAYTI — AUTO DEPLOY BOSHLANDI
echo ========================================
echo.

REM --- 1. Git o'zgarishlarini commit va push ---
git add .
git commit -m "Auto update (update_site.bat)" >nul 2>&1

echo 🔄 GitHub’ga push qilinmoqda...
git push origin main
if %errorlevel% neq 0 (
    echo ❌ Git pushda xato. Internet yoki Git sozlamasini tekshiring.
    pause
    exit /b
)

echo ✅ GitHub’ga muvaffaqiyatli push qilindi.
echo.

REM --- 2. Render uchun API sozlamalari ---
set "RENDER_API_KEY=rnd_nqgSyGHTxTTVTlt983Gctdd2YLz0"
set "RENDER_SERVICE_ID=srv-d3p6s5re5dus738hfll0"

echo 🔄 Render’da yangi build ishga tushirilmoqda...

curl -X POST ^
  "https://api.render.com/v1/services/%RENDER_SERVICE_ID%/deploys" ^
  -H "Authorization: Bearer %RENDER_API_KEY%" ^
  -H "Content-Type: application/json" ^
  -d "{}"

if %errorlevel% neq 0 (
    echo ❌ Render API chaqiruvida xato yuz berdi.
    pause
    exit /b
)

echo ✅ Render Build muvaffaqiyatli ishga tushirildi.
echo.

REM --- 3. Loglarni olish ---
echo 📝 So‘nggi 20 qatordan loglar:

curl -s ^
  -H "Authorization: Bearer %RENDER_API_KEY%" ^
  "https://api.render.com/v1/services/%RENDER_SERVICE_ID%/logs?tail=true&limit=20"

echo.
echo ========================================
echo   🚀 Yangilash yakunlandi!
echo   Render 1–3 daqiqada saytni yangilaydi.
echo ========================================
echo.
pause
