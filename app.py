from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for the menu page
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Route for the testimonials page
@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
