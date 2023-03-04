$(document).ready(function() {    
    const csrftoken =  window.CSRF_TOKEN;
    $('.edit_product').click(function() {
        let value_id = $(this).attr("id");
       $.ajax({
            type: "POST",
            url: "/getProduct/",
            data: {csrfmiddlewaretoken:csrftoken, id:value_id},
            async : false,
            complete: function(response) {
                console.log(response.responseJSON);
                $("#exampleModalCenter").modal('show');
                $("#exampleModalCenterTitle").html = "Producto"

            },
            error: function() {
                console.error('Ha ocurrido un error');
            }
        });
    });
    $('.delete_product').click(function() {
       $("#exampleModalCenter").modal('show');
        let value_id = $(this).attr("id");
       $.ajax({
            type: "POST",
            url: "/deleteProduct/",
            data: {csrfmiddlewaretoken:csrftoken, id:value_id},
            async : false,
            complete: function(response) {
                console.log(response)
            },
            error: function() {
                console.error('Ha ocurrido un error');
            }
        });
    });
});