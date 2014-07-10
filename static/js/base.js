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



    var confirmationOk      = null;
    var confirmationDeby    = null;
    

    confirmModalDialog  =function (title, msg, okconfirm, denyconfirm){
        confirmationOk   = okconfirm;
        confirmationDeby = denyconfirm;
        $("#confirmTitle").html(title);
        $("#confirmBody").html(msg);
        $("#confirmModal").modal("show");
    }
    
    
    
    
        $("#confirmSave").click(function(){
            $("#confirmModal").modal("hide");
            return confirmationOk.apply(this);
            
        });
        $("#confirmClose").click(confirmationDeby);
        $("#closeConfirmModal").click(confirmationDeby);


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