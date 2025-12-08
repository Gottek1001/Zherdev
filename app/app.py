# app.py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    student_name = os.getenv('STUDENT_NAME', 'Федоськина Виктория Эдуардовна')
    student_group = os.getenv('STUDENT_GROUP', 'ИКТ-01')
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Project - {student_name}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .container {{ max-width: 800px; margin: 0 auto; }}
            .info {{ background: #f5f5f5; padding: 20px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>т Мой DevOps проект</h1>
            <div class="info">
                <h2>Информация о студенте:</h2>
                <p><strong>ФИО:</strong> {student_name}</p>
                <p><strong>Группа:</strong> {student_group}</p>
                <p><strong>Дисциплина:</strong> Инструменты DevOps</p>
                <p><strong>Оценка:</strong> 4 (CI/CD через Jenkins)</p>
            </div>
            <h3>Технологии:</h3>
            <ul>
                <li>Python Flask</li>
                <li>Docker</li>
                <li>Jenkins</li>
                <li>GitHub</li>
                <li>Nginx</li>
            </ul>
            <p>Время сервера: {os.popen("date").read()}</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)