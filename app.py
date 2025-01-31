from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT, phone TEXT, email TEXT, 
                            event_type TEXT, guests INTEGER, 
                            date TEXT, message TEXT)''')
        conn.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        event_type = request.form['event_type']
        guests = request.form['guests']
        date = request.form['date']
        message = request.form['message']

        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bookings (name, phone, email, event_type, guests, date, message) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (name, phone, email, event_type, guests, date, message))
            conn.commit()
        
        return redirect(url_for('home'))

    return render_template('booking.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
