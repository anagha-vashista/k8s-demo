from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="mysql-service",
        user="root",
        password="rootpass",
        database="testdb"
    )

@app.route('/init', methods=['GET'])
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    conn.commit()
    return "DB Initialized"

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (data['name'],))
    conn.commit()
    return "User Added"

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    return jsonify(user)

app.run(host='0.0.0.0', port=8080)
