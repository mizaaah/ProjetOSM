document.addEventListener('DOMContentLoaded', function () {
    
    var map = L.map('map').setView([48.8566, 2.3522], 13);

    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    
    var marker = L.marker([48.8566, 2.3522]).addTo(map);
    marker.bindPopup("<b>Bienvenue à Paris !</b><br>Ceci est un exemple.").openPopup();
});