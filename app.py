from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

DATABASE = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Services Route
@app.route('/services')
def services():
    return render_template('services.html')

# Menu Route
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Booking Route
@app.route('/booking')
def booking():
    return render_template('booking.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Testimonials Route
@app.route('/testimonials')
def testimonials():
    conn = get_db_connection()
    testimonials = conn.execute("SELECT * FROM testimonials ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('testimonials.html', testimonials=testimonials)

# Blog Route
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Handle Booking Form Submission
@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    event_type = request.form['event_type']
    event_date = request.form['event_date']
    guests = request.form['guests']
    message = request.form['message']

    conn = get_db_connection()
    conn.execute("INSERT INTO bookings (name, email, phone, event_type, event_date, guests, message) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (name, email, phone, event_type, event_date, guests, message))
    conn.commit()
    conn.close()

    flash("Booking request submitted successfully!")
    return redirect(url_for('booking'))

# Handle New Testimonial Submission
@app.route('/submit_testimonial', methods=['POST'])
def submit_testimonial():
    name = request.form['name']
    review = request.form['review']
    rating = request.form['rating']

    conn = get_db_connection()
    conn.execute("INSERT INTO testimonials (name, review, rating) VALUES (?, ?, ?)",
                 (name, review, rating))
    conn.commit()
    conn.close()

    flash("Thank you for your review!")
    return redirect(url_for('testimonials'))

# API to Get Testimonials (For Dynamic Loading)
@app.route('/api/testimonials')
def api_testimonials():
    conn = get_db_connection()
    testimonials = conn.execute("SELECT * FROM testimonials ORDER BY id DESC").fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in testimonials])

# Run App
if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        conn.execute('''CREATE TABLE bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        phone TEXT,
                        event_type TEXT,
                        event_date TEXT,
                        guests INTEGER,
                        message TEXT)''')
        conn.execute('''CREATE TABLE testimonials (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        review TEXT,
                        rating INTEGER)''')
        conn.commit()
        conn.close()
    
    app.run(debug=True)
import sqlite3

def init_db():
    with sqlite3.connect("database.db") as conn:
        with open("schema.sql") as f:
            conn.executescript(f.read())
        conn.commit()

# Run this once to initialize the database
init_db()
