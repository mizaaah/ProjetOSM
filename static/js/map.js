let map;

document.addEventListener('DOMContentLoaded', function () {
    map = L.map('map').setView([46.8, 2.2], 6); // Centre France

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    document.getElementById('categorie').addEventListener('change', loadMarkers);

    loadMarkers(); // Initial load
});

function loadMarkers() {
    const categorieId = document.getElementById('categorie').value;
    const url = categorieId ? `/api/etablissements?categorie_id=${categorieId}` : '/api/etablissements';

    fetch(url)
        .then(res => res.json())
        .then(data => {
            clearMarkers();
            data.forEach(e => {
                addMarker(e.latitude, e.longitude, `<b>${e.nom}</b><br>${e.adresse}<br>${e.ville}`);
            });
        });
}

let markers = [];

function addMarker(lat, lon, message) {
    const marker = L.marker([lat, lon]).addTo(map);
    marker.bindPopup(message);
    markers.push(marker);
}

function clearMarkers() {
    markers.forEach(m => map.removeLayer(m));
    markers = [];
}