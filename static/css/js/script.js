document.addEventListener("DOMContentLoaded", function () {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // Form validation for booking form
    const bookingForm = document.getElementById("booking-form");
    if (bookingForm) {
        bookingForm.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent default form submission

            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const phone = document.getElementById("phone").value.trim();
            const guests = document.getElementById("guests").value.trim();
            const eventDate = document.getElementById("event-date").value.trim();

            if (!name || !email || !phone || !guests || !eventDate) {
                alert("Please fill in all required fields.");
                return;
            }

            if (!/^\d{10}$/.test(phone)) {
                alert("Please enter a valid 10-digit phone number.");
                return;
            }

            if (!/^\d+$/.test(guests) || parseInt(guests) <= 0) {
                alert("Please enter a valid number of guests.");
                return;
            }

            this.submit(); // Submit form if validation passes
        });
    }

    // WhatsApp Chat Integration
    const whatsappBtn = document.getElementById("whatsapp-btn");
    if (whatsappBtn) {
        whatsappBtn.addEventListener("click", function () {
            const phoneNumber = "+91XXXXXXXXXX"; // Update with the business WhatsApp number
            const message = encodeURIComponent("Hello, I would like to inquire about catering services.");
            window.open(`https://wa.me/${phoneNumber}?text=${message}`, "_blank");
        });
    }

    // Animation on scroll
    const fadeElements = document.querySelectorAll(".fade-in");
    function checkFade() {
        fadeElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight * 0.9) {
                el.classList.add("visible");
            }
        });
    }
    window.addEventListener("scroll", checkFade);
    checkFade(); // Trigger on load
});
