$(document).ready(function () {
    $(".showDetail").click(function(){
       var id=$(this).attr("internalid");
       $("#taskid").attr("value", id);
       $("#frmDetail").submit();
        
    });
});