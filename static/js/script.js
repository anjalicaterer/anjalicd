document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        let isValid = true;

        // Basic form validation
        if (!formData.get('name')) {
            alert('Please enter your name.');
            isValid = false;
        }
        if (!formData.get('email') || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.get('email'))) {
            alert('Please enter a valid email.');
            isValid = false;
        }
        if (!formData.get('phone') || formData.get('phone').length < 10) {
            alert('Please enter a valid phone number.');
            isValid = false;
        }
        if (!formData.get('message')) {
            alert('Please enter a message.');
            isValid = false;
        }

        if (isValid) {
            // Here you would typically send the form data to a server
            alert('Form submitted successfully!'); // Placeholder for actual submission
            this.reset(); // Reset the form after submission
        }
    });

    // Google Maps integration
    function initMap() {
        var location = {lat: 22.449638, lng: 88.356407}; // Coordinates for the address
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 15,
            center: location
        });
        var marker = new google.maps.Marker({
            position: location,
            map: map
        });
    }
});