$(document).ready(function() {

    var regiones = [];

    $.get("https://apis.digital.gob.cl/dpa/regiones", function(data) {
        $.each(data, function(i, item) {
            htmlRegion = htmlRegion + '<option value="' + item.codigo + '">' + item.nombre + '</option>';
        });

        $('#regiones').html(htmlRegion);
    });

    var iRegion = 0;
    var htmlRegion = '<option value="sin-region">Seleccione región</option>';
    var htmlComunas = '<option value="sin-region">Seleccione comuna</option>';
    $('#comunas').html(htmlComunas);

    $('#regiones').change(function() {
        var selectedOption = $("#regiones option:selected").val();

        $.get("https://apis.digital.gob.cl/dpa/regiones/" + selectedOption + "/comunas", function(data) {
            htmlComuna = "";
            $('#comunas').html(htmlComunas)

            $.each(data, function(i, item) {
                htmlComuna = htmlComuna + '<option value="' + item.codigo + '">' + item.nombre + '</option>';
            });

            $('#comunas').html(htmlComuna);
        });
    });

    $('#regiones').change(function() {
        if ($(this).val() == 'sin-region') {
            alert('Porfavor debe seleccionar una Región');
            $('#comunas').html(htmlComunas);
        }
    });

});