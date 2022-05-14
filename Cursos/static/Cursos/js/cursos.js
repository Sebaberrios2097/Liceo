$(document).ready(function() {

    // FETCHING DATA FROM JSON FILE
    $.getJSON("Cursos/js/json/cursos.json",
        function(data) {
            var curso = '';

            $.each(data.cursos.curso, function(key, value) {

                curso += '<tr><td class="text-center">' + value.nivel + value.letra + '</td>  <td class="text-center">' + value.profesor + '</td> <td class="text-center">' + value.paradocente + '</td></tr>';
            });

            $('#curso').append(curso);
        });
    // $('#cursos').DataTable();
});