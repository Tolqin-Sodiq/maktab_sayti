from flask import Flask, render_template, request, redirect
import pandas as pd
import os
from openpyxl import load_workbook

app = Flask(__name__)

# 🔹 Bosh sahifa
@app.route('/')
def home():
    return render_template('index.html')

# 🔹 Biz haqimizda
@app.route('/about')
def about():
    return render_template('about.html')

# 🔹 To‘garaklar
@app.route('/clubs')
def clubs():
    return render_template('clubs.html')

# 🔹 Aloqa sahifasi
@app.route('/aloqa')
def aloqa():
    return render_template('aloqa.html')

# 🔹 Ro‘yxatdan o‘tish sahifasi
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        ism = request.form['ism']
        familiya = request.form['familiya']
        telefon = request.form['telefon']
        email = request.form['email']

        # 🔸 Telefon raqamini matn sifatida saqlash
        new_data = {
            'Ism': [ism],
            'Familiya': [familiya],
            'Telefon': ["'" + telefon],  # ilmiy formatdan saqlaydi
            'Email': [email]
        }

        try:
            # 🔸 Fayl mavjud bo‘lsa — ustiga yozamiz
            if os.path.exists('data.xlsx'):
                df = pd.read_excel('data.xlsx', dtype=str)
                df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
            else:
                df = pd.DataFrame(new_data)

            # 🔸 Yangi vaqtinchalik faylga yozish
            temp_file = 'data_temp.xlsx'
            df.to_excel(temp_file, index=False)

            # 🔸 Eski faylni almashtirish
            os.replace(temp_file, 'data.xlsx')

            # 🔹 Ustun kengliklarini avtomatik moslash
            wb = load_workbook('data.xlsx')
            ws = wb.active
            for col in ws.columns:
                max_length = 0
                col_letter = col[0].column_letter
                for cell in col:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = max_length + 2
                ws.column_dimensions[col_letter].width = adjusted_width
            wb.save('data.xlsx')

        except PermissionError:
            # 🔸 Fayl ochiq bo‘lsa, xato chiqarmasdan o'tkazib yuboradi
            print("⚠️ Excel fayl hozir ochiq. Yopib, qayta urinib ko‘ring.")

        return redirect('/')
    return render_template('register.html')

# 🔹 Serverni ishga tushirish

# 🔹 Admin sahifasi — ro‘yxatdan o‘tganlar jadvali
@app.route('/admin')
def admin():
    try:
        if os.path.exists('data.xlsx'):
            df = pd.read_excel('data.xlsx', dtype=str)
            # NaN qiymatlar bo‘lsa, ularni bo‘sh qoldiramiz
            df = df.fillna("")
            # DataFrame'ni HTML jadvalga aylantiramiz
            table_html = df.to_html(classes='table', index=False, border=0)
            return f"""
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Admin sahifasi</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background: #f0f4f8;
                        padding: 40px;
                    }}
                    h2 {{
                        text-align: center;
                        color: #333;
                    }}
                    .table {{
                        margin: 20px auto;
                        border-collapse: collapse;
                        width: 80%;
                        background: white;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }}
                    th, td {{
                        border: 1px solid #ccc;
                        padding: 10px;
                        text-align: left;
                    }}
                    th {{
                        background-color: #4CAF50;
                        color: white;
                    }}
                    tr:nth-child(even) {{
                        background-color: #f9f9f9;
                    }}
                    a {{
                        display: inline-block;
                        margin-top: 15px;
                        text-decoration: none;
                        color: #333;
                        background: #ddd;
                        padding: 8px 15px;
                        border-radius: 5px;
                    }}
                    a:hover {{
                        background: #bbb;
                    }}
                </style>
            </head>
            <body>
                <h2>📋 Ro‘yxatdan o‘tgan foydalanuvchilar</h2>
                {table_html}
                <div style="text-align:center;">
                    <a href="/">⬅️ Bosh sahifaga qaytish</a>
                </div>
            </body>
            </html>
            """
        else:
            return "<h3>Ma'lumotlar fayli hali yaratilmagan.</h3>"
    except Exception as e:
        return f"<h3>Xatolik: {str(e)}</h3>"


if __name__ == '__main__':
    app.run(debug=True)
