document.getElementById('closeIcon').addEventListener('click', function() {
    document.getElementById('formContainer').classList.add('hidden');
});

document.getElementById('openForm').addEventListener('click', function() {
    document.getElementById('formContainer').classList.remove('hidden');
});