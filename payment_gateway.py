<!DOCTYPE html>
<html lang="en">
<head>
    <title>Payment - Anjali Caterer & Decorators</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

<!-- Navbar -->
<div class="navbar">
    <a href="{{ url_for('home') }}">Home</a>
    <a href="{{ url_for('services') }}">Services</a>
    <a href="{{ url_for('menu') }}">Menu</a>
    <a href="{{ url_for('booking') }}">Booking</a>
    <a href="{{ url_for('payment') }}">Payment</a>
    <a href="{{ url_for('contact') }}">Contact</a>
</div>

<!-- Header -->
<div class="hero">
    <div class="overlay">
        <h1 class="fade-in">Make a Secure Payment</h1>
    </div>
</div>

<!-- Payment Form -->
<section class="payment-container fade-in">
    <h2>Pay Online</h2>
    
    <form action="{{ url_for('payment') }}" method="POST">
        <input type="text" name="name" placeholder="Full Name" required>
        <input type="email" name="email" placeholder="Email Address" required>
        <input type="text" name="phone" placeholder="Phone Number" required>
        <input type="number" name="amount" placeholder="Amount (INR)" required>
        
        <select name="payment_method" required>
            <option value="">Select Payment Method</option>
            <option value="UPI">UPI</option>
            <option value="Credit Card">Credit Card</option>
            <option value="Bank Transfer">Bank Transfer</option>
        </select>
        
        <button type="submit" class="btn">Proceed to Pay</button>
    </form>
</section>

</body>
</html>
