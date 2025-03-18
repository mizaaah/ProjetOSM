document.getElementById('closeIcon').addEventListener('click', function() {
    document.getElementById('formContainer').classList.add('hidden');
});

document.getElementById('openForm').addEventListener('click', function() {
    document.getElementById('formContainer').classList.remove('hidden');
});

document.querySelector('.incrilien').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('formContainer').classList.add('hidden');
    document.getElementById('registerContainer').classList.remove('hidden');
});

document.getElementById('closeRegisterIcon').addEventListener('click', function() {
    document.getElementById('registerContainer').classList.add('hidden');
});