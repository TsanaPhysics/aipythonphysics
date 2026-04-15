document.addEventListener('DOMContentLoaded', () => {
    const toggleButtons = document.querySelectorAll('.toggle-btn');

    toggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            const card = button.closest('.topic-card');
            const content = card.querySelector('.collapsible-content');
            
            // Toggle expansion
            content.classList.toggle('expanded');
            
            // Update button text
            if (content.classList.contains('expanded')) {
                button.textContent = 'ย่อข้อมูล';
                // Smooth scroll to card
                card.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                button.textContent = 'อ่านคู่มือ';
            }
        });
    });

    // Add a simple fade-in effect for cards on scroll
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.topic-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease-out';
        observer.observe(card);
    });
});
