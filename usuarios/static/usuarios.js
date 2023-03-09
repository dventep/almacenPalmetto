$(document).ready(function() {    
    const csrftoken =  window.CSRF_TOKEN;
    function validateFields (errorsReport = "", nameUser = "", lastnameUser = "", userUser = "", passwordUser = "", telephoneUser = "", emailUser = "") {
        $("#errorsReport").html("");
        $("#alertUser").hide();
        if (nameUser === undefined || nameUser === "") {
            errorsReport += "El nombre no puede estar vacío.\n"
        }
        if (lastnameUser === undefined || nameUser === "") {
            errorsReport += "El apellido no puede estar vacío.\n"
        }
        if (userUser === undefined || userUser === "") {
            errorsReport += "El usuario no puede estar vacío.\n"
        }
        if (passwordUser === undefined || passwordUser === "") {
            errorsReport += "La contraseña no puede estar vacía.\n"
        }
        if (telephoneUser === undefined || telephoneUser === "") {
            errorsReport += "El telefono no puede estar vacío.\n"
        }
        if (emailUser === undefined || emailUser === "") {
            errorsReport += "El email no puede estar vacío.\n"
        }
        return errorsReport
    };
    $('#goToUser').click(function() {
       $.ajax({
            type: "POST",
            url: "/usuarios/goToUser/",
            data: {csrfmiddlewaretoken:csrftoken},
            async : false,
            complete: function(response) {
                $("#exampleModalCenterTitle").html("Usuario");
                $("#modalBody").html(response.responseText);    
                $("#exampleModalCenter").modal('show');
                $("#createUser").show();
                $("#saveChangesUser").hide();
            },
            error: function() {
                console.error('Ha ocurrido un error');
            }
        });
    });
    $('#createUser').click(function() {
        let errorsReport = ""
        const nameUser = $("#nameUser").val();
        const lastnameUser = $("#lastnameUser").val();
        const userUser = $("#userUser").val();
        const passwordUser = $("#passwordUser").val();
        const telephoneUser = $("#telephoneUser").val();
        const emailUser = $("#emailUser").val();
        errorsReport = validateFields(errorsReport, nameUser, lastnameUser, userUser, passwordUser, telephoneUser, emailUser)
        if (errorsReport.length === 0) {
            $.ajax({
                type: "POST",
                url: "/usuarios/createUser/",
                data: {csrfmiddlewaretoken:csrftoken, name_user: nameUser, lastname_user: lastnameUser, user_user: userUser, password_user: passwordUser, telephone_user: telephoneUser, email_user: emailUser},
                async : false,
                complete: function(response) {
                    if (response.responseJSON !== undefined && response.responseJSON['error'] && Array.isArray(response.responseJSON['error'])) {
                        if (response.responseJSON['error'] && response.responseJSON['error'].length !== 0) {
                            response.responseJSON['error'].forEach(function (text) {
                                errorsReport += text
                            })
                            $("#errorsReport").html(errorsReport);
                            $("#alertUser").show();
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
            $("#alertUser").show();
        }
    });
    $('.edit_user').click(function() {
        let value_id = $(this).attr("id");
       $.ajax({
            type: "POST",
            url: "/usuarios/getUser/",
            data: {csrfmiddlewaretoken:csrftoken, id:value_id},
            async : false,
            complete: function(response) {
                $("#exampleModalCenterTitle").html("Usuario");
                $("#modalBody").html(response.responseText);    
                $("#exampleModalCenter").modal('show');
                $("#createUser").hide();
                $("#saveChangesUser").show();
            },
            error: function() {
                console.error('Ha ocurrido un error');
            }
        });
    });
    $('#saveChangesUser').click(function() {
        let errorsReport = ""
        const idUser = $("#idUser").val();
        const nameUser = $("#nameUser").val();
        const lastnameUser = $("#lastnameUser").val();
        const userUser = $("#userUser").val();
        const passwordUser = $("#passwordUser").val();
        const telephoneUser = $("#telephoneUser").val();
        const emailUser = $("#emailUser").val();
        if (idUser === undefined || idUser === "") {
            errorsReport += "El ID no esta definido, vuelve a seleccionar el usero.\n"
        }
        errorsReport = validateFields(errorsReport, nameUser, lastnameUser, userUser, passwordUser, telephoneUser, emailUser)
        if (errorsReport.length === 0) {
            $.ajax({
                type: "POST",
                url: "/usuarios/putUser/",
                data: {csrfmiddlewaretoken:csrftoken, id:idUser, name_user: nameUser, lastname_user: lastnameUser, user_user: userUser, password_user: passwordUser, telephone_user: telephoneUser, email_user: emailUser},
                async : false,
                complete: function(response) {
                    if (response.responseJSON !== undefined && response.responseJSON['error'] && Array.isArray(response.responseJSON['error'])) {
                        if (response.responseJSON['error'] && response.responseJSON['error'].length !== 0) {
                            response.responseJSON['error'].forEach(function (text) {
                                errorsReport += text
                            })
                            $("#errorsReport").html(errorsReport);
                            $("#alertUser").show();
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
            $("#alertUser").show();
        }
    });
    $('.delete_user').click(function() {
        let value_id = $(this).attr("id");
       $.ajax({
            type: "POST",
            url: "/usuarios/deleteUser/",
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
                        $("#alertUser").show();
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