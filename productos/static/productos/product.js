$(document).ready(function() {    
    const csrftoken =  window.CSRF_TOKEN;
    function validateFields (errorsReport = "", nameProduct = "", descripcionProduct = "", priceProduct = "", inventoryProduct = "") {
        $("#errorsReport").html("");
        $("#alertProduct").hide();
        if (nameProduct === undefined || nameProduct === "") {
            errorsReport += "El nombre no puede estar vacío.\n"
        }
        if (descripcionProduct === undefined || nameProduct === "") {
            errorsReport += "La descripción no puede estar vacío.\n"
        }
        if (priceProduct === undefined || priceProduct === "") {
            errorsReport += "El precio no puede estar vacío.\n"
        }
        if (inventoryProduct === undefined || inventoryProduct === "") {
            errorsReport += "El inventario no puede estar vacío.\n"
        }
        return errorsReport
    };
    $('#goToProduct').click(function() {
       $.ajax({
            type: "POST",
            url: "/goToProduct/",
            data: {csrfmiddlewaretoken:csrftoken},
            async : false,
            complete: function(response) {
                $("#exampleModalCenterTitle").html("Producto");
                $("#modalBody").html(response.responseText);    
                $("#exampleModalCenter").modal('show');
                $("#createProduct").show();
                $("#saveChangesProduct").hide();
            },
            error: function() {
                console.error('Ha ocurrido un error');
            }
        });
    });
    $('#createProduct').click(function() {
        let errorsReport = ""
        const nameProduct = $("#nameProduct").val();
        const descripcionProduct = $("#descripcionProduct").val();
        const priceProduct = $("#priceProduct").val();
        const inventoryProduct = $("#inventoryProduct").val();
        errorsReport = validateFields(errorsReport, nameProduct, descripcionProduct, priceProduct, inventoryProduct)
        if (errorsReport.length === 0) {
            $.ajax({
                type: "POST",
                url: "/createProduct/",
                data: {csrfmiddlewaretoken:csrftoken, name_product: nameProduct, descrip_product: descripcionProduct, price_product: priceProduct, inventory_product: inventoryProduct},
                async : false,
                complete: function(response) {
                    if (response.responseJSON !== undefined && response.responseJSON['error'] && Array.isArray(response.responseJSON['error'])) {
                        if (response.responseJSON['error'] && response.responseJSON['error'].length !== 0) {
                            response.responseJSON['error'].forEach(function (text) {
                                errorsReport += text
                            })
                            $("#errorsReport").html(errorsReport);
                            $("#alertProduct").show();
                        } else {
                            window.location.reload();
                        }
                    }
                },
                error: function() {
                    console.error('Ha ocurrido un error');
                }
            });
        } else {
            $("#errorsReport").html(errorsReport);
            $("#alertProduct").show();
        }
    });
    $('.edit_product').click(function() {
        let value_id = $(this).attr("id");
       $.ajax({
            type: "POST",
            url: "/getProduct/",
            data: {csrfmiddlewaretoken:csrftoken, id:value_id},
            async : false,
            complete: function(response) {
                $("#exampleModalCenterTitle").html("Producto");
                $("#modalBody").html(response.responseText);    
                $("#exampleModalCenter").modal('show');
                $("#createProduct").hide();
                $("#saveChangesProduct").show();
            },
            error: function() {
                console.error('Ha ocurrido un error');
            }
        });
    });
    $('#saveChangesProduct').click(function() {
        let errorsReport = ""
        const idProduct = $("#idProduct").val();
        const nameProduct = $("#nameProduct").val();
        const descripcionProduct = $("#descripcionProduct").val();
        const priceProduct = $("#priceProduct").val();
        const inventoryProduct = $("#inventoryProduct").val();
        if (idProduct === undefined || idProduct === "") {
            errorsReport += "El ID no esta definido, vuelve a seleccionar el producto.\n"
        }
        errorsReport = validateFields(errorsReport, nameProduct, descripcionProduct, priceProduct, inventoryProduct)
        if (errorsReport.length === 0) {
            $.ajax({
                type: "POST",
                url: "/putProduct/",
                data: {csrfmiddlewaretoken:csrftoken, id:idProduct, name_product: nameProduct, descrip_product: descripcionProduct, price_product: priceProduct, inventory_product: inventoryProduct},
                async : false,
                complete: function(response) {
                    if (response.responseJSON !== undefined && response.responseJSON['error'] && Array.isArray(response.responseJSON['error'])) {
                        if (response.responseJSON['error'] && response.responseJSON['error'].length !== 0) {
                            response.responseJSON['error'].forEach(function (text) {
                                errorsReport += text
                            })
                            $("#errorsReport").html(errorsReport);
                            $("#alertProduct").show();
                        } else {
                            window.location.reload();
                        }
                    }
                },
                error: function() {
                    console.error('Ha ocurrido un error');
                }
            });
        } else {
            $("#errorsReport").html(errorsReport);
            $("#alertProduct").show();
        }
    });
    $('.delete_product').click(function() {
        let value_id = $(this).attr("id");
       $.ajax({
            type: "POST",
            url: "/deleteProduct/",
            data: {csrfmiddlewaretoken:csrftoken, id:value_id},
            async : false,
            complete: function(response) {
                if (response.responseJSON !== undefined && response.responseJSON['error'] && Array.isArray(response.responseJSON['error'])) {
                    if (response.responseJSON['error'] && response.responseJSON['error'].length !== 0) {
                        response.responseJSON['error'].forEach(function (text) {
                            errorsReport += text
                            console.log(text)
                        })
                        $("#errorsReport").html(errorsReport);
                        $("#alertProduct").show();
                    } else {
                        window.location.reload();
                    }
                }
            },
            error: function() {
                console.error('Ha ocurrido un error');
            }
        });
    });
});