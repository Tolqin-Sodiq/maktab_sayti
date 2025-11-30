from flask import Flask, render_template, request
from datetime import datetime
import openpyxl
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', year=datetime.now().year)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Bu yerda sizning ma’lumotlarni Excelga yozish kodingiz bo‘ladi
        pass
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html', year=datetime.now().year)

@app.route('/clubs')
def clubs():
    return render_template('clubs.html', year=datetime.now().year)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        place = request.form.get('place')
        age = request.form.get('age')
        name = request.form.get('name')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Fayl nomi
        file_path = 'data.xlsx'

        # Fayl mavjud bo'lmasa, yangi yaratamiz
        if not os.path.exists(file_path):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = "Aloqa ma'lumotlari"
            sheet.append(["Vaqt", "Manzil ma‘qulmi?", "Farzand yoshi", "Ismi-sharifi", "Telefon", "Xabar"])
            workbook.save(file_path)

        # Faylni ochamiz
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        # age ni butun songa o‘tkazamiz (agar to‘g‘ri raqam kiritilgan bo‘lsa)
        try:
            age_value = int(age)
        except (ValueError, TypeError):
            age_value = None  # Agar noto‘g‘ri raqam kiritilsa, bo‘sh qoldiramiz

        # Yangi satr yozamiz
        sheet.append([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            place,
            age_value,
            name,
            phone,
            message
        ])

        workbook.save(file_path)

        return render_template('contact.html', year=datetime.now().year, success=True)

    return render_template('contact.html', year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)
