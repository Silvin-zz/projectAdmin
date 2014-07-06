/**
this is the base javascript from the project 
its loaded everytime whith the base template.
silvio.bravo :D
**/




$("#loadingModal").modal({ keyboard: false, show:false, backdrop: "static" });
$("#confirmModal").modal({ keyboard: false, show:false, backdrop: "static" });



/*
    Custom Modal :D from all project :D
*/


$(document).ready(function(){


    

    confirmModalDialog  =function (title, msg, okconfirm, denyconfirm){
        $("#confirmTitle").html(title);
        $("#confirmBody").html(msg);
        $("#confirmModal").modal("show");
        $("#confirmSave").click(okconfirm);
        $("#confirmClose").click(denyconfirm);
        $("#closeConfirmModal").click(denyconfirm);
    }


    SPNotification= function (type, title, message){


        $.pnotify({
            title       : title,
            text        : message,
            type        : type,
            icon        : 'glyphicon glyphicon-bell',
            shadow      : true,
            animation   : 'slide'
        });

    }



// Notificaciones :D:D:D



});