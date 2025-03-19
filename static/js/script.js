$(document).ready(function() {
    $('#closeIcon').on('click', function() {
        $('#formContainer').addClass('hidden');
    });

    $('#openForm').on('click', function() {
        $('#formContainer').removeClass('hidden');
    });

    $('.incrilien').on('click', function(event) {
        event.preventDefault();
        $('#formContainer').addClass('hidden');
        $('#registerContainer').removeClass('hidden');
    });

    $('#closeRegisterIcon').on('click', function() {
        $('#registerContainer').addClass('hidden');
    });

    $('.colien').on('click', function(event) {
        event.preventDefault();
        $('#registerContainer').addClass('hidden');
        $('#formContainer').removeClass('hidden');
    });

    $('.oublielien').on('click', function(event) {
        event.preventDefault();
        $('#formContainer').addClass('hidden');
        $('#registerContainer').addClass('hidden');
        $('#mdpOublie').removeClass('hidden');
    });

    $('#mdpOublie .iconferme').on('click', function() {
        $('#mdpOublie').addClass('hidden');
    });

    $('#mdpOublie .oublielien').on('click', function(event) {
        event.preventDefault();
        $('#mdpOublie').addClass('hidden');
        $('#formContainer').removeClass('hidden');
    });
});