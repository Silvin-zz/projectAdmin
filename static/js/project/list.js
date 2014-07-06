$(document).ready(function(){


    $(".remove").click(function(){
        var id          =$(this).attr("data");
        var rowContent  =$(this).parent().parent();

        //Styles
        rowContent.parent().parent().removeClass('table-striped');
        $(rowContent).addClass("danger");
        
        //custom Confirm :D from bootstrap :D
        confirmModalDialog("Remove Project", "¿ Are you Sure to remove this Project ?", 
            function(){
                $("#loadingModal").modal("show");
                $("#projectId").val(id);
                $.ajax({  

                    url     : "/projects/delete",
                    type    : "POST",
                    data    : $("#projectForm").serialize(),

                    success : function(result){
                        $("#loadingModal").modal("hide");
                        rowContent.fadeOut('slow', function() {
                            tablecontent=rowContent.parent().parent();
                            rowContent.remove();
                            tablecontent.addClass('table-striped');
                        });    
                    }

                });
            },
            function(){  //Cancel confirm
                rowContent.parent().parent().addClass('table-striped');
                rowContent.removeClass("danger");            
            }
        );
    });


    $(".edit").click(function(){
        var id =$(this).attr("data");
        $("#projectId").val(id);
        $("#projectForm").attr("action", "/projects/new")
        $("#projectForm").submit();

    });

});