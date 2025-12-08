from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    student_info = {
        'name': os.getenv('STUDENT_NAME', 'Федоськина Виктория Эдуардовна'),
        'group': os.getenv('STUDENT_GROUP', 'БИСТ-22-ИТ-2'),
        'course': 'Инструменты DevOps',
        'task': 'Домашнее задание (CI/CD через Jenkins)',
        'grade_target': '4',
        'server_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': os.getenv('HOSTNAME', 'unknown')
    }
    return render_template('index.html', **student_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)