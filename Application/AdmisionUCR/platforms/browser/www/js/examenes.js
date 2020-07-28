$( document ).ready(function() {

    $.ajax({
        url: 'http://127.0.0.1:5000/exams',
        success: function (response) {
            var userData = JSON.stringify(response);
            alert(userData);
        },
        error: function () {
            alert('Hubo un error');
        }
    });
});