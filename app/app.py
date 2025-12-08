from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    name = os.getenv('STUDENT_NAME', 'Федоськина Виктория Эдуардовна')
    group = os.getenv('STUDENT_GROUP', 'БИСТ-22-ИТ-2')
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return f'''<!DOCTYPE html>
<html>
<head>
    <title>DevOps ДЗ - {name}</title>
    <style>
        body {{ font-family: Arial; padding: 40px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        .header {{ background: #4CAF50; color: white; padding: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>DevOps Домашнее задание</h1>
            <h2>CI/CD Pipeline с Jenkins</h2>
        </div>
        <h3>Информация о студенте:</h3>
        <p><strong>ФИО:</strong> {name}</p>
        <p><strong>Группа:</strong> {group}</p>
        <p><strong>Дисциплина:</strong> Инструменты DevOps</p>
        <p><strong>Целевая оценка:</strong> 4/5</p>
        <p><strong>Время сервера:</strong> {time}</p>
        <h3>Статус:</h3>
        <p>Приложение успешно развернуто через Docker Compose + Jenkins</p>
    </div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)