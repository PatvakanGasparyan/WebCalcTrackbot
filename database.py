import mysql.connector
from WebCalcTrackbot.config import *

# Подключение к базе
def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Создаем таблицу, если ее еще нет
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id VARCHAR(50),
            username VARCHAR(100),
            from_currency VARCHAR(10),
            to_currency VARCHAR(10),
            amount_in FLOAT,
            amount_out FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Запись новой операции от пользователя
def add_log(user_id, username, from_curr, to_curr, amount_in, amount_out):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logs (user_id, username, from_currency, to_currency, amount_in, amount_out)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (user_id, username, from_curr, to_curr, amount_in, amount_out))
    conn.commit()
    conn.close()

# Получить все записи для сайта
def get_all_logs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM logs ORDER BY created_at DESC")
    records = cursor.fetchall()
    conn.close()
    return records