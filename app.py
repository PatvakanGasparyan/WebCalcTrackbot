from flask import Flask, render_template
import WebCalcTrackbot.database as database

app = Flask(__name__)

@app.route('/')
def index():
    # Берем историю из базы данных
    logs = database.get_all_logs()
    # Отдаем историю в файл index.html
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    print("Сайт запущен на http://127.0.0.1:5000")
    app.run(debug=True, port=5000)