import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Database setup (create table if it doesn't exist)
conn = sqlite3.connect(app.config['DATABASE'])
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password STRING 
    )
''')
conn.commit()
conn.close()
