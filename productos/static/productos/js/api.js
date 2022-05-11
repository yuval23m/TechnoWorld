$(document).ready(function(){
    $.get("/static/productos/js/datos.json", 
    function(data){
        $.each(data.datos,(function (i, item) {
            $("#items").append('<div class = "carousel-item">'
                + '<img src="'+item.img+'" class="d-block w-100" alt="Ejemplo_foto_nosotros"></img>' +
                '<h1>'+ item.name +'</h1>' +
                '<p>'+ item.desc +'</p>' +
            '</div>');
            $(".carousel-item").first().addClass('active');
        }));
    });
});
