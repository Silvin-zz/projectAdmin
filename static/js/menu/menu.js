$(document).ready(function(){
   
   $("#new").click(function(){
       
     $("#menuAction").attr("value","new");
     $("#menuId").attr("value", "");
   });
   
   $("#menuSave").click(function(){
       
        $.ajax({  
      
                    url   : "/admin/menu/new",
                    type    : "POST",
                    dataType: "JSON",
                    data    : $("#frmMenu").serialize(),
                    success : function(result){
                            if(result.success=="true"){
                                addNewUser(result.data)
                                $('#userModal').modal('hide');
                            }
            
                      }
        });
      
       
   });
   
   
   function addNewUser(obj){
       
       cad ='<tr><td>';
       cad = cad + '<i class="'+ obj.iconclass +'">';
       cad = cad + obj.iconclass + '<div class="color-swatch brand-primary"></div></td>';
       cad = cad + '<td>' + obj.name + '</td><td>'+ obj.url +'</td><td>';
       cad = cad + '<button class="btn btn-xs btn-primary btn-flat taskdetail" title="edit"     action="edit"  lang="' + obj.id + '" data-toggle="modal" data-target="#userModal"><i class="glyphicon glyphicon-pencil white"></i></button>';
       cad = cad + '<button class="btn btn-xs btn-primary btn-flat taskdetail" title="remove"   action="edit"  lang="' + obj.id + '" data-toggle="modal" data-target="#userModal"><i class="glyphicon glyphicon-remove white"></i></button>';
       cad = cad + '</td></tr>';
       $("#usersBody").prepend(cad);
   }
    
});